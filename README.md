# Insurance_Fraud_Detection_SEL

A machine learning-powered web application designed to help insurance companies detect potentially fraudulent claims in real-time. By inputting key incident parameters, the system utilizes a pre-trained AI model to instantly classify the claim's legitimacy.

## 🚀 Features

* **Real-time AI Analysis:** Instantly predicts whether a claim is "Genuine" or "Fraud" using a trained machine learning model.
* **Modern Web Interface:** A sleek, responsive, and professional UI designed for seamless data entry and clear result visualization.
* **Key Metrics Evaluation:** Analyzes crucial data points including policy deductibles, total claim amounts, umbrella limits, and incident severity.

## 🛠️ Tech Stack

* **Backend Framework:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Serialization:** Pickle (Python built-in)
* **Frontend:** HTML, CSS

## 📁 Project Structure

For the application to run correctly, ensure your files are organized like this:

```text
your-project-folder/
│
├── app.py                              # The main Flask web server
├── requirements.txt                    # Python library dependencies
├── insurance_claims.csv                # The original dataset
├── Insurance_Fraud_Detection.ipynb     # Model training and data exploration file
│
└── templates/                          # MUST be named exactly 'templates'
    └── index.html                      # The frontend UI

```

## ⚙️ Installation & Setup

**1. Create a Virtual Environment (Recommended)**
It's best practice to run Python projects in a virtual environment to keep dependencies clean. Open your terminal/command prompt and run:

```bash
python -m venv venv

```

Activate the environment:

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

**2. Install Dependencies**
Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt

```

**3. Run the Application**
Start the Flask development server:

```bash
python app.py

```

**4. Access the Web App**
Open your web browser and navigate to the local address provided by Flask, usually:
`http://127.0.0.1:5000`

## 📝 Usage

1. Launch the web application in your browser.
2. Fill out the form with the specific details of the insurance incident (e.g., Months as Customer, Incident Severity, etc.).
3. Click the **"Initialize AI Analysis"** button.
4. The system will process the inputs and return an immediate, color-coded assessment of the claim.
