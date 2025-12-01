# CS361 Microservice 3: Image Microservice
# Trent Scoggins
# Used Assignment 4 as a starting point, heavily modified after.

import os, zmq

# Path to images (generated in main program/additional microservice)
folder_path = os.getcwd() +  "/team-fortress-2"

# set up the environment 
context = zmq.Context()
print("Attempting to connect to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5002")

# Send folder path for server to package images
print(f"Sending parameters: /team-fortress-2")
socket.send_string(folder_path)

# receive confirmation from server
return_obj = socket.recv_pyobj()
# print out confirmation
if type(return_obj) == str:
    print("Error: " + return_obj)

print(f"Dictionary recieved, verifying integrity")
for key, value in return_obj.items():
    print(f"{key}: {value}")

# Close connection to server
socket.send_string("Q") 
