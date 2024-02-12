from Web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(infura_url)) #establish the connection

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json') #get the data from the API in json format.
latest_block_info = json.loads(req_ethgas_data.content) # convert the json formatted data to normal data.

#access various costs of transactions depending upon the speed.
print('safeLow', latest_block_info['safeLow'])
print('average', latest_block_info['average'])
print('fast', latest_block_info['fast'])
print('fastest', latest_block_info['fastest'])
print('Block number:', latest_block_info['blockNum'])

gas_price = web3.eth.gas_price
gas_price_in_ether = gas_price/10**18
print("gas_price_in_ether:", gas_price_in_ether)
gas_price_in_dollar = gas_price_in_ether*3105.35
print("gas_price_in_dollar:", gas_price_in_dollar)

Block_data = web3.eth.getBlock(19154560)
latest_transaction = Block_data['transactions'][-1].hex()
print('transaction hash data:', latest_transaction)
transaction_detail = web3.eth.get_transaction(latest_transaction)
gas_estimate = web3.eth.estimateGas({'To' : transaction_detail['To'], 'From' : transaction_detail['From']})
print("Gas used by this transaction:", gas_estimate)
print("Gas limit is:", transaction_detail['gas'])