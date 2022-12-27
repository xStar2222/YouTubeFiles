from PIL import Image

im = Image.open('dice.png')

im = im.convert('RGB')

im.save('image.jpeg', 'JPEG')
