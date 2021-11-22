import streamlit as st
import numpy as np
import pandas as pd
import math


st.header("Welcome to Natasah Web App")
st.image("https://celebrationspress.com/wp-content/uploads/2017/12/120417Rapunzel.jpg")
st.title("CHINESE ZODIAC PREDICTION")

name = st.text_input("Please enter your name")
color = st.color_picker("Choose your favourite color")
date = st.date_input("Please enter your birthday date")
year = st.number_input("Please enter your birth of year",min_value=1)

if year % 12 == 0:
  sign = "Monkey"
elif year % 12 == 1:
  sign = "Rooster"
elif year % 12 == 2:
  sign = "Dog"
elif year % 12 == 3:
  sign = "Pig"
elif year % 12 == 4:
  sign = "Rat"
elif year % 12 == 5:
  sign = "Ox"
elif year % 12 == 6:
  sign = "Tiger"
elif year % 12 == 7:
  sign = "Rabbit"
elif year % 12 == 8:
  sign = "Dragon"
elif year % 12 == 9:
  sign = "Snake"
elif year % 12 == 10:
  sign = "Horse"
elif year % 12 == 11:
  sign = "Goat"

if st.button("Predict"):
    st.write(f"Your chinese zodiack is {sign}")

st.sidebar.header('Hello')
st.sidebar.write("This is Natasah Web App, in this web app will show the prediction of the chinese zodiac sign, to continue viewing the zodiac please click continue")
show = st.sidebar.checkbox('Continue')
if show:
  st.sidebar.markdown("![Alt Text](http://pa1.narvii.com/7463/94cfe6eeada62c2eb83eb6d3c3d98638faa62e57r1-320-198_00.gif)")
