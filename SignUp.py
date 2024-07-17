import streamlit as st
import pymongo
st.title("Register page")
st.text_input("Enter username",key="username")
st.text_input("Enter password",key="password")
st.text_input("Enter age",key="age")
st.text_input("Enter gender",key="gender")
st.text_input("Enter Date of Birth",key="dob")
st.text_input("Enter Email",key="email")
st.text_input("Enter Phone Number",key="phone")
mongodb=pymongo.MongoClient("mongodb://localhost:27017/")
mycol=mongodb.createCollection()
if st.button("Register"):
    mycol['username']=st.session_state.username
    mycol['password']=st.session_state.password
    mycol['Age']=st.session_state.age
    mycol['Gender']=st.session_state.gender
    mycol['Email']=st.session_state.email
    mycol['Phone Number']=st.session_state.phone
    st.success("Registered")
    st.navigation([st.Page("login_page.py")])
else:
    st.write("Not Registered")