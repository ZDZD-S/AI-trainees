import requests
import json
import configparser
from .constants import CONFIG_PATH

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['slack']['webhook_url']

def send_slack_notification(message):
    webhook_url = load_config()
    payload = {'text': message}
    response = requests.post(
        webhook_url,
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    


    