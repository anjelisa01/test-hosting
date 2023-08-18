import streamlit as st
import pandas as pd
import mysql.connector
def getDataSendiri1():
    mycursor.execute('SELECT tb_jenis_var.nama_var ,tb_dataset.bln_tahun,tb_dataset.nilai,tb_dataset.id_admin FROM tb_dataset INNER JOIN tb_jenis_var ON tb_dataset.id_jenis_var=tb_jenis_var.id_jenis_var where tb_dataset.id_jenis_var=1;')
    data = mycursor.fetchall()
    return data

database_connection = mysql.connector.connect(
   host="boon1y6eurxayeoke2kx-mysql.services.clever-cloud.com",
   port=3306,
   user="uco7itezylzntgza",
   password="gXwKqKx1Se7dUValN3Rs",
   database="boon1y6eurxayeoke2kx"
)
mycursor=database_connection.cursor()

st.title("Test hosting")
dataInflasi=getDataSendiri1()
datInflasiDF=pd.DataFrame(dataInflasi,columns=["Nama Variabel","Bulan & Tahun","Nilai Variabel","Id Admin"])
st.dataframe(datInflasiDF)