# CS361 Microservice 3: Image Microservice

Send the server a folder path, it will reply with a dictionary of the images
in the folder with the key being the image name and value being the path to the image.
The image microservice sorts through the given folder to pick images files of type
jpeg/jpg, png, and webp. If there are no images of those types, or if the folder is
empty, the server will print an error to the console and destroy itself.

# How to Run This Microservice

1. Create and activate the virtual environment

python3 -m venv venv
source venv/bin/activate        # Linux/macOS


2. Install dependencies

pip install -r requirements.txt

3. Start the microservice

python3 server.py

Expected output:

Connected to port tcp://*:5002



# Communication Contract

How to programmatically request and recieve data from this microservice:

- Server requires a folder path to be explicity provided

### How to Request Data

REQUEST parameters: folder_path
Parameter | Type | Description
--------- | ---- | -----------
folder_path | str | path to folder containing valid images

Example Call:
'''
  import os, zmq

  folder_path = os.getcwd() +  "/team-fortress-2"

  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5002")

  socket.send_string(folder_path)
'''

### How to Receive Data

Successful Python Dictionary Response:

'''
{
  "image1": "/Users/trentscoggins/Documents/OSU/CS361/Microservice3/CS361-Team7-Micro-Services3/team-fortress-2/boxart.jpg"
  "image2": "/Users/trentscoggins/Documents/OSU/CS361/Microservice3/CS361-Team7-Micro-Services3/team-fortress-2/image1.jpg"
  "image3": "/Users/trentscoggins/Documents/OSU/CS361/Microservice3/CS361-Team7-Micro-Services3/team-fortress-2/image2.jpg"
  "image4": "/Users/trentscoggins/Documents/OSU/CS361/Microservice3/CS361-Team7-Micro-Services3/team-fortress-2/image3.jpg"
  "image5": "/Users/trentscoggins/Documents/OSU/CS361/Microservice3/CS361-Team7-Micro-Services3/team-fortress-2/image4.jpg"
}
'''

Error Response Format:

'''
  "Directory provided has no valid images"
'''
Example Call:

'''
return_obj = socket.recv_pyobj()

if type(return_obj) == str:
    print("Error: " + return_obj)

for key, value in return_obj.items():
    print(f"{key}: {value}")
'''
  
![UML Diagram](/UML_diagram.png)
