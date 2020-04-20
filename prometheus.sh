#!/bin/bash 
# This script is used to install prometheus on Amazon Linux AMI
# Link for help https://devopscube.com/install-configure-prometheus-linux/

# Update system
sudo yum update -y

# Add users
sudo useradd --no-create-home --shell /bin/false prometheus
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
sudo chown prometheus:prometheus /etc/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus


# Download prometheus from a link
# Releases are shown here https://github.com/prometheus/prometheus/releases
curl -LO https://github.com/prometheus/prometheus/releases/download/v2.3.2/prometheus-2.3.2.linux-amd64.tar.gz
tar -xvf prometheus-2.3.2.linux-amd64.tar.gz
mv prometheus-2.3.2.linux-amd64 prometheus-files


# Copy binaries
sudo cp prometheus-files/prometheus /usr/local/bin/
sudo cp prometheus-files/promtool /usr/local/bin/
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool

# Move console files
sudo cp -r prometheus-files/consoles /etc/prometheus
sudo cp -r prometheus-files/console_libraries /etc/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries


# Creates prometheus config file
sudo bash -c 'cat > /etc/prometheus/prometheus.yml' <<EOF
global:
  scrape_interval: 10s
  evaluation_interval: 1s

scrape_configs:
  - job_name: 'prometheus'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    ec2_sd_configs:
      - region: us-east-1
        port: 9100
  - job_name: 'node_exporter'
    static_configs:
    - targets: ['localhost:9100']
EOF


# Change permission
sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml



# Creates Systemd service
sudo bash -c 'cat > /etc/systemd/system/prometheus.service' <<EOF
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target
 
[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries
 
[Install]
WantedBy=multi-user.target
EOF


# Restarts
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
sudo systemctl status prometheus




