import requests, requests, json
from login import SLACK_WEBHOOK_PROD

def SendSlack(payload):

    url= SLACK_WEBHOOK_PROD
       
    headers ={
        "Content-type": "application/json"
    }
    json_message = json.dumps(payload)

    response = requests.post(url, data=json_message, headers=headers)

    if response.status_code == 200:
        print("Slack Notification sending...")
    else:
        print(f"Failed to send message. Error: {response.status_code}, {response.text}")