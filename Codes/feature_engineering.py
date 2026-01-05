import pandas as pd
from sklearn.preprocessing import StandardScaler

def feature_engineering(df):
    # Extreme Event Flags
    df['Heatwave'] = df['Temperature'].apply(lambda x: 1 if x >= 35 else 0)
    df['HeavyRain'] = df['Rainfall'].apply(lambda x: 1 if x >= 50 else 0)

    # Rolling mean / cumulative
    df['Temp_7day_avg'] = df['Temperature'].rolling(window=7, min_periods=1).mean()
    df['Rain_7day_sum'] = df['Rainfall'].rolling(window=7, min_periods=1).sum()

    # CO2 trend
    df['CO2_diff'] = df['CO2'].diff().fillna(0)

    # Scaling
    scaler = StandardScaler()
    df[['Temperature_scaled', 'Rainfall_scaled', 'CO2_scaled']] = scaler.fit_transform(
        df[['Temperature', 'Rainfall', 'CO2']]
    )
    return df

if __name__ == "__main__":
    df = pd.read_csv("Data/cleaned_climate_data.csv")
    df = feature_engineering(df)
    df.to_csv("Data/processed_climate_data.csv", index=False)
    print("Feature engineering complete, processed data saved.")
