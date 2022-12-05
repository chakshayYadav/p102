import os
import shutil

from_dir= "C:/Users/chaks/OneDrive/Desktop/python/C102/p102/folder1"
to_dir = "C:/Users/chaks/OneDrive/Desktop/python/C102/p102/folder2"

list_files= os.listdir(from_dir)
#print(list_files)

for i in list_files:
    name, extension = os.path.splitext(i)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt','.pdf','.doc']:
        path1= from_dir + '/' + i
        path2 = to_dir + '/' + "Doc_Files" 
        path3 = to_dir + '/' + "Doc_Files" + '/' + i

       # print("path1 ", path1)
       # print("path2 ", path2)
       # print("path3 ", path3)

        if os.path.exists(path2):
          print("Moving " + i + ".....")
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + i + ".....")
          shutil.move(path1, path3)
