import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
age = st.text_input("На колко години си?")
if name:
   st.write(f"Здравей, {name}!")
if age:
   st.write(f"Ти си на {age} години!")
input("Ти си луд!")
