from Password_generator import password_gen
import streamlit as st
st.title('Random Password Generator')
st.markdown("""
This tool generates a secure password using a mix of lowercase letters, uppercase letters, digits, and special characters. 
Each password includes at least three characters from each category to ensure complexity and security.
""")

pass_length = st.text_input('Enter the length of the password:', value=16)
sml_let_len = st.text_input('Enter the number of small letters:', value=4)
cap_let_len = st.text_input('Enter the number of capital letters:', value=4)
digits_len = st.text_input('Enter the number of digits:', value=4)
spl_char_len = st.text_input('Enter the number of special characters:', value=4)
if st.button('Generate Password'):
    generated_password = password_gen(int(pass_length),int(sml_let_len), int(cap_let_len), int(digits_len), int(spl_char_len))
    st.text('Your generated password is:')
    st.code(generated_password, language='text')