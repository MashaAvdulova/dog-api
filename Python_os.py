import os

# создание каталога
# os.mkdir('folder')

# проверка существования пути
if os.path.exists('folder'):
    # запись в каталог
    with open('folder/file.txt', 'w') as file:
        pass

# проверка существования файла
if os.path.exists('folder/file.txt'):
    print('ok')

if os.path.isfile('folder/file.txt'):
    print('file')
else:
    print('no file')

print(os.listdir('folder'))

# def compare_images(input_image):
#     for image in images:
#         with open(image, 'rb') as file:
#             if input_image == file:
#                 return True