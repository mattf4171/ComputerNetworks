#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:27:09 2021

@author: matthewfernandez
"""

from socket import *
import threading
​
i = 0
sentences = []
​
def catch_msg(socket, name):
	global i, sentences
	sentences.append(socket.recv(1024).decode())
	msg = name + " Sent message: " + sentences[i]
	print(msg)
	i += 1
​
​
​
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(2)
print("The server is ready to receive")
​
while True:
	connectionSocketX,addrX = serverSocket.accept()
	print("Accepted first connection, calling it connection X")
	connectionSocketX.send("Client X connected".encode())
	
	connectionSocketY,addrY = serverSocket.accept()
	print("Accepted second connection, calling it connection Y")
	connectionSocketY.send("Client Y connected".encode())
​
	print("\nWaiting to receive messages from client X and client Y\n")
​
	t1 = threading.Thread(target=catch_msg,args = (connectionSocketX,"Client X"))
	t2 = threading.Thread(target=catch_msg,args = (connectionSocketY,"Client Y"))
	t1.start()
	t2.start()
	t2.join()
	t1.join()
​
	msg = sentences[0] + " received before " + sentences[1]
	connectionSocketX.send(msg.encode())
	connectionSocketY.send(msg.encode())	
​
	connectionSocketX.close()
	connectionSocketY.close()
