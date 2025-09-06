import streamlit as st
import pandas as pd
st.title("Hi , Iam Omar Tawfik")
st.header("This Is First Project")
st.subheader("Sub Of First Project")
st.text("Nothing To Be Written Here")
st.markdown("# Omar Tawfik")
st.markdown("## Omar Tawfik")
st.markdown("### Omar Tawfik")
st.markdown("**Omar** Tawfik")
st.markdown("*Omar* Tawfik")
st.markdown(">Omar Tawfik")
str = "Print('Hello World')"
st.code(str)
st.markdown("---")
st.markdown('[LinkedIn](https://www.linkedin.com/in/omar-sayed-b68602243/)')
table = '''
|omar|Sayed |
|----|-------|
'''
st.markdown(table)
json = {"a" :"1,2,3","b":"4,5,6"}
st.json(json)
st.markdown("That is so funny! :joy:")
st.metric(label="Win Speed",
          value='70ms',delta='-2.8')
st.metric(label="Win Speed",
          value='70ms',delta='2.8')

table1 = ({"Column 1 ":[1,2,3,4,5],
          "Column2":[6,7,8,9,10]})
st.table(table1)
st.dataframe(table1)
st.image(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg",caption="أى حاجة و خلاص",width=400)
st.audio(r"D:\My Phone\Music\5. MARWAN MOUSSA - RO7 3ALATOL  مروان موسى - روح على طول.mp3")
st.video(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\Facebook wordmark - Open app - pfbid0QLQseH2GmTpyibznEskftSPpPxSc7R49iPDEah8i1QqPPeYkoPU9ShbZpq9frsHYl(720p).mp4")
car_list = ["toyota",'fiat','bmw','mg']
car = st.text_input("Enter The Car: ")
button = st.button("Check Availbality")

if button == True:
    car_lower = car.lower() in car_list
    if car_lower:
        st.text("Found")
    else:
        st.text("Not Found")


st.image(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg",caption="أى حاجة و خلاص",width=400)
file_mame = st.text_input("Enter The File Name: ")
st.write(file_mame)
with open(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg",'rb') as file:
 btn = st.download_button(
    label="Download Image",
    data=file,
    file_name=file_mame,
    mime="image/png"
 )



