import random as rn
import streamlit as st
sml_let = 'qwertyuiopasdfghjklzxcvbnm'
cap_let = sml_let.upper()
digits = "1234567890"
spl_char = "!@#$%^&*|?><."
def password_gen():
    global sml_let, cap_let, digits, spl_char
    ls = []
    for i in range(3):
        rn_sml_let = rn.choice(sml_let)
        ls.append(rn_sml_let)
        rn_cap_let = rn.choice(cap_let)
        ls.append(rn_cap_let)
        rn_digits = rn.choice(digits)
        ls.append(rn_digits)
        rn_spl_char = rn.choice(spl_char)
        ls.append(rn_spl_char)
    password = ''.join(ls)
    return password

st.title('Random Password Generator')
st.markdown("""
This tool generates a secure password using a mix of lowercase letters, uppercase letters, digits, and special characters. 
Each password includes at least three characters from each category to ensure complexity and security.
""")
if st.button('Generate Password'):
    generated_password = password_gen()
    st.text('Your generated password is:')
    st.code(generated_password, language='text')