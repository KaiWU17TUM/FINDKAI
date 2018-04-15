import cv2 as CV2
import os
from PIL import Image
import numpy as np

class ImageModule:
	def __init__(self):
		#self.take_photo()
		#self.save()
		print("image module initialized!")

	def take_photo(self):
		cam = CV2.VideoCapture(0)
		CV2.namedWindow("Photoing")
		ret, frame = cam.read()
    	#cv2.imshow("Photoing", frame)
		rgb_frame = frame[:, :, ::-1]	
		#print("{} written!".format(img_name))
		cam.release()
		CV2.destroyAllWindows()
		return rgb_frame

	def save(self, image, name, path):
		image_pil = Image.fromarray(image)
		print(image_pil.mode)
		image_pil.save(path+"/"+name+".jpeg")
		#CV2.imwrite(os.path.join(path, name), image)		