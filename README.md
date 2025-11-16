# CS361 Microservice 3: Image Microservice
#
# Send the server a folder path, it will reply with a dictionary of the images
# in the folder with the key being the image name and value being the path to the image.
# The image microservice sorts through the given folder to pick images files of type
# jpeg/jpg, png, and webp. If there are no images of those types, or if the folder is
# empty, the server will print an error to the console and destroy itself.
# 
# Communication Contract
# REQUEST parameters: folder_path
# Example Call:
#   socket.send_string(folder_path)
#
# RECEIVE parameters: image_dictionary
# Example Call:
#   socket.send_json(image_dictionary)