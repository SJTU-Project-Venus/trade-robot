import requests
import socket
import json
import time
import _thread
import threading
import random

apiPathA = "http://202.120.40.8:30383/A/"
apiPathB = "http://202.120.40.8:30383/B/"
apiPathN = "http://202.120.40.8:30382/one/"
apiPathM = "http://202.120.40.8:30382/two/"

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
        self.LimitOrder()
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
        futureName="OIL-SEP22"
        # side
        side = ""
        unitPrice = 0
        if(random.random()<0.3):
            side="BUY"
            unitPrice = random.randint(18,28)*10
        else:
            side = "SELL"
            unitPrice = random.randint(24,34)*10
       # number     
        number = random.randint(1, 6)*100
        #unitPrice
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
        res = requests.post(self.apiPath+"order/create",headers = headers,data=json.dumps(data),params={"access_token": self.access_token})
        print(res)
    def StopOrder(self):
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
        futureNames = ['OIL-SEP22','OIL-MAR01','GOLD-JUN18','GOLD-FEB22','GOLD-SEP13']
        for each in member:
            data = {
                "name":each
            }
            requests.post(apiPathM+"/addFuture",headers = headers,data=json.dumps(data))
        for each in member:
            data = {
                "name":each
            }
            requests.post(apiPathN+"/addFuture",headers = headers,data=json.dumps(data))
    def start(self):
        self.initFutureName()
        account1 = TradingRobot("123","123","A")
        account2 = TradingRobot("wzy","123","B")
        account1.login()
        account2.login()
        for num in range(0,60):
            time.sleep(2)
            if(random.random()<0.5):
                account1.postOrder()
            else:
                account2.postOrder()
def main():
    robot = Robot()
    robot.start()
main()