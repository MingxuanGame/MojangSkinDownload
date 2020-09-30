#coding:utf-8
import os
import random
ran = random.randint(1,4)
if ran == 1:
    print('  __  __   _____  _____  ')
    print(' |  \/  | / ____ |  __ \ ')
    print(' | \  / |  (___  | |  | |')
    print(' | |\/| | \___ \ | |  | |')
    print(' | |  | | ____)  | |__| |')
    print(' |_|  |_| _____/ |_____/ ')
elif ran == 2:
    print('    __  ________ ____ ')
    print('   /  |/  / ___// __ \\')
    print('  / /|_/ /\__ \/ / / /')
    print(' / /  / /___/ / /_/ / ')
    print('/_/  /_//____/_____/  ')
elif ran == 3:
    print(' __    __     ______     _____    ')
    print('/\ "-./  \   /\  ___\   /\  __-.  ')
    print('\ \ \-./\ \  \ \___  \  \ \ \/\ \ ')
    print(' \ \_\ \ \_\  \/\_____\  \ \____- ')
    print('  \/_/  \/_/   \/_____/   \/____/ ')
elif ran == 4:
    print(' _____ ______   ________  ________     ')
    print('|\   _ \  _   \|\   ____\|\   ___ \    ')
    print('\ \  \\\\\__\ \  \ \  \___|\ \  \_|\ \   ')
    print(' \ \  \\\\|__| \  \ \_____  \ \  \ \\\\ \  ')
    print('  \ \  \    \ \  \|____|\  \ \  \_\\\\ \ ')
    print('   \ \__\    \ \__\____\_\  \ \_______\\ ')
    print('    \|__|     \|__|\_________\|_______|')
    print('                  \|_________|         ')
print('==========================================')
print('          MojangSkinDownload')
print('        Current version：MSD1.2')
print('You can download the latest version and ')
print('view the latest news in GitHub and Gitee')
print('==========================================')

name = input('Enter Minecraft user name:')
url1 = 'https://api.mojang.com/users/profiles/minecraft/' + name    #Mojang API（UUID）
from urllib import request
with request.urlopen(url1) as file:
    uuiddata = file.read()
uuiddata = str(uuiddata)     


jsu = len(name)
print('Got player UUID, getting skin Base64')
uuiddata = uuiddata[jsu + 19:-3]      
url2 = 'https://sessionserver.mojang.com/session/minecraft/profile/' + uuiddata  
with request.urlopen(url2) as file:
    skindata = file.read()
skindata = skindata[jsu+123:-9]


print('Skin Base64 obtained, decoding')
import base64
skin = base64.b64decode(skindata).decode()     
skintf = skin[299+jsu:-20]
if skintf != 'slim"':           
    skin = skin[154+jsu:-13]
else:
    skin = skin[154+jsu:-68]
    #print(skin)



print("The download address of player skin has been obtained")
import zipfile
filename = input('Input the name of the skin file to save, support Chinese:')
if filename == type(int):
    filename = str(filename)
else:
    pass  
from urllib.request import urlretrieve
urlretrieve(skin,filename + '.png')
resacce = input("If the download is successful, press any key + Enter key to close, and enter res + enter to generate the resource package")


import zipfile
copyzip = os.getcwd()
if resacce == 'res':
    zipname = input('Enter resource package save Name:')
    def zip():
        startdir = "C:\\msdres"
        file_news = zipname + '.zip' 
        z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir,'')
            fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
        print ('Compression successful')
        z.write('pack.mcmeta','pack.mcmeta', zipfile.ZIP_DEFLATED)
        z.close()
    print('Building resource bundle')
    os.makedirs('C:\\msdres\\assets\\minecraft\\textures\\entity')
    if skintf != 'slim"':           
        resmd2 = 'C:\\msdres\\assets\\minecr~1\\textures\\entity\\steve.png'
    else:
        resmd2 = 'C:\\msdres\\assets\\minecr~1\\textures\\entity\\alex.png'
    os.system('copy %s %s /Y' % (filename + '.png',resmd2))
    with open("pack.mcmeta","w") as f:
        f.write("{\n")
    with open("pack.mcmeta","a") as f:
        f.write('  "pack": {\n    "pack_format": 5,\n    "description": "\\u00A7r\\u76ae\\u80a4\\u8d44\\u6e90\\u5305\\u00A7r,§eBy MojangSkinDownload"\n  }\n}')
    zip()
    os.system('rd /s /q C:\\msdres')
    os.system('del /F /S /Q pack.mcmeta')
    print('Resource package generation completed, file name:' + zipname + '.zip')
    os.system('pause')
else:
    exit()
