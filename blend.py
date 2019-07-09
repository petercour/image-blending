from PIL import Image

Im = Image.open("lena.jpg")
print(Im.mode,Im.size,Im.format)
Im.show()

newIm = Image.new ("RGBA", (640, 480), (255, 0, 0))
Im2 = Image.open("flower.jpg").convert(Im.mode)
Im2 = Im2.resize(Im.size)
Im2.show()

img = Image.blend(Im,Im2,0.5)
img.show()

