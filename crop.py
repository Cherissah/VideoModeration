from PIL import Image, ImageFilter
image=Image.open('three.jpeg')
#image.show()
cropped_image = image.crop((310,290,420,355))
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=10))
image.paste(blurred_image, (310,290,420,355))
#cropped_image.show()
blurred_image.show()
#image.show()