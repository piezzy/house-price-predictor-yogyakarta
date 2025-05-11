import streamlit as st
import joblib

linear_model = joblib.load('linear_model.pkl')
tree_model = joblib.load('tree_model.pkl')
gboost_model = joblib.load('gboost_model.pkl')
forest_model = joblib.load('forest_model.pkl')

models = {
    'Linear Regression': linear_model,
    'Decision Tree': tree_model,
    'Gradient Boosting': gboost_model,
    'Random Forest': forest_model,
}

def predict_price(model_name, building_area):
    if model_name not in models:
        st.error(f"Model '{model_name}' tidak ditemukan. Pilih dari: {list(models.keys())}")
        return None

    model = models[model_name]
    input_area = float(building_area)
    prediction = model.predict([[input_area]])

    return prediction[0]

def compare_models(building_area):
    predictions = {}
    for name in models:
        pred = predict_price(name, building_area)
        predictions[name] = pred

    st.bar_chart(predictions)
    
st.title('Prediksi Harga Rumah berdasarkan Luas Bangunan')

building_area = st.number_input('Masukkan Luas Bangunan (m²):', min_value=1, step=1)
model_choice = st.selectbox('Pilih Model:', ['Linear Regression', 'Decision Tree', 'Gradient Boosting', 'Random Forest'])

if st.button('Prediksi Harga'):
    if building_area > 0:
        pred = predict_price(model_choice, building_area)
        if pred:
            st.success(f"Perkiraan harga rumah dengan luas {building_area} m² menggunakan model {model_choice}: Rp {pred:,.0f}")
    else:
        st.error('Masukkan luas bangunan yang valid.')

if st.button('Perbandingan Semua Model'):
    if building_area > 0:
        st.subheader(f'Perbandingan Prediksi Harga untuk {building_area} m²')
        compare_models(building_area)
