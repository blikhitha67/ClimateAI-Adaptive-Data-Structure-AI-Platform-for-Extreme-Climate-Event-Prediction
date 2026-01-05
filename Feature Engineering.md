# Feature Engineering

Feature engineering is a crucial step in this project, where raw climate data is transformed into meaningful features that improve analysis, visualization, and predictive modeling. The process involves creating new variables, transforming existing ones, and encoding temporal or seasonal patterns.

## 1. Temporal Features
- **Month, Year, Season:** Extracted from date columns to capture **seasonal trends** in temperature and rainfall.  
- **Day of the Week:** Useful to study weekly patterns in precipitation or temperature.  

## 2. Aggregated Statistics
- **Rolling Mean / Moving Average:** Computes the average temperature or rainfall over a fixed window (e.g., 7-day rolling mean) to smooth out daily fluctuations.  
- **Cumulative Sums:** Useful for analyzing total rainfall over a period.  

## 3. Extreme Event Indicators
- **Heatwave Flag:** Identifies days where temperature exceeds a threshold (e.g., 35°C).  
- **Heavy Rainfall Flag:** Identifies days with rainfall above a critical limit (e.g., 50 mm/day).  
- **Outlier Detection:** Detect extreme temperature or rainfall values using Z-score or IQR methods.  

## 4. Environmental Feature Transformation
- **CO₂ Trend:** Compute the difference or growth rate of CO₂ levels over time to capture long-term trends.  
- **Temperature-Rainfall Interaction:** Creating a combined feature to study correlation between heat and precipitation patterns.  

## 5. Normalization & Scaling
- Standardized numeric features (temperature, rainfall, wind speed, CO₂) using **Min-Max Scaling or Z-score normalization** for model consistency.  

## 6. Encoding & Binning
- **Binning Continuous Variables:** Temperature and rainfall values can be categorized into bins (e.g., low, moderate, high) for classification tasks.  
- **Categorical Encoding:** Seasons, months, or heatwave flags are encoded as numeric or one-hot features for model input.  

## 7. Feature Selection
- **Correlation Analysis:** Identify redundant features using correlation matrices to remove highly correlated variables.  
- **Importance from Models:** Use feature importance from Random Forest or other models to select features with the highest predictive power.  

## Outcome
The result of feature engineering is a **clean, structured dataset** with additional derived features that improve model performance, enhance visualization insights, and help detect extreme climate events effectively.
