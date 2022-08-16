import os, json
from dotenv import load_dotenv
from theblockchainapi import SolanaAPIResource, SolanaNetwork


#using blockchain api and importing the candy machine ID used for the mint, we can retrieve the list of the nfts addresses


load_dotenv()

KeyID = os.getenv('Key_ID')
Secret = os.getenv('Secret_key')

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=KeyID,
    api_secret_key=Secret
)

candy_id = "" #candy machine ID

print(f"Retrieving all NFTs from the V2 candy machine with ID {candy_id}")

result = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=candy_id,
        network=SolanaNetwork.MAINNET_BETA
    )




minted_nfts = result['minted_nfts']
mintedList = []
print(f"Total minted NFTs: {len(minted_nfts)}")
for nft in minted_nfts:
        print(f"Minted: {nft}")
        nft_addy = nft['nft_metadata']['mint']
        print(nft_addy)
        mintedList.append(nft_addy)
        print("\n")

with open('mintList.json', 'w') as f:
    json.dump(mintedList, f)
