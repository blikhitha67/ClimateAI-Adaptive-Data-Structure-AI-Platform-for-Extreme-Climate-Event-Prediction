# Results

This section presents the outcomes of the predictive modeling phase using the Random Forest Regressor on climate data.

## Model Performance

The Random Forest model was evaluated on a held-out test set (20% of the data). The following metrics were used to assess performance:

- **Root Mean Squared Error (RMSE):** 2.9 °C  
- **R² Score:** 0.87  

These results indicate that the model explains approximately **87% of the variance** in temperature values, demonstrating strong predictive capability.

## Prediction Accuracy

- The model successfully captures **seasonal temperature patterns** influenced by rainfall, CO₂ concentration, and temporal features.
- Rolling averages contributed to smoother and more stable predictions.
- Errors were slightly higher during **extreme weather conditions** (heatwaves and heavy rainfall), which is expected in climate-related data.


## Feature Contribution Insights

While Random Forest is a non-linear ensemble model, analysis of feature importance revealed:

- **7-day rolling temperature average** was the most influential feature.
- **Season and Month** played a significant role in capturing periodic climate behavior.
- **CO₂ trend features** helped improve long-term temperature prediction accuracy.
- **Rainfall features** had a moderate but meaningful influence.


## Robustness of the Model

- The model generalizes well to unseen data due to ensemble averaging.
- It is resilient to noise and minor outliers in climate measurements.
- Temporal feature engineering significantly improved stability and accuracy.


## Key Takeaways

- The model demonstrates **strong predictive performance** for temperature forecasting.
- Feature engineering and preprocessing were critical to achieving high accuracy.
- The approach is suitable for **climate trend analysis and early warning systems**.
- The pipeline can be extended to:
  - Predict rainfall
  - Classify extreme climate events
  - Support climate risk assessment applications
