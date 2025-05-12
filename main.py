import streamlit as st
import langchain_helper
st.title("Restaurant name Generator")
cuisine= st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexican","American","Arabic"))

#generate restaurant name and menu


if cuisine:
    response=langchain_helper.generate_restaurant_name_and_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(',')
    st.write("**MENU ITEMS**")
    
    for item in menu_items:
        st.write("-",item)

