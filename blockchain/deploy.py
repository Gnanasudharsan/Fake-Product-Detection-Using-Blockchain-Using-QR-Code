from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Load contract details
with open('compiled_contract.json') as f:
    contract_data = json.load(f)

contract_abi = contract_data["abi"]
contract_bytecode = contract_data["bytecode"]

# Deploy contract
contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = contract.constructor().transact({'from': w3.eth.accounts[0]})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at {tx_receipt.contractAddress}")
