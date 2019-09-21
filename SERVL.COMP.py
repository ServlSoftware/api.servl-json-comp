import json
from time import localtime, strftime


def send(x, y):
    req = {
      "workplace": y, 
      "ID": x, 
      "Time": str( strftime("%Y-%m-%d %H:%M:%S", localtime())), "Accepted": "False"
    }
    jsonReq = json.dumps(req)
    print("User login :", x)
    return jsonReq


print("Please input your request: ")

print("Workplace ID: ", end='')
requestA = input()

print("Person ID: ", end='')
requestB = input()
print("------------")

print("Login Sent")
req = send(requestB, requestA)
print("Event Logged:\n-----------")
print(req)
