import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',
                   page_title="Country Census Analysis", 
                   )
st.header('Analysis of Data --- Census(2011)')


# Data wala part
df = pd.read_csv('final_df.csv')
list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Over All India')

#


st.sidebar.title('India Data Viz')
selected_state = st.sidebar.selectbox('Select One',list_of_state)
primary = st.sidebar.selectbox('Select Primary',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary',sorted(df.columns[5:]))
plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size Represent primary')
    st.text('Color Represent secondary')
    if selected_state == 'Over All India':
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=4,size_max=35,hover_name='District',width=1500,height=700,map_style='carto-positron',color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)

        # ---- Top Population state--#
        st.subheader('Top State Population Wise')
        temp = df.groupby('State')[['District','Population','Male_Literate','Female_Literate','Households_with_Internet','Housholds_with_Electric_Lighting','sex_ratio','literacy_rate']].sum().reset_index()
        t = temp[['State','Population']]
        st.dataframe(t.sort_values(by='Population',ascending=False).head(),hide_index=True)


        #---- Top literacy---#
        st.subheader('Top States Literacy Wise')
        temp = df.groupby('State')[['District','Population','Male_Literate','Female_Literate','Households_with_Internet','Housholds_with_Electric_Lighting','sex_ratio','literacy_rate']].mean(numeric_only=True).reset_index()
        t = temp[['State','literacy_rate']]
        t['literacy_rate'] = t['literacy_rate'].round(2)
        st.dataframe(t.sort_values(by='literacy_rate',ascending=False).head(),hide_index=True)

        #----Top electricity---#
        st.subheader('Top States Electricity HouseHold Use Wise')
        t = temp[['State','Housholds_with_Electric_Lighting']]
        t['Housholds_with_Electric_Lighting'] = t['Housholds_with_Electric_Lighting'].round(2)
        st.dataframe(t.sort_values(by='Housholds_with_Electric_Lighting',ascending=False).head(),hide_index=True)

         #----Top electricity---#
        st.subheader('Top States Internet HouseHold Use Wise')
        t = temp[['State','Households_with_Internet']]
        t['Households_with_Internet'] = t['Households_with_Internet'].round(2)
        st.dataframe(t.sort_values(by='Households_with_Internet',ascending=False).head(),hide_index=True)

        pass #state wise
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=7,size_max=35,hover_name='District',width=1500,height=700,map_style='carto-positron',color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig)

        temp = df[df['State'] == selected_state]

        #-------------Tops 5 popultation------#
        st.subheader('This Is Population Data of Top-5 District')
        st.dataframe(temp[['District','Population','sex_ratio']].sort_values(by='Population',ascending=False).head(5).reset_index()[['District','Population','sex_ratio']],hide_index=True)

        #------------Top district for literacy-----#
        st.subheader('This Is Literacy Data of Top-5 District')
        st.dataframe(temp[['District','literacy_rate']].sort_values(by='literacy_rate',ascending=False).head().reset_index()[['District','literacy_rate']],hide_index=True)

        #------------Top 5 electricity----#
        st.subheader('This Is Housholds with Electric Lighting Data of Top-5 District')
        st.dataframe(temp[['District','Housholds_with_Electric_Lighting']].sort_values(by='Housholds_with_Electric_Lighting',ascending=False).head().reset_index()[['District','Housholds_with_Electric_Lighting']],hide_index=True)

        #------------Tops 5 Households_with_Internet-----#
        st.subheader('This Is Households with Internet Data of Top-5 District')
        st.dataframe(temp[['District','Households_with_Internet']].sort_values(by='Households_with_Internet',ascending=False).head().reset_index()[['District','Households_with_Internet']],hide_index=True)
        
        pass #state wise

    st.header('Thanks For Coming Here!')
