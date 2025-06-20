# Ansible Role: Apache

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-yourusername.apache-blue.svg)](https://galaxy.ansible.com/yourusername/apache)
[![Build Status](https://github.com/yourusername/ansible-role-apache/workflows/CI/badge.svg)](https://github.com/yourusername/ansible-role-apache/actions)

A production-ready Ansible role to install and configure Apache HTTP Server with various security and performance optimizations.

## Requirements

- Ansible 2.10 or higher
- Supported platforms:
  - Ubuntu 20.04 (Focal), 22.04 (Jammy)
  - Debian 11 (Bullseye), 12 (Bookworm)
  - EL 8, 9 (Rocky Linux, AlmaLinux, etc.)

## Role Variables

```yaml
# Basic configuration
apache_listen_port: 80
apache_listen_port_ssl: 443
apache_server_name: "{{ inventory_hostname }}"

# Virtual hosts
apache_vhosts:
  - name: default
    server_name: "{{ apache_server_name }}"
    document_root: "/var/www/html"
    enable_ssl: false

# SSL configuration
apache_enable_ssl: false

