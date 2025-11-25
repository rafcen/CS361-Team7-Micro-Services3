# CS361 Microservice 3: Image Microservice
# Trent Scoggins
# Used Assignment 4 as a starting point, heavily modified after.

import os, zmq

# Path to images (generated in main program/additional microservice)
folder_path = os.getcwd() + "/team-fortress-2"

# set up the environment
context = zmq.Context()
print("Attempting to connect to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5002")

# Send folder path for server to package images
print(f"Sending parameters: /team-fortress-2")
socket.send_string(folder_path)

# receive confirmation from server
return_dict = socket.recv_pyobj()
# check for empty dictionary (no images found), if no images, exit program
if not return_dict:
    print("No images received, exiting program")
    socket.send_string("Q")
    exit()
# print out confirmation
print(f"Dictionary received, verifying integrity")
for key, value in return_dict.items():
    print(f"{key}: {value}")

# Close connection to server
socket.send_string("Q")
