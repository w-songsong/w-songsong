'''创建客户端'''
from aip import AipFace

# 以字符串的形式存储密钥
APP_ID = 'AAA'
API_KEY = 'BBB'
SECRET_KEY = 'CCC'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

'''转换图片格式'''
import base64

# 图片的路径
img_path = '图片的路径'

with open(img_path, "rb") as file:
    res = file.read()

    img = base64.b64encode(res)
    img = str(img, 'utf-8')
    
'''获取检测结果'''
options = {
    'max_face_num': 10,
    'face_field': 'quality,age'}


img_type = "BASE64"

ret_data = client.detect(img, img_type, options)
print(ret_data)

'''PIL 打开图片'''
from PIL import Image

with Image.open(img_path) as img:
    img_cp = img.copy()
    print(img_cp)
    
'''修改图片标记出人脸'''
from PIL import ImageDraw
draw_img = ImageDraw.Draw(img_cp)
from PIL import ImageFont

if ret_data['error_msg'] == 'SUCCESS':
    for face_msg in ret_data['result']['face_list']:
        location = face_msg['location']
        x1 = location['left']
        y1 = location['top']
        x2 = x1 + location['width']
        y2 = y1 + location['height']
        
        
        # 字体路径
        font_path = '字体路径'
        font_size = location['height']//5
        font = ImageFont.truetype(font_path, font_size)
        quality = face_msg['quality']['occlusion']
        
        if quality['nose'] > 0.5 and quality['mouth'] == 1:
            color = 'lightgreen'
            text = '已佩戴口罩'
        else:
            color = 'red'
            text = '未佩戴口罩'

        draw_img.rectangle([x1, y1, x2, y2], outline=color, width=2)
        draw_img.rectangle([x1, y2, x2, y2 + font_size*2], fill=color)
        draw_img.text([x1, y2], text, 'white', font)
        
    img_cp.save('/User/img/draw.png')
else:
    print('识别失败')
