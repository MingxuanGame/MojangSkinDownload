#coding:utf-8
import os
os.system('rd /s /q C:\\msdres')
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
print('          当前版本：MSD1.2.1')
print('你可以在Github和码云下载最新版本以及查看')
print('                最新动态')
print('==========================================')
#获取玩家UUID
name = input('输入Minecraft用户名:')
url1 = 'https://api.mojang.com/users/profiles/minecraft/' + name    #Mojang API（UUID）
from urllib import request
with request.urlopen(url1) as file:
    uuiddata = file.read()
uuiddata = str(uuiddata)     #Byte转String

#计算Base64
jsu = len(name)
print('已经获取玩家UUID，正在获取皮肤Base64')
uuiddata = uuiddata[jsu + 19:-3]      #UUID获取
url2 = 'https://sessionserver.mojang.com/session/minecraft/profile/' + uuiddata   #计算Base64
with request.urlopen(url2) as file:
    skindata = file.read()
skindata = skindata[jsu+123:-9]

#解码Base64
print('已经获取皮肤Base64，正在解码')
import base64
skin = base64.b64decode(skindata).decode()      #解码
skintf = skin[299+jsu:-20]
if skintf != 'slim"':           #判断纤细皮肤
    skin = skin[154+jsu:-13]
else:
    skin = skin[154+jsu:-68]
    #print(skin)

#下载文件

print("已经获取玩家皮肤下载地址")
import zipfile
import tkinter
from tkinter import filedialog
gaann = tkinter.Tk()
gaann.withdraw()
filename = tkinter.filedialog.asksaveasfilename(title =u'保存文件',filetypes=[( "PNG图片", ".png")])
from urllib.request import urlretrieve
urlretrieve(skin,filename + '.png')
resacce = input("下载成功，按任意键＋回车键关闭,输入res＋回车生成资源包：")

#资源包生成
import zipfile
import tkinter
copyzip = os.getcwd()
if resacce == 'res':
    zipname = tkinter.filedialog.asksaveasfilename(title= u'保存文件', filetypes=[( "ZIP压缩包", ".zip")])
    def zip():
        startdir = "C:\\msdres"
        file_news = zipname + '.zip' 
        z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir,'')
            fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
        print ('压缩成功')
        z.write('pack.mcmeta','pack.mcmeta', zipfile.ZIP_DEFLATED)
        z.close()  
    print('正在生成资源包中')
    os.makedirs('C:\\msdres\\assets\\minecraft\\textures\\entity')
    zhanwei = open('C:\\msdres\\assets\\minecraft\\textures\\entity\\steve.png','w')
    zhanwei.close()
    zhanwei2 = open('C:\\msdres\\assets\\minecraft\\textures\\entity\\alex.png','w')  
    zhanwei2.close()  
    import shutil
    resmd2 = 'C:/msdres/assets/minecraft/textures/entity/steve.png'
    resmd4 = 'C:/msdres/assets/minecraft/textures/entity/alex.png'
    shutil.copy(filename + '.png', resmd2)
    shutil.copy(filename + '.png', resmd4)    
    with open("pack.mcmeta","w") as f:
        f.write("{\n")
    with open("pack.mcmeta","a") as f:
        f.write('  "pack": {\n    "pack_format": 5,\n    "description": "\\u00A7r\\u76ae\\u80a4\\u8d44\\u6e90\\u5305\\u00A7r,§eBy MojangSkinDownload"\n  }\n}')
    zip()
    os.system('rd /s /q C:\\msdres')
    os.system('del /F /S /Q pack.mcmeta')
    print('生成资源包完成')
    os.system('pause')
else:
    exit()