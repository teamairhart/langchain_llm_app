import langchain_helper as lch
import streamlit as st  

st.set_page_config(page_title="Pimp Name Generator", page_icon=":guardsman:", layout="centered")  
st.title("Pimp Name Generator")

first_name = st.sidebar.selectbox("What is your first name?", ["Matt", "Jonathan", "Ashley", "Tara"] , index=0)

if first_name == "Matt" or first_name == "Ashley":
    last_name = st.sidebar.selectbox("What is your last name?", ["Pettoni"], index=0)
else:
    last_name = st.sidebar.selectbox("What is your last name?", ["Airhart"], index=0)  

pimp_name = lch.generate_pimp_name(first_name, last_name)
st.write(f"Your New Handle: \n{pimp_name}")


