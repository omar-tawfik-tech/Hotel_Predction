import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
  return pd.read_csv(file)

st.set_page_config(
  page_title="Tawfik"
  ,page_icon=r"C:\Users\os474\OneDrive\Desktop\ChatGPT Image Aug 5, 2025, 12_08_23 AM.png"
)
st.header("Welcome to My Streamlit App")
file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])
if file is not None:
    df = load_data(file)
    n_rows = st.slider("Choose number of rows to display",min_value=5, max_value=len(df))
    coulmns_to_show = st.multiselect("Select columns to display", df.columns.tolist(),default=df.columns.tolist())
    st.write(df[:n_rows][coulmns_to_show])
    tab1,tab2 = st.tabs(['Scatter Plot',"Histogram"])
    col1,col2,col3 = st.columns(3)
    with tab1:
     with col1:
      numericl_columns = df.select_dtypes(include=np.number).columns.to_list()
      color = st.selectbox("select Column Color",df.columns)
      with col2:
       x_columns = st.selectbox("select Coulmn on x-axis: ",numericl_columns)
       with col3:
        y_columns = st.selectbox("select Coulmn on y-axis: ",numericl_columns)
        fig_scatter = px.scatter(df,x=x_columns,y=y_columns,color=color)
    
        st.plotly_chart(fig_scatter)
     with tab2:   
      histogram_feature = st.selectbox("select Feature To Hisotgram",numericl_columns)
      fig_hist = px.histogram(df,x=histogram_feature)
      st.plotly_chart(fig_hist)