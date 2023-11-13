from eth_account import Account
import secrets

if __name__ == '__main__':
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print('eth private key: ', private_key)
    accct = Account.from_key(private_key) ## Generate Ethereum wallet/address
    print("Address:", accct.address)
