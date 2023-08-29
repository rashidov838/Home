from PIL import Image
import shutil
from os import path
import os
# from docx import Document

# print("Текущая директория", os.getcwd())
# os.makedirs('myfile')

# print("Текущая директория поменялась на myfile",os.getcwd())

with Image.open("lesson31\qblue.jpg") as img:
    img.load()


convert=img.save("lesson31\qblue.png",'png')





# ol_img=open("lesson31\qblue.png","r").read()
# new_img=open("new_pro.docx","a")
# new_img.write(ol_img)
# new_img.close()


# os.replace(convert,'myfile')


# img.show()

#TAsk-2
text='Hi Bekzod'
# color=(100,200,300,400)
# img=Image.new('RGB',(100,100),color)
# imgDrawer=ImageDraw.Draw(img)
# imgDrawer.text((10,20),text)
# img.save('drawpict.png')



# ---------------------------------------------------------------------------------------------------------
source_path="green.jpg"
if path.exists(source_path):
    destination=open("Files.txt","r")
    new_location=shutil.move(source_path,destination)
    print("%s перемещен в указанное место %s"%(source_path,new_location))
else:
    print("Файл не существует")


