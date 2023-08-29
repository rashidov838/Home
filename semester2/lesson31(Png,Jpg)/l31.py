from PIL import Image
import os,sys
# import Image
# import PIL
# import PIL.Image
import pathlib
class InvalidFileNameError(Exception):
    def __str__(self):
        return 'Было написано не существующее имя файла'

def image_convert(image_folder,output_folder):
    direc=os.getcwd()+'\\' + output_folder + '\\'

    if not os.path.exists(direc):
        os.mkdir(direc)

    # print(pathlib.Path(__file__).parent.absolute())

    if not os.path.isdir(image_folder):  # проверка директории 
        raise InvalidFileNameError()



    for infile in os.listdir(image_folder):
        # print(infile)
        # output_file=infile.split('.')[0]+'.jpg'
        # with Image.open(f'{image_folder}/{infile}') as img:
        #     rbg_img=img.convert("RGB")
        #     rbg_img.save(f"{output_folder}/{output_file}",'jpg')


        output_file=infile.split('.')[0]+'.png'
        try:
            with Image.open(f'{image_folder}/{infile}') as img:
                img.save(f"{output_folder}/{output_file}")
        except (OSError,FileNotFoundError) as err:
            print(err)
try:
    image_folder=sys.argv[1]
    output_folder=sys.argv[2]
    image_convert(image_folder,output_folder)
except IndexError as err:
    print(f'передайте значение файлов для ввода и вывода: {err}')
    
    


# filtered_img.save("blur_pic.png",'png')

# filtered_img=img.convert('L') #greyscale
# filtered_img.save("blur_pic.png",'png')
# filtered_img.show()


# rotated=filtered_img.rotate(90)
# rotated.save('ratated.png','png')
# rotated.show()



# transposed=img.transpose(Image.TRANSVERSE)
# transposed.show()







array = [ {"id":"1"}, {"id":"1"},{"id":"2"}]
data={}
for i in array:
    data_2={}
    data_2['id']=i['id']
    data[i['id']]=[data_2]
print(data)