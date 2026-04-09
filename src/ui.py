import streamlit as st
from main import add, subtract, multiply, divide

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        try:
            result = divide(num1, num2)
        except ValueError as e:
            st.error(str(e))
            result = None

    if result is not None:
        st.success(f"The result of {operation.lower()}ing {num1} and {num2} is: {result}")  