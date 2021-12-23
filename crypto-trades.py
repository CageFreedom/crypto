from typing import Collection
from cryptofeed import FeedHandler
from cryptofeed.backends.mongo import CandlesMongo, TradeMongo
from cryptofeed.defines import TRADES, CANDLES
from cryptofeed.exchanges import Binance, Coinbase

def main():
    f = FeedHandler()
    f.add_feed(
        Binance(
            retries = -1,
            # candle_interval = '1h',
            channels=[TRADES],
            symbols=['BTC-USDT','ETH-USDT','SOL-USDT',],
            callbacks={
                TRADES: TradeMongo('binance', collections='trades'),
                # CANDLES: CandlesMongo('binance', collection='candles')
            }
        )
    )

    f.add_feed(
        Coinbase(
            retries = -1,
            channels=[TRADES],
            symbols=['BTC-USD','ETH-USD',],
            callbacks={
                TRADES: TradeMongo('coinbase', collections='trades'),
            }
        )
    )

    f.run()

if __name__ == '__main__':
    main()