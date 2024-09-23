#!/usr/bin/python3

from PIL import Image, ImageFilter
import PIL 
import glob
from sightengine.client import SightengineClient

client = SightengineClient('994769317', 'EqdmT9ANjLp52GD2wPyf')
client.check('nudity', 'wad').video('https://www.youtube.com/watch?v=a5YuOEn0cCA', 'https://example.com/yourcallback')

for video in glob.glob("*"):
	try:
		#Chec for nude images
		nudes = client.check('nudity', 'wad').video('https://www.youtube.com/watch?v=a5YuOEn0cCA', 'https://example.com/yourcallback')
		nude = nudes["nudity"]["raw"]
		not_Nude = nudes["nudity"]["safe"]
		alcohol = violence["alcohol"]
		weapon = violence["weapon"]
		drugs = violence["drugs"]

		if alcohol > 0.1 or weapon > 0.1 or drugs > 0.1:
			#call the chec content function
			checkContent(video)
			unsafe.append(video)
		if nude > not_Nude:
			#call the chec content function
			checkContent(video)
			unsafe.append(video)

	except:
		print(f"{video} Not readable")
		print("Loadng.... ")

print("unsafe content:")