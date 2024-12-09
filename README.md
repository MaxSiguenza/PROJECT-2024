Stock Analysis and Trend Detection Tool
Overview
This project is a Python tool that analyzes stock price data, detects trends, and generates buy/sell signals using Simple Moving Averages (SMA) and Exponential Moving Averages (EMA). It fetches historical stock data from Yahoo Finance, computes technical indicators, and visualizes trends.

Setup
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/Stock-Analysis-Project.git
cd Stock-Analysis-Project
Install Dependencies
Install required Python libraries:

Copy code
pip install -r requirements.txt
How to Use
Edit main.py to set your stock parameters:

python
Copy code
ticker = "AAPL"
start_date = "2022-01-01"
end_date = "2023-01-01"
sma_window = 20
ema_window = 50
Run the script:

css
Copy code
python main.py
The program will generate a chart with SMA, EMA, and buy/sell signals in the images/ folder.

Troubleshooting
Ensure you have an active internet connection.
Check the stock symbol if data is not found.
Install missing dependencies with:
Copy code
pip install -r requirements.txt
Contributing
To contribute, create a pull request with your changes.
