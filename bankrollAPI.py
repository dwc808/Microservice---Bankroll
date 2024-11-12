import json
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

#add funds to an account
def add_funds(id, amount):
    """
    Add funds to a user's account.

    :param str id: the username
    :param int amount: the amount to be deposited into the account

    :return: record of completed transaction in dictionary
    """

    try:
        with open(f'finances.json', 'r') as log:

            accounts = json.load(log)
    except:
        return "ERROR: No finances file."

    try:
        account = accounts[id]

    except:
        return "ERROR: User not found"

    #get balance to record for transaction history
    balance = float(account["balance"])

    # update balance
    new_balance = round((balance + amount), 2)

    #get timestamp
    timestamp = str(datetime.today())

    #create a transaction (list of four values)
    transaction = ["Deposit", timestamp, balance, amount, new_balance]

    #update JSON balance, add transaction, and rewrite file
    account["balance"] = new_balance
    account["transactions"].append(transaction)
    accounts[id] = account

    with open('finances.json', 'w') as log:
        json.dump(accounts, log)

    return transaction

#withdraw funds from an account
def withdraw_funds(id, amount):
    """
       Withdraw funds from a user's account.

       :param str id: the username
       :param int amount: the amount to be withdrawn from the account

       :return: record of completed transaction in dictionary
    """

    try:
        with open(f'finances.json', 'r') as log:

            accounts = json.load(log)
    except:
        return "ERROR: No finances file."

    try:
        account = accounts[id]

    except:
        return "ERROR: User not found"

    # get balance to record for transaction history
    balance = float(account["balance"])

    #ensure adequate funds
    if balance < amount:
        return "ERROR: NOT ENOUGH FUNDS"

    # update balance
    new_balance = round((balance - amount), 2)

    # get timestamp
    timestamp = str(datetime.today())

    # create a transaction (list of four values)
    transaction = ["Withdrawal", timestamp, balance, amount*-1, new_balance]

    # update JSON balance, add transaction, and rewrite file
    account["balance"] = new_balance
    account["transactions"].append(transaction)
    accounts[id] = account

    with open('finances.json', 'w') as log:
        json.dump(accounts, log)

    return transaction

#view balance
def view_balance(id):
    """
           View user balance.

           :param str id: the username for the acccount

           :return: user's balance as a string
    """

    try:
        with open(f'finances.json', 'r') as log:

            accounts = json.load(log)
    except:
        return "ERROR: No finances file."

    try:
        account = accounts[id]

    except:
        return "ERROR: User not found"

    # get balance
    balance = account["balance"]

    return(balance)

#view history of all transactions
def view_transactions(id):
    """
               View a history of all of the user's transactions.

               :param str id: the username for the acccount

               :return: list with all of user's transactions, in order: type, date, previous balance, amount, balance
    """

    try:
        with open(f'finances.json', 'r') as log:

            accounts = json.load(log)
    except:
        return "ERROR: No finances file."

    try:
        account = accounts[id]

    except:
        return "ERROR: User not found"

    transactions = account["transactions"]

    return transactions


@app.route('/checkbalance', methods = ['GET'])
def balance():
    id = request.args.get('User')
    balance = view_balance(id)

    return {"balance": balance}

@app.route('/addfunds', methods = ['POST'])
def addfunds():
    id = request.json["User"]
    amount = request.json["Amount"]

    transaction = add_funds(id, amount)

    return transaction

@app.route('/withdrawfunds', methods = ['POST'])
def withdrawfunds():
    id = request.json["User"]
    amount = request.json["Amount"]

    transaction = withdraw_funds(id, amount)

    return transaction

@app.route('/viewtransactions', methods = ['GET'])
def viewtransactions():
    id = request.args.get('User')
    history = view_transactions(id)

    return history

app.run()