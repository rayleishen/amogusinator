#guide https://www.geeksforgeeks.org/mouse-library-in-python/
#docs https://github.com/boppreh/mouse#api
import mouse

# left click
mouse.click('left')
# right click
mouse.click('right')
# middle click
mouse.click('middle')


# get the current location of your mouse
mouse.get_position() 
#current position of the mouse using the "position" function
position = mouse.position()
print(position)

mouse.move_relative(10, 20)
#mouse cursor relative to its current position
