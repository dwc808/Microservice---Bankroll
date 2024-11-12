import requests

##################### requests to add funds to an account ##################################
payload = {"User": "sample", "Amount": 12.77}
r = requests.post("http://127.0.0.1:5000/addfunds", json=payload)
print(r.text)

input("Press enter to continue the test program")


payload = {"User": "sample", "Amount": 25.27}
r = requests.post("http://127.0.0.1:5000/addfunds", json=payload)
print(r.text)

input("Press enter to continue the test program")


payload = {"User": "sample", "Amount": 51.02}
r = requests.post("http://127.0.0.1:5000/addfunds", json=payload)
print(r.text)

input("Press enter to continue the test program")

##################### request to widthraw funds from an account ##################################
payload = {"User": "sample", "Amount": 35.49}
r = requests.post("http://127.0.0.1:5000/withdrawfunds", json=payload)
print(r.text)

input("Press enter to continue the test program")

##################### request to view account balance ##################################
payload = {"User": "sample"}
r = requests.get("http://127.0.0.1:5000/checkbalance", params=payload)
print(r.text)

payload = {"User": "sample2"}
r = requests.get("http://127.0.0.1:5000/checkbalance", params=payload)
print(r.text)

input("Press enter to continue the test program")

##################### request to view transaction history ##################################
payload = {"User": "sample"}
r = requests.get("http://127.0.0.1:5000/viewtransactions", params=payload)
print(r.text)

