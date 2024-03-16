# encoding:utf-8
import requests 

'''获取第一个参数request_url'''
host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=u9PfhKsAZf5jPYZN1lHQSDQQ&client_secret=lCpinlOL7YPffoIey25Kmqlob8d25DQQ'
response = requests.get(host)
if response:
    result = response.json()
access_token = result["access_token"]
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze"
request_url = request_url + "?access_token=" + access_token


'''获取第二个参数data'''
import base64
f = open('/User/img/pic.png', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}


'''获取第三个参数headers'''
headers = {'content-type': 'application/x-www-form-urlencoded'}


'''发送请求'''
response = requests.post(request_url, data=params, headers=headers)


'''获取返回结果'''
if response:
    result = response.json()


'''获取base64编码图片'''
img_str = result["image"]


'''将base64编码转换为图片'''
img_data = base64.b64decode(img_str)
with open('/User/img/dehaze.png', 'wb') as f:
    f.write(img_data)
