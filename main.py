
def createWallet():
    from eth_account import Account                 ## Python 3.10
    import secrets
    priv = secrets.token_hex(32)                    ## Python 3.10
    private_key = "0x" + priv
    print('eth private key: ', private_key)
    accct = Account.from_key(private_key)       ## Generate Ethereum wallet/address
    print("Address:", accct.address)


def transferFunds():
    from web3 import Web3  ## Python 3.9
    import os
    w3 = Web3(Web3.HTTPProvider                     ## Python 3.9
    ('https://mainnet.infura.io/v3/...'))

    print(w3.isConnected())

    from_address = '0x'
    receive_address = ''
    private_key = os.getenv('PRIVATE_KEY')

    address1 = Web3.toChecksumAddress(from_address)
    address2 = Web3.toChecksumAddress(receive_address)

    nonce = w3.eth.getTransactionCount(address)

    tx = {
        'nonce': nonce,
        'to': address2,
        'value': w3.toWei(.001, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei(40, 'gwei')
    }

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.SendRawTransaction(signed_tx.rawTransaction)

