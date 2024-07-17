import streamlit as st
import pymongo
mongodb=pymongo.MongoClient("mongodb://localhost:27017/")
st.write("Age",mongodb.mycol['Age'])
st.write("Gender",mongodb.mycol['Gender'])
st.write("Birthdate",mongodb.mycol['Birthdate'])
st.write("Email",mongodb.mycol['Email'])
st.write("Phone Number",mongodb.mycol['Phone Number'])