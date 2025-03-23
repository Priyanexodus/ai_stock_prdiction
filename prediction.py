from utilities_model import load_scaler, load_model, predict_single

# Load models and scalers
model_eth = load_model(r"F:\test\assests\models\model_eth.pt")
scaler_eth = load_scaler(r"F:\test\assests\scalers\minmax_scaler_eth.pkl")

model_amazon = load_model(r"F:\test\assests\models\model_amazon.pt")
scaler_amazon = load_scaler(r"F:\test\assests\scalers\minmax_scaler_amazon.pkl")

model_google = load_model(r"F:\test\assests\models\model_google.pt")
scaler_google = load_scaler(r"F:\test\assests\scalers\minmax_scaler_google.pkl")

model_tsla = load_model(r"F:\test\assests\models\model_tsla.pt")
scaler_tsla = load_scaler(r"F:\test\assests\scalers\minmax_scaler_tsla.pkl")

def prediction(stock_values, ticker):
    # Get user input for ticker symbol and last 7 days' stock values
    ticker = ticker
    prices = stock_values

    if len(prices) != 7:
        print("Error: You must provide exactly 7 stock values.")
        exit(1)

    # Select model/scaler based on ticker symbol
    if ticker == "ETH":
        model = model_eth
        scaler = scaler_eth
    elif ticker in ("AMZN", "AMAZON"):
        model = model_amazon
        scaler = scaler_amazon
    elif ticker in ("GOOG", "GOOGL"):
        model = model_google
        scaler = scaler_google
    elif ticker == "TSLA":
        model = model_tsla
        scaler = scaler_tsla
    else:
        print("Ticker not recognized. Please try again.")
        exit(1)

    # Use the model and scaler to predict the next day's stock price
    prediction = predict_single(model,  prices, scaler)
    return prediction