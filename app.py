from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Cross-Origin Resource Sharing 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    
class DeepNN(nn.Module):
    def __init__(self, input_dim=33):
        super(DeepNN, self).__init__()
        self.layer_1 = nn.Linear(input_dim, 4)
        self.layer_out = nn.Linear(4, 1)
        
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.4)
        self.sigmoid = nn.Sigmoid()

    def forward(self, inputs):
        lay_1 = self.layer_1(inputs)
        lay_1 = self.relu(lay_1)
        lay_1 = self.dropout(lay_1)
        
        linear_output = self.layer_out(lay_1)
        output = self.sigmoid(linear_output)
        return output
    
    
def apply_feature_engineering(df_input):
    df_out = df_input.copy()
    
    # Feature 1: Total Services Count
    service_cols = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    df_out['TotalServices'] = (df_out[service_cols] == 'Yes').sum(axis=1)
    
    # Feature 2: Automatic Payment Indicator
    auto_payments = ['Bank transfer (automatic)', 'Credit card (automatic)']
    df_out['IsAutomaticPayment'] = df_out['PaymentMethod'].isin(auto_payments).astype(int)
    
    # Feature 3: Monthly Spend Difference (Current vs Historical Avg)
    # Using tenure + 1 to safely prevent division by zero for tenure = 0
    historical_avg = df_out['TotalCharges'] / (df_out['tenure'] + 1)
    df_out['MonthlySpendDiff'] = df_out['MonthlyCharges'] - historical_avg
    
    return df_out

preprocessor = joblib.load(os.path.join(BASE_DIR, 'models', 'preprocessor_pipeline.pkl'))

model = DeepNN()
state_dict = torch.load(os.path.join(BASE_DIR, 'models', 'churn_nn_weights.pth'),
                        map_location=torch.device('cpu'), weights_only=True)

model.load_state_dict(state_dict)
model.eval()


@app.route('/health', methods=['GET'])  # route an incoming URL path to the specific Python function that should be executed
def health():
    return {'status': 'healthy (PyTorch)'}

@app.route('/', methods=['GET'])
def home():
    return render_template('UI.html')
    
    
@app.route('/predict', methods=['POST']) # 21 features .. return one of the two classes 
def predict():
    try:
        data = request.json
        features_data = data['features']
        
        if isinstance(features_data, dict):
            input_df = pd.DataFrame([features_data])
        else:
            input_df = pd.DataFrame(features_data)
            
        engineered_df = apply_feature_engineering(input_df)
        processed_features = preprocessor.transform(engineered_df)
        features_tensor = torch.tensor(processed_features, dtype=torch.float32)

        with torch.no_grad():
            prob = model(features_tensor).item() 
            prediction = 1 if prob >= 0.5 else 0  

        return jsonify({
            'prediction': prediction,
            'churn_probability': prob
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

# in another terminal you can run..
# curl http://localhost:8080/health
# curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d "{\"features\": [1.1, 13.5, 1.4, 4.2]}"