# 1.读取所有文件
import os
# 将存储照片的文件夹路径'AAA'赋值给变量imgroot
imgroot = 'AAA' 
imglist = os.listdir(imgroot)

from aip import AipImageClassify
# 将AppID"BBB"赋值给变量APP_ID
APP_ID = 'BBB'
# 将API Key"CCC"赋值给变量API_KEY
API_KEY = 'CCC'
# 将Secret Key"DDD"赋值给变量SECRET_KEY
SECRET_KEY = 'DDD'
# 新建一个AipImageClassify，并赋值给变量client
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
