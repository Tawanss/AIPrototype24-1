# import requests
# import json
    
# url = 'http://40.81.22.119:5006/simpleAPI'
# myobj = {'message_key': 'what are you',
#          'msg':'hi non'}

# x = requests.post(url, data = json.dumps(myobj))

import requests
import json
import datetime

def get_user_input(prompt):
    return input(prompt).strip()

def send_message(ip, port, sender, message):
    url = f'http://{ip}:{port}/simpleAPI'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    payload = {
        'sender': sender,
        'message': message,
        'timestamp': timestamp
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = get_user_input("Enter IP Address: ")
    port = get_user_input("Enter Port: ")
    sender = get_user_input("Enter Your Name: ")
    message = get_user_input("Enter Your Message: ")
    
    send_message(ip, port, sender, message)
