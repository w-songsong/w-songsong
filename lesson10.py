# 1.读取所有文件
import os
imgroot = '文件夹路径' 
imglist = os.listdir(imgroot)

from aip import AipImageClassify
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

for imgname in imglist:
    if imgname[0] == '.' or '.' not in imgname:
        continue
    filePath = imgroot + '/' + imgname
    with open(filePath, 'rb') as f:
        image = f.read()
    
    # 2.调用通用物体识别
    ending = client.advancedGeneral(image)
    
    # 3.提取分类结果
    if "result" in ending: 
        value = ending['result'][0].get('root', '未分类')
        label=value.split("-")[0]
        targetPath = imgroot + '/' + label
    
        # 4.对应分类文件夹还未创建时，创建文件夹   
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        
        # 5.移动图像到对应文件夹
        import shutil
        newPath = shutil.move(filePath, targetPath)
        print(f"已经移动到：{newPath}")
