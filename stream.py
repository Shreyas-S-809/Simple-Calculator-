import streamlit as st 

# Title 

st.title("Simple Calculator")

# Dropdown instead of choice input 

choice = st.selectbox(
    "Select Operation", 
    ("Addition", "Subtraction", "Multiplication")
)

a = st.number_input("Enter the First Number : ", step = 1)
b = st.number_input("Enter the Second Number  :", step = 1)

# Funcitons 

def add(a,b):
    return a + b 
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b 

# Button

if st.button("Calculate"):
    if choice == "Addition":
        result = add(a,b)
        st.success(f"Result = {result}")

    elif choice == "Subtraction":
        result = sub(a,b)
        st.success(f"Result = {result}")

    elif choice == "Multiplication":
        result = mul(a,b)
        st.success(f"Result = {result}")
