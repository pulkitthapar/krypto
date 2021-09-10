from django.db import models

#all_tokens = ['bitcoin', 'ethereum', 'cardano', 'tether', 'binancecoin', 'solana', 'ripple', 'dogecoin', 'polkadot', 'usd-coin', 'terra-luna', 'chainlink', 'binance-usd', 'bitcoin-cash', 'litecoin', 'uniswap', 'algorand', 'avalanche-2', 'wrapped-bitcoin', 'internet-computer', 'matic-network', 'filecoin', 'ftx-token', 'vechain', 'stellar', 'cosmos', 'ethereum-classic', 'theta-token', 'tron', 'dai', 'compound-ether', 'compound-usd-coin', 'tezos', 'okb', 'bitcoin-cash-abc-2', 'monero', 'cdai', 'quant-network', 'iota', 'eos', 'ecash', 'crypto-com-chain', 'pancakeswap-token', 'aave', 'elrond-erd-2', 'staked-ether',
#               'the-graph', 'near', 'fantom', 'axie-infinity', 'neo', 'kusama', 'klay-token', 'shiba-inu', 'hedera-hashgraph', 'waves', 'arweave', 'leo-token', 'bitcoin-cash-sv', 'bittorrent-2', 'maker', 'amp-token', 'terrausd', 'celsius-degree-token', 'huobi-token', 'thorchain', 'compound-governance-token', 'dash', 'sushi', 'decred', 'helium', 'havven', 'huobi-btc', 'chiliz', 'harmony', 'holotoken', 'iostoken', 'theta-fuel', 'nem', 'enjincoin', 'xdce-crowd-sale', 'zcash', 'blockstack', 'zilliqa', 'true-usd', 'qtum', 'flow', 'icon', 'mdex', 'yearn-finance', 'mina-protocol', 'bitcoin-gold', 'omisego', 'basic-attention-token', 'ravencoin', 'decentraland', 'telcoin', 'audius', 'paxos-standard', 'zencash']
# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=20)
    user_email = models.EmailField(max_length=254)
    token_name=models.CharField(max_length=20)
    target=models.IntegerField()
    

    def __str__(self):
        return self.username


# class coin(form.Form):
#    widget=forms.Select(choices=all_tokens)
