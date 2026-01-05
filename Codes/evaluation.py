from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import joblib

def evaluate(y_test, y_pred):
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"Random Forest Temperature Prediction")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")

if __name__ == "__main__":
    df = pd.read_csv("Data/processed_climate_data.csv")
    model = joblib.load("src/rf_temperature_model.pkl")
    
    features = ['Rainfall_scaled', 'CO2_scaled', 'Month', 'Season', 'Temp_7day_avg']
    target = 'Temperature'
    
    split_idx = int(0.8 * len(df))
    X_test = df[features].iloc[split_idx:]
    y_test = df[target].iloc[split_idx:]
    
    y_pred = model.predict(X_test)
    evaluate(y_test, y_pred)
