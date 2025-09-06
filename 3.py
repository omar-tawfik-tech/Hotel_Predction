import streamlit as st
# st.header("Welcome To My Site")
# st.image(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg")
# images_list = [r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg",r"C:\Users\os474\OneDrive\Desktop\ChatGPT Image Aug 3, 2025, 09_41_33 PM.png"]
# st.image(image=images_list,width=100)
# st.link_button("My LinkedIn","https://www.linkedin.com/in/omar-sayed-b68602243/")
st.header("Welcome To My Site")
images_list = [r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\WhatsApp Image 2024-07-27 at 6.45.50 PM.jpeg",r"C:\Users\os474\OneDrive\Desktop\ChatGPT Image Aug 3, 2025, 09_41_33 PM.png"]
images = st.checkbox("Do You Want To See Photos")
codes = st.checkbox("Do Want To See Codes?")
if images:
    st.image(image=images_list,width=100)
if codes:
    st.code("print('Omar Tawfik')")

toggle_audio = st.toggle("Enable Audio")
toggle_video = st.toggle('Enable Video')
if toggle_video:
    st.video(r"C:\Users\os474\OneDrive\Desktop\OT\Work\STEAM Academy\Python\AIO\Facebook wordmark - Open app - pfbid0QLQseH2GmTpyibznEskftSPpPxSc7R49iPDEah8i1QqPPeYkoPU9ShbZpq9frsHYl(720p).mp4")

if toggle_audio:
    st.audio(r"D:\My Phone\Music\5. MARWAN MOUSSA - RO7 3ALATOL  مروان موسى - روح على طول.mp3")


