#in the name of null...!!
import socket
from threading import Thread
import os
os.system("pip install pysocket")
os.system("clear")
ip = input("Enter The Ip Addres : ")
port = int(input("Enter The Port Number : "))
name = input("Enter The User Name : ")
def rmessage():
    print("Waiting To Connect User ...")
    print("\n")
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.bind((ip , port))
    s.listen(5)
    client , addr = s.accept()
    print("new user Connected : {}".format(addr))
    print("\n")
    print("Waiting To send Message ...")
    #c = "Connected Succesfully...!"
        
    #client.send(c.encode())
     
    while True:
        cmessage = client.recv(1024).decode()
        print(cmessage)
        print("\n")
        txt = input("Enter The Maessage : ")
        mm = "{} > {}".format(name,txt)
        client.send(mm.encode())
        print("\n")
        print("Wait For answer ...")
        print("\n")
        
        
if __name__ == "__main__":
    rmessage()
else:
    pass