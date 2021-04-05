#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:27:37 2021

@author: matthewfernandez
"""

from socket import * # modules needed
​
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort))
​
sentence = clientSocket.recv(1024)
print("From Server: ", sentence.decode())
​
sentence = input("Enter message to send to server:")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())
​
clientSocket.close() # close port, no longer need it
