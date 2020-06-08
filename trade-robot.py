import requests
import pandas as pd
import socket
import json
import time
import _thread
import threading
import random

apiPath = "http://localhost:8080/"

class TradingRobot:
    username = "123"
    password = "123"
    access_token = ""
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        params={"username":self.username,
                "password":self.password,
                "grant_type":"password",
                "scope":"select",
                "client_id":"client_2",
                "client_secret":"123456"
        }
        res = requests.get(apiPath+"oauth/token",params=params)
        self.access_token = res.json()['access_token']
        print("access_token Result:\n", self.access_token)
    def testGet(self):
        res = requests.get(apiPath+"order/1",params={"access_token": self.access_token})
        print("result1:",res.text)
       
    def testPost(self):
        data = {"TestString":"123"}
        headers = {
            'Content-Type':'application/json'
        }
        res = requests.post(apiPath+"order/postTest",headers = headers,data=json.dumps(data),params={"access_token": self.access_token})
        print("result2:",res.text)
    def start(self):
        thread0 = threading.Thread(target=self.testGet,args=())
        thread1 = threading.Thread(target=self.testPost,args=())
        thread0.start()
        time.sleep(10)
        thread1.start()
def main():
    account = TradingRobot("123","123")
    account.login()
    account.start()
main()
