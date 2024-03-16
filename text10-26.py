import os
allImgPath = '存储照片的文件夹路径'
imglist = os.listdir(allImPath)
from aip import AipImageClassify
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipImageClassfy(APP_ID,API_KEY,SECRET_KEY)
for imgname in imglist:
    if imgname[0] == '.' or '.' not in imgname:
        continue
    path = allImgPath + "/" + imgname
    with open(path,"rb") as file:
        image = file.read()
    ending = client.advancedGeneral(image)
    if "result" in ending:
        value = ending["result"][0].get("root","未分类-未分类")
        label = value.split("-")[0]
        targetPath = allImgPath + "/" + label
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        import shtil
        newPath = shutil.move(path,targetPath)
        print(f"已移动至：{newPath}")
