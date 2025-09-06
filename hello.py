import streamlit as st
import time
st.header("First Project")

st.sidebar.title("About")
with st.sidebar:
 Choosen_Shape = st.selectbox("Choose Shape: ", ["Circle","Rectangle"])

if Choosen_Shape == "Circle":
    radius = st.number_input("Enter The Raduis: ",max_value=100,min_value=0)
    area = 2*3.14*(radius) 
    Permiter = 3.14*(radius**2) 

if Choosen_Shape == "Rectangle":
    Length = st.number_input("Enter The Length: ",max_value=100,min_value=0)
    Width = st.number_input("Enter The Width: ",max_value=100,min_value=0)
    area = 2*(Length+Width)
    Permiter = Length*Width

Compute_btn = st.button("Computes Area And Permiter")
if Compute_btn:
    with st.spinner("Computing..."):
     time.sleep(2)
     st.success("Done")
     st.write('Area ',area)
     st.write('Premiter ',Permiter)

