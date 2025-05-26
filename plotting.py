import matplotlib.pyplot as plt

def plot_price_and_indicators(df, symbol="BTC"):
    fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)
    fig.suptitle(f'{symbol} – Price and indicators', fontsize=16)

    # Plot of price and moving average
    axs[0].plot(df.index, df['price'], label='Price', color='blue')
    if 'sma_50' in df.columns:
        axs[0].plot(df.index, df['sma_50'], label='SMA 50', color='orange')
    if 'sma_200' in df.columns:
        axs[0].plot(df.index, df['sma_200'], label='SMA 200', color='red')
    axs[0].legend()
    axs[0].set_ylabel('Price (USD)')

    # RSI
    axs[1].plot(df.index, df['rsi'], label='RSI', color='purple')
    axs[1].axhline(70, color='red', linestyle='--', label='Overbought')
    axs[1].axhline(30, color='green', linestyle='--', label='Oversold')
    axs[1].set_ylabel('RSI')
    axs[1].legend()

    # MACD
    axs[2].plot(df.index, df['macd'], label='MACD', color='black')
    axs[2].plot(df.index, df['macd_signal'], label='Signal Line', color='magenta')
    axs[2].bar(df.index, df['macd_diff'], label='MACD Histogram', color='gray')
    axs[2].legend()
    axs[2].set_ylabel('MACD')

    plt.tight_layout()
    plt.show()