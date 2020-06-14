import requests
import pandas as pd
import socket
import json
import time
import _thread
import threading
import random

apiPathA = "http://localhost:8082/"
apiPathB = "http://localhost:8083/"
apiPathM = "http://localhost:8080/"
class TradingRobot:
    username = "123"
    password = "123"
    access_token = ""
    apiPath = ""
    traderCompany = ""
    def __init__(self, username, password,traderCompany):
        if(traderCompany == "A"):
            self.apiPath = apiPathA
        else:
            self.apiPath = apiPathB
        self.username = username
        self.password = password
        self.traderCompany = traderCompany
        data = {
          "password": self.password,
          "phone": self.username,
          "traderCompony": self.traderCompany
        }
        headers = {
            'Content-Type':'application/json'
        }
        res = requests.post(self.apiPath+"traderUser/register",headers = headers,data=json.dumps(data))
        
    def login(self):
        params={"username":self.username,
                "password":self.password,
                "grant_type":"password",
                "scope":"select",
                "client_id":"client_2",
                "client_secret":"123456"
        }
        res = requests.get(self.apiPath+"oauth/token",params=params)
        self.access_token = res.json()['access_token']
        print("access_token Result:\n", self.access_token)
    def postOrder(self):
        if(random.random()<0.2):
            self.LimitOrder()
        elif(random.random()>0.6):
            self.MarketOrder()
        else:
            self.StopOrder()
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
    def LimitOrder(self):
        headers = {
            'Content-Type':'application/json'
        }
        #brokerName
        brokerName=""
        if(random.random()<0.5):
            brokerName="M"
        else:
            brokerName = "N"
        futureName="GOLD"
        # side
        side = ""
        if(random.random()<0.5):
            side="BUY"
        else:
            side = "SELL"
       # number     
        number = random.randint(1, 6)*100
        #unitPrice
        unitPrice = random.randint(20,30)*10
        data={
            "brokerName": brokerName,
            "futureName": futureName,
            "id": -1,
            "number": number,
            "orderId": -1,
            "orderType": "LIMIT",
            "pendingNumber": number,
            "side": side,
            "status": "PENDING",
            "stopPrice": -1,
            "targetType": "LIMIT",
            "timestamp": 0,
            "traderCompany": self.traderCompany,
            "traderName": self.username,
            "unitPrice": unitPrice
        }
        res = requests.post(self.apiPath+"order/create",headers = headers,data=json.dumps(data),params={"access_token": self.access_token})
        print(res)
    def MarketOrder(self):
        headers = {
            'Content-Type':'application/json'
        }
        #brokerName
        brokerName=""
        if(random.random()<0.5):
            brokerName="M"
        else:
            brokerName = "N"
        futureName="GOLD"
        # side
        side = ""
        if(random.random()<0.5):
            side="BUY"
        else:
            side = "SELL"
       # number     
        number = random.randint(1, 6)*100
        #unitPrice
        unitPrice = random.randint(20,30)*10
        data={
            "brokerName": brokerName,
            "futureName": futureName,
            "id": -1,
            "number": number,
            "orderId": -1,
            "orderType": "MARKET",
            "pendingNumber": number,
            "side": side,
            "status": "PENDING",
            "stopPrice": -1,
            "targetType": "LIMIT",
            "timestamp": 0,
            "traderCompany": self.traderCompany,
            "traderName": self.username,
            "unitPrice": 0
        }
        res = requests.post(self.apiPathM+"order/create",headers = headers,data=json.dumps(data),params={"access_token": self.access_token})
        print(res)
    def StopOrder(self):
        print("Hello World!")
        headers = {
            'Content-Type':'application/json'
        }
        #brokerName
        brokerName=""
        if(random.random()<0.5):
            brokerName="M"
        else:
            brokerName = "N"
        futureName="GOLD"
        # side
        side = ""
        if(random.random()<0.5):
            side="BUY"
        else:
            side = "SELL"
       # number     
        number = random.randint(1, 6)*100
        #unitPrice
        unitPrice = random.randint(20,30)*10
        #stopPrice
        stopPrice = random.randint(20,30)*10
        #targetType
        targetType = ""
        if(random.random()<0.5):
            targetType="LIMIT"
        else:
            targetType="MARKET"
        data={
            "brokerName": brokerName,
            "futureName": futureName,
            "id": -1,
            "number": number,
            "orderId": -1,
            "orderType": "STOP",
            "pendingNumber": number,
            "side": side,
            "status": "PENDING",
            "stopPrice": stopPrice,
            "targetType": targetType,
            "timestamp": 0,
            "traderCompany": self.traderCompany,
            "traderName": self.username,
            "unitPrice": unitPrice
        }
        res = requests.post(self.apiPath+"order/create",headers = headers,data=json.dumps(data),params={"access_token": self.access_token})
        print(res)
class Robot:
    def initFutureName(self):
        data = {
            "name":"GOLD"
        }
        requests.post(self.apiPath+"/addFuture",headers = headers,data=json.dumps(data))
    def start(self):
        self.initFutureName()
        account1 = TradingRobot("123","123","A")
        #account2 = TradingRobot("wzy","123","B")
        account1.login()
        #account2.login()
        for num in range(0,120):
            time.sleep(2)
            account1.postOrder()
            #if(random.random()<0.5):
              #  account1.postOrder()
            #else:
              #  account2.postOrder()
def main():
    robot = Robot()
    robot.start()
main()