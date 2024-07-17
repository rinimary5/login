import streamlit as st
import pymongo
st.title("Login page")
mongodb=pymongo.MongoClient("mongodb://localhost:27017/")
st.text_input("Username",key="user")
st.text_input("password",key="passwd")
if st.button("Login"):
    if st.session_state.user == mongodb.mycol['username'] and st.session_state.passwd == mongodb.mycol['password']:
        st.write("Login successful!")
        st.write("Age",mongodb.mycol['Age'])
        st.write("Gender",mongodb.mycol['Gender'])
        st.write("Birthdate",mongodb.mycol['Birthdate'])
        st.write("Email",mongodb.mycol['Email'])
        st.write("Phone Number",mongodb.mycol['Phone Number'])
        st.navigation([st.Page("Profile.py")])
    else:
        st.write("Entered invalid username/password")



