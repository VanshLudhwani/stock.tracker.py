import yfinance as yf
import matplotlib.pyplot as plt

# Dictionary 
company_map = {
    "reliance": "RELIANCE.NS",
    "tata motors": "TATAMOTORS.NS",
    "tcs": "TCS.NS",
    "adani green": "ADANIGREEN.NS",
    "adani ports": "ADANIPORTS.NS",
    "infosys": "INFY.NS",
    "hdfc bank": "HDFCBANK.NS"
}

# User input
company = input("Enter company name: ").lower()

# Check in dictionary
if company in company_map:
    ticker = company_map[company]
    data = yf.download(ticker, period="1mo")

    # Show first 5 rows
    print("\nSample Stock Data:")
    print(data.head())

    # Plot Closing Price
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-')
    plt.title(f"Closing Price of {company.title()} (Last 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()

else:
    print(" Sorry, this company is not available in the current database.")

