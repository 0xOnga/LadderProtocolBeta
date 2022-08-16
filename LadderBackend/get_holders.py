import requests, json
f = open('mintList.json')
holders = []
mints = json.load(f)

#we get list of players addresses from the nfts one

for i in mints:
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'tokenAddress': i,
        'offset' : 0,
        'limit' : 10
    }
    response = requests.get('https://public-api.solscan.io/token/holders', headers=headers, params=params)

    data = response.json()

    owner = data["data"]
    for index, value in enumerate(owner):
        print(value['owner'])
        holders.append(value['owner'])

holders = list(dict.fromkeys(holders))

with open('players.json', 'w', encoding='utf-8') as f:
    json.dump(holders, f, ensure_ascii=False, indent=4)