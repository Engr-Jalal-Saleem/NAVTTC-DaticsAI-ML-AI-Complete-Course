import streamlit as st
st.title("Welcome to Rock, Paper, Scissors Game!")
st.header('How to play:')
st.write('Choose your weapon and see if you can beat the computer!')
st.write('Rock beats Scissors')
st.write('Scissors beats Paper')
st.write('Paper beats Rock')
st.image(image=r'D:\NAVTCC\First Week\Projects\Rock Game\src\Rock-paper-scissors_(paper).png', caption='Paper', width=250)
st.image(image=r'D:\NAVTCC\First Week\Projects\Rock Game\src\Rock-paper-scissors_(rock).png', caption='Rock', width=250)
st.image(image=r'D:\NAVTCC\First Week\Projects\Rock Game\src\Rock-paper-scissors_(scissors).png', caption='Scissors', width=250)

st.subheader('Choose your weapon:')
st.selectbox('Select', options=['Rock', 'Paper', 'Scissors'])