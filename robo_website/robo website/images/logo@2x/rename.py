#from shutil import copyfile
#
#
#src="C:/Users/ADMIN/desktop/robo website/robo website/images/logo@2x/xyz/"
#dst="C:/Users/ADMIN/desktop/robo website/robo website/images/logo@2x/xyz/"
#
#copyfile(src, dst)



import os
# Function to rename multiple files
def main():
   i = 1
   path="C:/Users/ADMIN/desktop/robo website/robo website/images/logo@2x/xyz/"
   for filename in os.listdir(path):
      my_dest ="header_logo_" + str(i) + "@2x"+".png"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()