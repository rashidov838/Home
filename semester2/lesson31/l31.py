from PIL import Image, ImageFilter

# import Image
# import PIL
# import PIL.Image


with Image.open("lesson31\green.jpg") as img:
    img.load()    

print(img)
 

print(img.size)
print(img.mode)

print(dir(img))


filtered_img=img.filter(ImageFilter.SMOOTH)
# filtered_img.save("blur_pic.png",'png')

# filtered_img=img.convert('L') #greyscale
# filtered_img.save("blur_pic.png",'png')
# filtered_img.show()


# rotated=filtered_img.rotate(90)
# rotated.save('ratated.png','png')
# rotated.show()



# transposed=img.transpose(Image.TRANSVERSE)
# transposed.show()







# array = [ {"id":"1"}, {"id":"1"},{"id":"2"}]
# data={}
# for i in array:
#     data_2={}
#     data_2['id']=i['id']
#     data[i['id']]=[data_2]
# print(data)
