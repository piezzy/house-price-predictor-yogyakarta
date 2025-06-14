# House Price Predictor Yogyakarta 🏠

A simple Streamlit app to predict house prices in Yogyakarta based on building area using multiple machine learning models.

## 🔍 Features
- Predict house price based on building area
- Compare predictions from 4 models: Linear Regression, Decision Tree, Gradient Boosting, and Random Forest
- Interactive UI with Streamlit

## 📦 Requirements
- Python 3.8+
- Streamlit
- scikit-learn
- joblib
- numpy

Install the dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
Clone the repository:
```bash
git clone https://github.com/your-username/house-price-predictor-yogyakarta.git
cd house-price-predictor-yogyakarta
streamlit run app.py
```

## 📁 Files
- `app.py` : Main Streamlit application
- `linear_model.pkl`, `tree_model.pkl`, `gboost_model.pkl`, `forest_model.pkl` : Trained ML models
- `yogyakarta_price_prediction.ipynb` : Jupyter notebook for training and evaluating machine learning models for house price prediction in Yogyakarta