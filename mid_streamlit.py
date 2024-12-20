
import streamlit as st
import plotly.express as px 
import pandas as pd
import numpy as np

# Page Title
st.set_page_config(
    layout="wide",
    page_title = 'Simple DashBoard for Boston Crimes'
)
st.title('🚔Simple DashBoard for Boston Crimes')

df = pd.read_csv('cleand_dataset.csv')
## Creating a side bar for showing data and visuaization per year
x = st.sidebar.checkbox('Press me if you wanna Show Data',False,key=1)
year = st.sidebar.selectbox('select year', df['year'].unique())
if x:
    st.header("Here`s your DATA ")
    st.dataframe(df.head(8))
# pepare the size of each column
col1, col2,col3 = st.columns([5,1,5])
with col1:
    new_df= df[(df['year'] == year)]
    # A Histogram to visualize the Distrubution of most crime occur
    new_df =new_df['offense_code_group'].value_counts().reset_index().head(25)
    new_df.columns = ['offense_code_group','counts']
    fig = px.histogram(new_df,x='offense_code_group',y='counts',template='plotly_dark',title='A Histogram to visualize the Distrubution of most crime occur')
    st.plotly_chart(fig,use_container_width=True)

    # Visualze The district where most crimes occur
    new_df= df[(df['year'] == year)]
    new_df =new_df['district'].value_counts().reset_index().head(25)
    new_df.columns = ['district','counts']
    fig = px.histogram(new_df,x='district',y='counts',template='plotly_dark',title='which district has  most crimes occur')
    st.plotly_chart(fig,use_container_width=True)
    



     #2D line plot represent how many crimes occurs over the year
    new_df= df[(df['year'] == year)]
    new_df['occurred_on_date']=pd.to_datetime(new_df['occurred_on_date'],errors='coerce')
    new_df['month_year'] = new_df['occurred_on_date'].dt.strftime('%Y-%m')
    new_df =new_df.groupby('month_year')['offense_code_group'].count().sort_index().reset_index()
    new_df.columns = ['month_year','counts']
    fig = px.line(new_df,x='month_year',y='counts',template='plotly_dark',title='2D line plot represent how many crimes occurs over the year')
    st.plotly_chart(fig,use_container_width=True,key='line')

    new_df= df[(df['year'] == year)]
    new_df = df[df['offense_code_group'] == 'motor vehicle accident response']
    new_df = new_df['street'].value_counts().reset_index().head(20)
    new_df.columns = ['street','counts']
    fig = px.bar(new_df,x='street',y='counts',template='plotly_dark',title='Visualize the most street have the most car accident')
    st.plotly_chart(fig,use_container_width=True)
    
    new_df= df[(df['year'] == year)]
    new_df = df['period'].value_counts().reset_index()
    new_df.columns =['period','counts']
    fig = px.histogram(new_df,x='period',y='counts',template='plotly_dark',title='making a histogram to visualize which period of the day contributes the most crimes ')
    st.plotly_chart(fig,use_container_width=True)

with col3:
    #The highest fine for the crime
    new_df= df[(df['year'] == year)]
    avg_fine = new_df.groupby('offense_code_group')['fine'].mean().reset_index().sort_values(by='fine',ascending=False).head(30)
    fig = px.pie(avg_fine,values='fine',names='offense_code_group',color_discrete_sequence=px.colors.qualitative.Pastel,title='The highest fine for the crime')
    st.plotly_chart(fig,use_container_width = True)

    #which street is most expsed to crimes
    new_df = df[(df['year'] == year)]
    o_c =df['street'].value_counts().reset_index().head(25)
    o_c.columns = ['street','counts']
    fig = px.histogram(o_c,x='street',y='counts',template='plotly_dark',title='which street is most expsed to crimes?')
    st.plotly_chart(fig,use_container_width=True,key='dc')

    #Visualize that most month contribute to the most crimes
    new_df = df[(df['year'] == year)]
    o_c =new_df['month_name'].value_counts().reset_index().head(25)
    o_c.columns = ['month_name','counts']
    fig = px.histogram(o_c,x='month_name',y='counts',template='plotly_dark',title='Visualize that most month contribute to the most crimes')
    st.plotly_chart(fig,use_container_width=True,key='s')

    new_df= df[(df['year'] == year)]
    most_street = new_df[new_df['shooting']=='Y']
    most_street = most_street['street'].value_counts().reset_index().head(25)
    most_street.columns = ['street','count']
    fig = px.histogram(most_street,x='street',y='count',template='plotly_dark',title='Bivariate analysis: most streets have the most shooting crimes')
    st.plotly_chart(fig,use_container_width=True,key='sh')


     #Visualize that most year contribute to the most crimes
    df['year'] = df['year'].astype(str)
    new_df = df['year'].value_counts().reset_index()
    new_df.columns = ['year','counts']
    fig = px.bar(new_df,x='year',y='counts',title='Most Crimes Occur Over the Years',template= 'plotly_dark')
    st.plotly_chart(fig,use_container_width=True)


