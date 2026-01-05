# How the Climate Prediction Model Works

This model predicts **temperature** based on climate features like rainfall, CO₂ levels, and seasonal patterns using a **Random Forest Regressor**. The pipeline is structured into **four main steps**:

## 1. Data Preprocessing

- **Loading the Data:** Reads the raw climate dataset (`climate_data.csv`) which contains daily temperature, rainfall, CO₂ levels, and optional date information.  
- **Handling Dates:** If a Date column exists, extracts **Month, Year, Season, and Day of the Week** to capture **seasonal and temporal patterns**.  
- **Missing Values & Outliers:** Missing values in Temperature, Rainfall, or CO₂ are filled using the median. Optional outlier handling ensures extreme values don’t skew the model.  

## 2. Feature Engineering

- **Extreme Event Flags:**  
  - **Heatwave:** 1 if temperature ≥ 35°C, else 0  
  - **Heavy Rain:** 1 if rainfall ≥ 50 mm, else 0  

- **Rolling Statistics:**  
  - 7-day average temperature (`Temp_7day_avg`) smooths fluctuations.  
  - 7-day cumulative rainfall (`Rain_7day_sum`) captures total rainfall trends.  

- **CO₂ Trend:** Day-to-day difference in CO₂ to capture long-term increases.  

- **Scaling / Normalization:** Temperature, Rainfall, and CO₂ features are standardized for better model performance.  

## 3. Model Training

- **Random Forest Regressor:**  
  - Builds multiple decision trees and averages their predictions.  
  - Captures **non-linear relationships** between features and temperature.  

- **Train-Test Split:**  
  - 80% training, 20% testing to ensure generalization.  

- **Feature Set:**  
  - `Rainfall_scaled`, `CO2_scaled`, `Month`, `Season`, `Temp_7day_avg`  

## 4. Model Evaluation

- **Predictions:** The model predicts temperature on the test set.  
- **Metrics:**  
  - **RMSE (Root Mean Squared Error):** Measures average prediction error.  
  - **R² Score:** Measures how well the features explain the variance in temperature.  


## 5. Outcome

- A trained Random Forest model (`rf_temperature_model.pkl`) that can **predict temperature for any day** based on processed features.  
- Can be extended to predict **rainfall** or **detect extreme events** like heatwaves or heavy rainfall.  


## Summary Pipeline (Step-by-Step)

1. **Preprocessing:** Clean raw data → handle missing values → extract date features  
2. **Feature Engineering:** Add extreme event flags, rolling averages, CO₂ trends → scale features  
3. **Modeling:** Train Random Forest using engineered features  
4. **Evaluation:** Measure RMSE & R² → analyze prediction performance  

 **Key Insight:**  
The model combines **software engineering practices (modular scripts)**, **data science techniques (EDA, feature engineering)**, and **AI/ML (Random Forest)** to deliver a **robust predictive system for climate analysis**.
