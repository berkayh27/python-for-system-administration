#!/bin/bash


# Creates a repo
sudo bash -c 'cat > /etc/yum.repos.d/grafana.repo' <<EOF
[grafana]
name=grafana
baseurl=https://packages.grafana.com/oss/rpm
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://packages.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
EOF

# Installs Grafana
sudo yum install grafana  fontconfig freetype* urw-fonts  -y


# Starts Grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server.service
sudo systemctl status grafana-server
