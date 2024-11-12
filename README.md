# Microservice - Bankroll

## Communication Pipe

bankrollAPI communicates via HTTP requests, and defaults to running on localhost:5000

It expects POST requests to be JSON, with a username and amount as follows:

```{"User": "Samplename", "Amount": 39.45}```

It expects GET requests to include a 'User' parameter with the username, as follows:

/checkbalance?User=sample

## Making requests and receiving responses

The following are examples requests that can be made to the Bankroll API. These requests were made with the Python requests library:

Adding funds to a user account:
```
payload = {"User": "sample", "Amount": 12.77}
r = requests.post("http://127.0.0.1:5000/addfunds", json=payload)
```

Withdrawing funds from a user account:
```
payload = {"User": "sample", "Amount": 35.49}
r = requests.post("http://127.0.0.1:5000/withdrawfunds", json=payload)
```

Retrieving a user's balance:
```
payload = {"User": "sample"}
r = requests.get("http://127.0.0.1:5000/checkbalance", params=payload)
```

Retrieving a user's transaction history
```
payload = {"User": "sample"}
r = requests.get("http://127.0.0.1:5000/viewtransactions", params=payload)
```

All of these requests return responses in the form of JSON. Here are the sample responses, in the same order as the above requests:
```
["Deposit","2024-11-12 17:50:51.835589",219.82,12.77,232.59]
["Withdrawal","2024-11-12 17:50:54.177990",308.88,-35.49,273.39]
{"balance":273.39}
[["2024-11-11 17:57:57.095094",1.0,340.0,341.0],["2024-11-11 17:58:13.757550",341.0,20.57,361.57],["2024-11-11 17:58:17.875927",361.57,3.57,365.14],["2024-11-11 18:06:06.178048",365.14,137,228.14],["withdrawal","2024-11-11 18:08:04.989806",228.14,-137,91.14]...]
```

## Diagram
![UML Bankroll](https://github.com/user-attachments/assets/d3b96fcd-f65d-4f57-aa98-57fc20d2a4b1)

