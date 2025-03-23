from utilities_model import load_scaler, load_model, predict_single

model_tsla = load_model(r"F:\test\assests\models\model_tsla.pt")
scaler_tsla = load_scaler(r"F:\test\assests\scalers\minmax_scaler_tsla.pkl")



prices = [700, 715, 720, 710, 725, 730, 740]
prediction = predict_single(model_tsla, prices, scaler_tsla)
print(prediction)