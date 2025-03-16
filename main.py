import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,1000)


st.subheader("Instint Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustle')
        if response.status_code == 200:
            hustle = response.json()
            return hustle["side_hustle"]
        else: 
            return ("Freelancing")

    except:
        return ("Some thing went wrong")

st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)

def fetch_moneyMaking():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quote')
        if response.status_code == 200:
            money = response.json()
            return money['money_quote']
        else:
            return ("Earn Money Not Spend")
    except:
        return ("Some Thing When Wrong")
    

st.subheader("Money Making Motivation")
if st.button("Money Quote"):
    money_quote  = fetch_moneyMaking() 
    st.info(money_quote)

