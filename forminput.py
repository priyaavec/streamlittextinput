import streamlit as st

customer = "John"
customer_password = "4321"
employee = "Tom"
emppassword = "1234"
st.title("Text input")
option = st.selectbox('Please select a template?', ('Employee', 'Customer'))
if option == 'Employee':
    st.write("Your option is Employee template")
    st.text_input("User name", employee)
    st.text_input("Password", emppassword)
else:
    st.write("Your option is Customer template")
    st.text_input("User name", customer)
    st.text_input("Password",customer_password)
