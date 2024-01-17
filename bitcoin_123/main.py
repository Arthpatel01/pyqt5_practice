from bitcoinlib.wallets import Wallet


def generate_bitcoin_wallet():
    wallet = Wallet.create("jack_black_patel")
    data = f"Wallet Name: {wallet.name}\nAddress: {wallet.get_key().address}\nPrivate Key: {wallet.get_key().wif}"

    if wallet:
        with open("temp.txt", "w") as file:
            file.write(data)


if __name__ == "__main__":
    generate_bitcoin_wallet()