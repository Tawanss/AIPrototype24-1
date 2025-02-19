import requests
import json
    
url = 'http://4.241.132.99:5006/simpleAPI'
myobj = {'message_key': 'message_val',
         'msg':'hi non'}

x = requests.post(url, data = json.dumps(myobj))