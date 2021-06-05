import subprocess

def get_username(username):
    s1 = subprocess.check_output(f'net user "{username}" /domain', shell=True)

    r = str(s1).split("\\r\\n")
    x = r[3].split("   ")
    fullname = x[-1].strip()
    return fullname