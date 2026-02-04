import pandas as pd 
import streamlit as st
import joblib

model_random = joblib.load("model_random_tomat.joblib")

st.sidebar.title("Informasi")
st.sidebar.success("Dibuat dengan :tomato: oleh Nabil Albara")

st.set_page_config(
	page_title="Regresi Penjualan Tomat",
	page_icon=":tomato:"
)
st.title("Regresi Penjualan Tomat")
st.markdown("Aplikasi Machine Learning Regression untuk menghitung total penjualan Tomat berdasarkan fitur Harga, Hari, Cuaca, dan Promo")

Harga = st.slider("Harga", 6200, 13000, 9000) 
Hari = st.selectbox("Hari", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
Cuaca = st.selectbox("Cuaca", ["Cerah", "Berawan", "Mendung"])
Promo = st.selectbox("Promo", ["Ya", "Tidak"])

if st.button("prediksi"):
	data_baru=pd.DataFrame([[Harga, Hari, Cuaca, Promo]],
                       columns=["Harga", "Hari", "Cuaca", "Promo"])
	prediksi = model_random.predict(data_baru)[0]
	st.success(f"Model memprediksi total penjualan Tomat: **{prediksi:.0f}**")
	st.balloons()
st.divider()
st.caption("Dibuat oleh Nabil Albara")
