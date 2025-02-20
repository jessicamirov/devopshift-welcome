import subprocess

cmd = "wsl systemctl status nginx"

try:
    p = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode == 0:
        output = p.stdout.decode()
        if "active (running)" in output:
            print("running")
            exit(0)  # Exit with success code (0), not error code (1)
        else:
            print("not running")
    else:
        print(p.stderr.decode())
except Exception:
    print("error")