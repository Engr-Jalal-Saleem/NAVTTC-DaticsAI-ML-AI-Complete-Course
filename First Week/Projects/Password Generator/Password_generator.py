import random as rn
import streamlit as st
sml_let = 'qwertyuiopasdfghjklzxcvbnm'
cap_let = sml_let.upper()
digits = "1234567890"
spl_char = "!@#$%^&*|?><."
# pass_length = int(input("Enter the length of the password: "))
# sml_let_len = int(input("Enter the number of small letters: "))
# cap_let_len = int(input("Enter the number of capital letters: "))
# digits_len = int(input("Enter the number of digits: "))
# spl_char_len = int(input("Enter the number of special characters: "))
def password_gen(pass_length=16, sml_let_len=4, cap_let_len=4, digits_len=4, spl_char_len=4):
    global sml_let, cap_let, digits, spl_char  
    ls = []
    sum_len = sml_let_len + cap_let_len + digits_len + spl_char_len
    if pass_length == sum_len:
        for i in range(sml_let_len):
            rn_sml_let = rn.choice(sml_let)
            ls.append(rn_sml_let)
        for i in range(cap_let_len):
            rn_cap_let = rn.choice(cap_let)
            ls.append(rn_cap_let)
        for i in range(digits_len):
            rn_digits = rn.choice(digits)
            ls.append(rn_digits)
        for i in range(spl_char_len):
            rn_spl_char = rn.choice(spl_char)
            ls.append(rn_spl_char)
    else:
        st.text("The sum of all the lengths should be equal to the length of the password")
        st.text("Please try again")
        st.text(pass_length)
        st.text(sum_len)
    rn.shuffle(ls)
    final_password = ''.join(ls)
    return final_password
