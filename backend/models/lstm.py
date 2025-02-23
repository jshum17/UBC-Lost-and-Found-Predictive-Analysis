import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import joblib

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, (hn, cn) = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

def load_model(model_path, input_size, hidden_size, num_layers, output_size):
    model = LSTMModel(input_size, hidden_size, num_layers, output_size)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def prepare_input(last_data, scaler, day_encoder, weekend_encoder, sequence_length=7):
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

def forecast_daily(model, last_data, scaler, day_encoder, weekend_encoder, forecast_days=7, sequence_length=7):
    model.eval()
    predictions = []
    current_seq = prepare_input(last_data.tail(sequence_length), scaler, day_encoder, weekend_encoder)
    last_date = last_data.index[-1]

    with torch.no_grad():
        for _ in range(forecast_days):
            pred = model(current_seq)
            predictions.append(pred.item())

            next_date = last_date + pd.Timedelta(days=1)
            last_date = next_date

            new_row = np.zeros((1, current_seq.shape[2]))
            new_row[0, 0] = scaler.transform([[pred.item()]])[0, 0]
            new_row[0, 1:-1] = day_encoder.transform([[next_date.dayofweek]])[0]
            new_row[0, -1] = weekend_encoder.transform([[next_date.weekday() >= 5]])[0]
            current_seq = torch.cat([current_seq[:, 1:, :], torch.tensor(new_row, dtype=torch.float32).unsqueeze(0)], dim=1)

    pred_counts = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()
    future_dates = pd.date_range(start=last_data.index[-1] + pd.Timedelta(days=1), periods=forecast_days, freq='D')
    return pd.Series(pred_counts, index=future_dates)