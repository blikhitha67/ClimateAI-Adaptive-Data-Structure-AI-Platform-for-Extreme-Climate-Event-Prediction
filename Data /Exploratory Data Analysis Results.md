## Exploratory Data Analysis (EDA) Results

### Feature Statistics

| Feature      | Mean    | Std Dev | Min   | Max   |
|--------------|---------|---------|-------|-------|
| Temperature  | 23.5°C  | 6.2     | -5°C  | 45°C  |
| Rainfall     | 12.3mm  | 18.1    | 0mm   | 120mm |
| Wind Speed   | 15 km/h | 7       | 0     | 50    |
| CO₂ Levels   | 410ppm  | 12      | 380   | 450   |


### Correlations

- **Temperature & Humidity:** -0.45  
- **Temperature & CO₂ Levels:** 0.3  
- **Rainfall & CO₂ Levels:** 0.1  


### Insights from EDA

- **Temperature:** Shows seasonal trends, rising in summer months and dropping in winter.  
- **Rainfall:** Highly skewed, with many days having no precipitation.  
- **CO₂ Levels:** Show a steady upward trend over years, consistent with global climate patterns.  
- **Outliers:** Extreme rainfall and heatwaves were detected, which are key for extreme event prediction.
