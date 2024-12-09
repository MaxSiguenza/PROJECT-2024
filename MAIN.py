import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock analyzer class
class StockAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.signals = None

    def fetch_data(self):
        """Fetch historical stock price data."""
        print("Fetching data...")
        self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        self.data['Close'] = self.data['Close']
        print("Data fetched successfully.")

    def compute_averages(self, short_window=20, long_window=50):
        """Compute moving averages."""
        print("Calculating moving averages...")
        self.data['SMA_Short'] = self.data['Close'].rolling(window=short_window).mean()
        self.data['SMA_Long'] = self.data['Close'].rolling(window=long_window).mean()
        self.data['EMA_Short'] = self.data['Close'].ewm(span=short_window, adjust=False).mean()
        self.data['EMA_Long'] = self.data['Close'].ewm(span=long_window, adjust=False).mean()
        print("Averages calculated.")

    def generate_signals(self):
        """Generate buy/sell signals based on SMA crossovers."""
        print("Generating signals...")
        self.data['Signal'] = 0
        self.data.loc[self.data['SMA_Short'] > self.data['SMA_Long'], 'Signal'] = 1
        self.data.loc[self.data['SMA_Short'] <= self.data['SMA_Long'], 'Signal'] = -1
        self.data['Signal_Change'] = self.data['Signal'].diff()
        self.signals = self.data.loc[self.data['Signal_Change'] != 0]
        print("Signals generated.")

    def plot_data(self):
        """Visualize stock price, SMAs, and buy/sell signals."""
        print("Plotting data...")
        plt.figure(figsize=(14, 8))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.6)
        plt.plot(self.data['SMA_Short'], label='SMA Short-Term', alpha=0.8)
        plt.plot(self.data['SMA_Long'], label='SMA Long-Term', alpha=0.8)
        plt.scatter(self.signals.index, self.signals['Close'], 
                    label='Signal', color='red', alpha=1, zorder=5)
        plt.title(f'{self.ticker} Stock Price and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define stock ticker and date range
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2023-01-01"

    # Create StockAnalyzer instance
    analyzer = StockAnalyzer(ticker, start_date, end_date)

    # Run analysis
    analyzer.fetch_data()
    analyzer.compute_averages()
    analyzer.generate_signals()
    analyzer.plot_data()
