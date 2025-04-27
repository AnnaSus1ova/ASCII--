import ascii_magic
output = ascii_magic.from_image_file(input("Enter file path: "), columns=100, char="#")
ascii_magic.to_terminal(output)

'''
нужно установить модуль ascii_magic через pip
'''
