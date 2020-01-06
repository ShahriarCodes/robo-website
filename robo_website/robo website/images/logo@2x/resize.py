from PIL import Image  
import os
import os.path
# Opens a image in RGB mode  
im = Image.open(r"C:\Users\ADMIN\Desktop\robo website\robo website\images\logo@2x\headerlogo@2x.png")  
  
# Size of the image in pixels (size of orginal image)  
# (This is not mandatory)  
width, height = im.size  
  
# Setting the points for cropped image  
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
  
# Cropped image of above dimension  
# (It will not change orginal image)  
#im1 = im.crop((left, top, right, bottom)) 
newsize = (450, 120) 
im1 = im.resize(newsize) 
# Shows the image in image viewer  
im1.show()


