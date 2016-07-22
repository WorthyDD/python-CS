
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

im = Image.open('two-cats.jpg')

w,h = im.size
print('origin image size (%s, %s)' % (w,h))

# im.thumbnail((200,200))
# im.save('thumb.jpg','jpeg')

# im2 = im.filter(ImageFilter.BLUR)
# im2.save('im2.jpg','jpeg')

def randChar():
    return chr(random.randint(65,90))

def randColor1():
    return (random.randint(64,255), random.randint(64,255), random.randint(65,255))

def randColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60*4
height = 60

image = Image.new('RGB', (width,height), (255,255,255))
font = ImageFont.truetype('Arial.ttf',36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=randColor1())

for t in range(4):
    draw.text((60*t+10, 10), randChar(), font = font, fill = randColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
