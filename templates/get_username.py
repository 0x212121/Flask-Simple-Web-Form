import subprocess
# import socket
# print(socket.gethostname())
# a = socket.gethostbyaddr("172.16.7.78")
# print(a)
# print(socket.getfqdn("8.8.8.8"))
# print(socket.getfqdn("localhost"))
# # print(socket.)
def get_username(username):
    s1 = subprocess.check_output(f'net user "{username}" /domain', shell=True)

    r = str(s1).split("\\r\\n")
    x = r[3].split("   ")
    fullname = x[-1].strip()
    return fullname