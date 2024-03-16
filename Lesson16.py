# 1. 读取图像文件
# 将照片路径'照片路径'赋值给变量filePath
filePath = '照片路径.png' 
with open(filePath, 'rb') as f:
    image = f.read()
    
# 2. 接入百度智云文字识别服务
from aip import AipOcr
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 3. 调用通用文字识别
# 如果有可选参数 
options = {"detect_direction":"true"}
result = client.basicAccurate(image, options)

# 4. 提取返回结果
ending = result['words_result']
for word in ending:
    text = word['words']

    # 5. 写入文件
    with open("test.txt","a") as fp:
        fp.write(text+ '\n')     
print("写入完成")
