import requests
import json
import configparser
from constants import CONFIG_PATH


def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['DEFAULT']['webhook_url']


def send_slack_notification(message):  # Default color set to green
    webhook_url = load_config()
    payload = {
        "attachments": [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "pretext": "Notification from Course Management System",
                "author_name": "Course Management System",
                "color": "#FF0000",
                "text": message,
                "footer": "Course Management System",
            }
        ]
    }
    payload = {'text': message}
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
