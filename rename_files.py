# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 

# Folder where your pics are
# use '\\' or '/' for path
# don't forget to add '\\' at the end of path
src_dir = '\\'  


# extension
ext = '.jpg'

# List here the pics missing in src_dir
missing_pic = []

# Return a list of the files in src_dir
liste = os.listdir(src_dir)

# Remove extension in filenames
# Split filenames if needed
for i in range(0,len(liste)):
#    liste[i] = (liste[i].split('H'))[1]
    liste[i] = os.path.splitext(liste[i])[0]

# Sort files as int    
liste = sorted(liste,key=int)

# Add extension 
# Add full original names if needed
for i in range(0,len(liste)):
    liste[i] = liste[i] + ext
#    liste[i] = '100H' + liste[i] + '.jpg'

# liste should contain your files sorted
print(liste)
    
#Function to rename multiple files 
def main(): 
    i = 1
    
    for filename in liste: 
        while i in missing_pic:
            print(i, 'missing_pic')
            i += 1
        dst = "1_" + str(i) + ext
        src = src_dir + filename 
        dst = src_dir + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

