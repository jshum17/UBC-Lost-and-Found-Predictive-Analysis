import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def preprocess_data_for_forecast(raw_data, scaler, day_encoder, weekend_encoder, sequence_length=7):
    # raw_data: DataFrame with 'Date' index and 'Count' column
    if len(raw_data) < sequence_length:
        raise ValueError(f"Input data must have at least {sequence_length} days.")
    
    last_data = raw_data.tail(sequence_length)
    scaled_counts = scaler.transform(last_data['Count'].values.reshape(-1, 1))
    df_scaled = pd.DataFrame(scaled_counts, index=last_data.index, columns=['Count'])

    df_scaled['Day of Week'] = df_scaled.index.dayofweek
    df_scaled['Weekend'] = df_scaled.index.weekday >= 5
    day_encoded = day_encoder.transform(df_scaled[['Day of Week']])
    weekend_encoded = weekend_encoder.transform(df_scaled[['Weekend']])
    
    day_columns = [f"day_{i}" for i in range(day_encoded.shape[1])]
    df_scaled[day_columns] = day_encoded
    df_scaled['Weekend'] = weekend_encoded
    df_scaled.drop(columns=['Day of Week'], inplace=True)

    return torch.tensor(df_scaled.values, dtype=torch.float32).unsqueeze(0)