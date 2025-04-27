import PIL.Image

# создаем список из ASCII символов, которые будут использоваться при рисовании картинки
asciiCharacters = ["@", "!", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


# создаем функцию которая изменияет размер изображения до нового в соответствии с шириной, которую мы ей укажем
def resizeImage(image, newWidth = 100):
    width, height = image.size # создаем кортеж из ширины и высоты
    ratio = height / width # находим отношение высоты и ширины
    newHeight = int(newWidth * ratio)
    resizedImage = image.resize((newWidth, newHeight))
    return(resizedImage)

# создаем функцию, которая делает изображение черно-белым чтобы его можно было преобразовать в ASCII код
def graify(image):
    grayscaleImage = image.convert("L")
    return(grayscaleImage)

# и наконец создаем функцию которая превращает нашу картинку в строку из ASCII символов
def convertToASCII(image):
    pixels = image.getdata()
    chars = "".join([asciiCharacters[pixel//25] for pixel in pixels]) # создаем массив из символов из которых получается картинка
    return(chars)

def main(newWidth=100): # это главная функция которая как раз и создает ASCII картинку из растровой
    path = input("Введите корректный путь к изображению: \n")
    try:# используем конструкцию try-except чтобы в случае когда мы задали неверный путь к картинке
        image = PIL.Image.open(path)
    except:
        print('Некорректный путь к файлу. Попробуйте снова')
        
    resizedImage = resizeImage(image, newWidth=newWidth)
    graifiedImage = graify(resizedImage)
    newImageData = convertToASCII(graifiedImage)

    pixelCount = len(newImageData)
    asciiImage = "\n".join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))
    print("Вуаля! \n \n{}".format(asciiImage))
    if input("Сохранить? [y/n]: ") == "y":
        fileName = input("Введите название файла: ")
        with open("{}.txt".format(fileName), "w") as file:
            file.write("Made by 'Mr. Paw' \n \n {}".format(asciiImage))
            print("Сохранено")

  
main(newWidth=100)

'''
Если выдает что нет модуля PIL, установите PIL либо Pillow (форк PIL) через pip
'''
