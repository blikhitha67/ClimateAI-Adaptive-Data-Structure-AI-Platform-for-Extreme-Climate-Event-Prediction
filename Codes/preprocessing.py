import pandas as pd

def load_data(file_path="Data/climate_data.csv"):
    df = pd.read_csv(file_path)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['Season'] = df['Month'] % 12 // 3 + 1
        df['DayOfWeek'] = df['Date'].dt.dayofweek
    return df

def handle_missing_outliers(df):
    # Example: Fill missing values with median
    for col in ['Temperature', 'Rainfall', 'CO2']:
        df[col].fillna(df[col].median(), inplace=True)
    # Optional: Add outlier handling here
    return df

if __name__ == "__main__":
    df = load_data()
    df = handle_missing_outliers(df)
    df.to_csv("Data/cleaned_climate_data.csv", index=False)
    print("Preprocessing complete, cleaned data saved.")
