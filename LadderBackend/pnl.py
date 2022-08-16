import requests, json


# retrieve mango accounts from pubkey
headers = {
        'Content-Type': 'application/json',
    }
params = {
        'mango-account': "",
        'start-date' : ""
    }
response = requests.get('https://mango-transaction-log.herokuapp.com/v3/stats/account-performance-detailed', headers=headers, params=params)
