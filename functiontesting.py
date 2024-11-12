import json

def view_transactions(id):
    """
               View a history of all of the user's transactions.

               :param str id: the username for the acccount

               :return: list with all of user's transactions, in order: type, date, previous balance, amount, balance
    """

    try:
        with open(f'{id}.json', 'r') as log:

            account = json.load(log)
    except:
        return "ERROR"

    transactions = account["transactions"]

    print(transactions)

    return transactions
