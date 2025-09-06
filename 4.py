import streamlit as st
st.header("Choose Your Course")

radio_button = st.radio("Choose Your Course",
                        ["HTML|CSS:rainbow:",
                         "JavaScript",
                         "C++"],index=None)
if radio_button =="HTML|CSS:rainbow:":
 st.write("You Selected HTML|CSS:rainbow:")
elif radio_button == "JavaScript":
 st.write("You Selected JavaScript")
elif radio_button == "C++":
 st.write("You Selected C++") 