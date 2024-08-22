from PIL import ImageGrab

px = ImageGrab.grab().load()
for x in range(719, 720, 10):
    for y in range(359, 360, 10):
        color = px[x, y]
        
print(color)

for x in range(719, 720, 10):
    for y in range(359, 360, 10):
        color = px[x, y]