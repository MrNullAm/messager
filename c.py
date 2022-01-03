#in the name of null...!
import socket
import os
os.system("pip install pysocket")
os.system("clear")
from threading import Thread
ip = input("Enter Ip Addres : ")
port = int(input("Enter The Port Number : "))
name = input("Enter The User Name : ")
def recive():
    s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip , port))
    while True:
        print("\n")
        message = input("Enter The Message : ")
        mmm = "{} > {}".format(name,message)
        s.send(mmm.encode())
        print("\n")
        print("Wait For answer ...")
        print("\n")
        print(s.recv(1028).decode())
        print("\n")
if __name__ == "__main__":
    recive()
else:
    pass
