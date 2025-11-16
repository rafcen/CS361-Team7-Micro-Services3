# CS361 Microservice 3: Image Microservice
# Trent Scoggins
# Used Assignment 4 as a starting point, heavily modified after.

import glob, os, zmq

# set up the environment 
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5002")
print("Connected to port tcp://*:5002")

# listen until we hear from the client
while True:
    return_dict = {}
    image_path = socket.recv()
    
    if len(image_path) > 0:
        image_path_str = image_path.decode()
        # maintain exit functionality
        if image_path_str == 'Q': 
            break

        print(f"Received folder path: {image_path_str}")
        # Using glob, pick only files that are valid image files
        images = []
        image_extensions = ["/*.jpeg", "/*.jpg", "/*.png", "/*.webp"]
        for extension in image_extensions:
            images.extend(glob.glob(image_path_str + extension))

        # Break if directory is empty
        if not images:
            print(f"Directory provided has no images")
            break

        sorted_images = sorted(images)

        # loop through each and add it to a dict
        # key = image[number]
        # value = path to image
        for image in range(len(sorted_images)):
            return_dict["image" + str(image + 1)] = os.path.join(image_path_str, sorted_images[image])

        print(f"Image dictionary created, sending to client")
        # Send reply back to client
        socket.send_pyobj(return_dict)

# Make a clean exit.
context.destroy()