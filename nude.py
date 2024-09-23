#!/usr/bin/python3

from PIL import Image, ImageFilter
import PIL 
import glob
from sightengine.client import SightengineClient

client = SightengineClient('994769317','EqdmT9ANjLp52GD2wPyf')
unsafe = []

#Check content function
def checkContent(file):
	im1 = Image.open(file) 
	blurred_image = im1.filter(ImageFilter.GaussianBlur(radius=10))
	  
	# save a image using extension
	im1 = blurred_image.save(f"output/{file}") 

for image in glob.glob("*"):
	try:
		#Chec for nude images
		nudes = client.check('nudity').set_file(image)
		nude = nudes["nudity"]["raw"]
		not_Nude = nudes["nudity"]["safe"]

		#Check for images with alcohol, drugs, weapons
		violence = client.check('wad').set_file(image)
		alcohol = violence["alcohol"]
		weapon = violence["weapon"]
		drugs = violence["drugs"]

		if alcohol > 0.1 or weapon > 0.1 or drugs > 0.1:
			#call the chec content function
			checkContent(image)
			unsafe.append(image)
		if nude > not_Nude:
			#call the chec content function
			checkContent(image)
			unsafe.append(image)

	except:
		print(f"{image} Not readable")
		print("Loadng.... ")

print("unsafe images:")
print(file for file in unsafe)