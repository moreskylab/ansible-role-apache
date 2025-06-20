import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache_installed(host):
    # Check if package is installed
    if host.system_info.distribution in ['debian', 'ubuntu']:
        apache = host.package('apache2')
    else:
        apache = host.package('httpd')
    assert apache.is_installed


def test_apache_running_and_enabled(host):
    # Check if service is running and enabled
    if host.system_info.distribution in ['debian', 'ubuntu']:
        service = host.service('apache2')
    else:
        service = host.service('httpd')
    assert service.is_running
    assert service.is_enabled


def test_apache_listening(host):
    # Check if Apache is listening on configured port
    socket = host.socket("tcp://0.0.0.0:8080")
    assert socket.is_listening


def test_config_file(host):
    # Check if config files exist with proper permissions
    if host.system_info.distribution in ['debian', 'ubuntu']:
        config_file = host.file('/etc/apache2/sites-available/test.conf')
    else:
        config_file = host.file('/etc/httpd/conf.d/test.conf')

    assert config_file.exists
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == 0o644


def test_document_root_exists(host):
    # Check if document root directory exists
    doc_root = host.file('/var/www/test')
    assert doc_root.exists
    assert doc_root.is_directory
