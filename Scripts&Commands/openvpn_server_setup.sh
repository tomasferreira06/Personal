# Variables - Change these as needed
SERVER_IP="your_server_ip"
CLIENT_NAME1="windows"
CLIENT_NAME2="linux"
EASY_RSA_DIR=~/etc/openvpn-ca/easy-rsa
SERVER_NAME="chewy"

# Install OpenVPN and Easy-RSA
sudo apt update
sudo apt install -y openvpn easy-rsa

# Set up Easy-RSA
make-cadir $EASY_RSA_DIR
cd $EASY_RSA_DIR

# Initialize the PKI
./easyrsa init-pki

# Build the CA (Certificate Authority)
./easyrsa --batch build-ca

# Generate the Server Certificate and Key
./easyrsa gen-req $SERVER_NAME
./easyrsa --batch sign-req server server

# Generate Diffie-Hellman Parameters
./easyrsa gen-dh

# Generate a Shared TLS Key
openvpn --genkey secret ta.key

# Copy Files to OpenVPN Directory
sudo cp pki/ca.crt pki/issued/$SERVER_NAME.crt pki/private/$SERVER_NAME.key pki/dh.pem ta.key /etc/openvpn

# Create the Server Configuration File
sudo bash -c "cat <<EOF > /etc/openvpn/$SERVER_NAME.conf
port 1194
proto udp
dev tun
ca ca.crt
cert $SERVER_NAME.crt
key $SERVER_NAME.key
dh dh.pem
tls-auth ta.key 0
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status /var/log/openvpn-status.log
log /var/log/openvpn.log
verb 3
EOF"

# Enable IP Forwarding
sudo sed -i "s/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/" /etc/sysctl.conf
sudo sysctl -p

# Configure Firewall
sudo ufw allow 1194/udp
sudo ufw enable

# Start and Enable OpenVPN Service
sudo systemctl start openvpn@$SERVER_NAME
sudo systemctl enable openvpn@$SERVER_NAME

# Generate Client Keys and Certificates
./easyrsa gen-req $CLIENT_NAME1
./easyrsa sign-req client $CLIENT_NAME1
./easyrsa gen-req $CLIENT_NAME2
./easyrsa sign-req client $CLIENT_NAME2

# Create Client Configuration Directory
mkdir -p ~/client-configs/keys

# Create Client Configuration File
cat <<EOF > ~/client-configs/base.conf
client
dev tun
proto udp
remote $SERVER_IP 1194
resolv-retry infinite
nobind
user nobody
group nogroup
persist-key
persist-tun
ca ca.crt
cert $CLIENT_NAME1.crt
key $CLIENT_NAME1.key
tls-auth ta.key 1
cipher AES-256-CBC
verb 3
EOF

# Copy Client Keys and Certificates
cp pki/ca.crt ~/client-configs/keys/
cp pki/issued/$CLIENT_NAME1.crt ~/client-configs/keys/
cp pki/private/$CLIENT_NAME1.key ~/client-configs/keys/
cp pki/issued/$CLIENT_NAME2.crt ~/client-configs/keys/
cp pki/private/$CLIENT_NAME2.key ~/client-configs/keys/
cp ta.key ~/client-configs/keys/

# Script to Package Client Configuration
cat <<'EOF' > ~/client-configs/make_config.sh
#!/bin/bash

KEY_DIR=~/client-configs/keys
OUTPUT_DIR=~/client-configs/files
BASE_CONFIG=~/client-configs/base.conf

mkdir -p \${OUTPUT_DIR}

for NAME in "$@"; do
    cat \${BASE_CONFIG} \
        <(echo -e '<ca>') \
        \${KEY_DIR}/ca.crt \
        <(echo -e '</ca>\n<cert>') \
        \${KEY_DIR}/\${NAME}.crt \
        <(echo -e '</cert>\n<key>') \
        \${KEY_DIR}/\${NAME}.key \
        <(echo -e '</key>\n<tls-auth>') \
        \${KEY_DIR}/ta.key \
        <(echo -e '</tls-auth>') \
        > \${OUTPUT_DIR}/\${NAME}.ovpn
done
EOF

chmod +x ~/client-configs/make_config.sh

# Generate Client Configuration Files
~/client-configs/make_config.sh $CLIENT_NAME1 $CLIENT_NAME2

echo "OpenVPN setup complete. Client configurations are available in ~/client-configs/files/"

