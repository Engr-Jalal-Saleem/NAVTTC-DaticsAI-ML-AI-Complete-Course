from Password_generator import password_gen
import streamlit as st
st.title('Random Password Generator')
st.markdown("""
This tool generates a secure password using a mix of lowercase letters, uppercase letters, digits, and special characters. 
Each password includes at least three characters from each category to ensure complexity and security.
""")
if st.button('Generate Password'):
    generated_password = password_gen()
    st.text('Your generated password is:')
    st.code(generated_password, language='text')