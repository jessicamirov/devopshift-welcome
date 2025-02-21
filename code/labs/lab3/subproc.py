import subprocess

cmd = "wsl ls -l /var/log"
try:
    p = subprocess.run(cmd.split(), stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    if p.returncode == 0:
        print(p.stdout.decode())
    else:
        print(p.stderr.decode())
except FileNotFoundError:
    print("ERROR: File not found")
except PermissionError:
    print("ERROR: Permmission denied")
