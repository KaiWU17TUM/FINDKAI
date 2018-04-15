import numpy as np
import face_recognition as fr
import cv2
import os

class Classifier:
	UNKNOWN = "Unknown"
	def __init__(self):
		self.KnownFaces = []
		self.KnownLabels = []

	def train(self,data_dir):
		included_extenstions = ['jpeg']
		images = [fn for fn in os.listdir(data_dir)
			if any(fn.endswith(ext) for ext in included_extenstions)]
		for image in images:
			label = os.path.splitext(image)[0]
			image = data_dir+"/"+image
			print(label)
			#self.KnownFaces.push(fr.face_encodings(fr.load_image_file(image)[0]))
			print(image)
			im = fr.load_image_file(image)
			#cv2.imshow('image', im)
			print("==>",np.shape(im),np.shape(fr.face_encodings(im)))
			im_encoding = fr.face_encodings(im)
			if len(im_encoding)>0 :
				im_encoding = im_encoding[0]
			else:
				print("no face found in image!")
				return
			self.KnownFaces.append(im_encoding)
			#self.KnownFaces.append(fr.face_encodings(fr.load_image_file(image)[0]))
			#self.KnownLabels.push(label)
			self.KnownLabels.append(label)

	def findFaces(self,image):
		smaller_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
		print("smaller-image-size : ",np.shape(smaller_image))
		# Find all the faces and face encodings in the current frame of video
		face_locations = fr.face_locations(smaller_image)
		face_encodings = fr.face_encodings(smaller_image, face_locations)
		face_names = []
		for face in face_encodings:
            # See if the face is a match for the known face(s)
			matches = fr.compare_faces(self.KnownFaces, face)
			name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
			if True in matches:
				first_match_index = matches.index(True)
				name = self.KnownLabels[first_match_index]
			face_names.append(name)

		return face_encodings,face_locations,face_names






