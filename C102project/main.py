import os
import shutil

from_dir="C:/Users/Divjot singh/OneDrive/Pictures"
to_dir="C:/Users/Divjot singh/OneDrive/Desktop/python test"
to_dir2='C:/Users/Divjot singh/OneDrive/Desktop/python test 2'

files = os.listdir(from_dir)
#print(files)
      
for file_name in files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    

    if extension == "":
        continue
    
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path_1 = from_dir + '/' + file_name
        path_2 = to_dir + '/' + "image_files"
        path_3 = to_dir + '/' + "image_files" + '/' + file_name

        print('path1',path_1)
        print('path3',path_3)

        if os.path.exists(path_2):
            print("Moving " + file_name + ".....")
             # Move from path1 ---> path3 
            shutil.move(path_1, path_3) 
        else:
            os.makedirs(path_2) 
            print("Moving " + file_name + ".....") 
            shutil.move(path_1, path_3)


