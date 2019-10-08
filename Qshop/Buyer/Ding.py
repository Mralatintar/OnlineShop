import json
import requests
import time
while True:
    for i in range(1,21):
        time.sleep(2)
        url = "https://oapi.dingtalk.com/robot/send?access_token=be4b677556aef1f1c532ead9e3b18db2e6c3401f6f268cf53e7a59271bd85f74"

        headers = {
            "Content-Type": "application/json",
            "Charset": "utf-8"
        }

        requests_data = {
            "msgtype": "text",
            "text": {
                "content": "我是胡清杰，皮皮怪！窝窝头。四个{}块钱".format(i)
            },
            "at": {
                "atMobiles": [True
                ],
                "isAtAll": False
            }
        }

        sendData = json.dumps(requests_data)

        response = requests.post(url = url,headers = headers, data = sendData)

        content = response.json()

        print(content)