import flask
from flask import request, jsonify
from PIL import Image, ImageDraw
import requests
import numpy as np
import face_recognition


# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]
print('Learned encoding for', len(known_face_encodings), 'images.')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>seps xd.</p>"

@app.route('/api', methods=['GET'])
def api():
	username = request.args.get('username')
	print(username)
	password= request.args.get('password')
	print(password)
	return "<h1>Distant  Archive</h1>" + username + " " + password

@app.route('/req', methods=['GET'])
def req():
	# Load an image with an unknown face
	unknown_image = face_recognition.load_image_file("Obama2.jpg")

	# Find all the faces and face encodings in the unknown image
	face_locations = face_recognition.face_locations(unknown_image)
	face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
	
	name = "Unknown"
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
	    # See if the face is a match for the known face(s)
	    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

	    name = "Unknown"

	    # Or instead, use the known face with the smallest distance to the new face
	    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
	    best_match_index = np.argmin(face_distances)
	    if matches[best_match_index]:
	        name = known_face_names[best_match_index]
	return name