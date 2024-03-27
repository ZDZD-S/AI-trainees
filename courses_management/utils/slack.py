import requests
import json
import configparser
from .constants import CONFIG_PATH, DATE

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['slack']['webhook_url']

def send_slack_notification(message, color="#FF0000"):  
    webhook_url = load_config()
    payload = {
        "attachments": [
            {
                "pretext": "Notification from Course Management System",
                "author_name": "Course Management System",
                "color": color,
                "text": message,
                "footer": f"| {DATE}",
            }
        ]
    }
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    