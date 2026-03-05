from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model, scaler, and column names
model = pickle.load(open('svm_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        
        # 1. FIX COLUMN MISMATCH & GET THE 140 VALID COLUMNS
        # We strip out the empty '_c39' column so the list exactly matches the scaler
        valid_columns = [col for col in model_columns if col != '_c39']
        
        # 2. Initialize with the scaler's mean (average) values!
        # Instead of 0s, we fill missing data with the exact training averages.
        # This prevents the SVM from penalizing empty fields as extreme outliers.
        input_df = pd.DataFrame([scaler.mean_], columns=valid_columns)
        
        # 3. Fill Numerical values from the web form
        numerical_fields = [
            'months_as_customer', 
            'policy_deductable', 
            'total_claim_amount', 
            'umbrella_limit', 
            'number_of_vehicles_involved'
        ]
        
        for field in numerical_fields:
            if field in data and field in input_df.columns:
                val = data[field].strip()
                if val: 
                    input_df.at[0, field] = float(val)

        # 4. Fill Categorical values from the web form
        if 'incident_severity' in data:
            # First, zero out ALL severity columns to erase the "averages"
            for col in input_df.columns:
                if col.startswith("incident_severity_"):
                    input_df.at[0, col] = 0
            
            # Now, set the one selected by the user to 1
            sev_col = "incident_severity_" + data['incident_severity']
            if sev_col in input_df.columns:
                input_df.at[0, sev_col] = 1
                
        # 5. Scale and Predict 
        # (The missing values will perfectly scale to 0.0, which is the exact center of the distribution)
        scaled_data = scaler.transform(input_df.values)
        prediction = model.predict(scaled_data)
        
        if prediction[0] == 1:
            result = "Fraudulent Claim Detected!" 
        else:
            result = "Claim appears to be Genuine."
            
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)