# Python3 one-liner shell upgrade

python3 -c 'import pty; pty.spawn("/bin/bash")' && stty raw -echo && fg

# Python2 one-liner shell upgrade

python -c 'import pty; pty.spawn("/bin/bash")' && stty raw -echo && fg