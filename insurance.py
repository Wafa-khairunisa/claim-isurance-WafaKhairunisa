import pickle
import streamlit as st

# membaca model
insurance2_model =  pickle.load(open('insurance2_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Klaim Asuransi')

age = st.text_input('Usia')

sex = st.text_input('Jenis Kelamin')

bmi = st.text_input('Masukkan Hasil Indeks Massa Tubuh')

children = st.text_input('Masukkan Jumlah Anak ')

smoker = st.text_input('Merokok atau tidak')

region = st.text_input('Agama')

charges = st.text_input('Biaya Asuransi')

insuranceclaim = st.text_input('Klaim atau Tidak')

# code untuk kelompok nasabah
insurance2_claim = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    ins_prediction = insurance2_model.predict([[age, sex, bmi, children, smoker, region, charges, insuranceclaim]])
    
    if(ins_prediction[0] == 1):
        insurance2_claim = 'Nasabah Mengklaim Asuransi'
    else :
        insurance2_claim = 'Nasabah Tidak Mengklaim Asuransi'

    st.success(insurance2_claim)
