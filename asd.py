from PIL import Image

img = Image.open('background.jpg')
img = img.resize((600, 600))
img.save('background.jpg')