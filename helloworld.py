import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title('Sentiment Analysis of Tweets about US Airlines')
st.sidebar.title('Sentiment Analysis of Tweets about US Airlines')
st.markdown('This application is a streamlit dashboard to analyze the sentiment of Tweets')
url=("C:/Users/coold/OneDrive/Desktop/py/Streamlit/Tweets.csv")
@st.cache(persist=True)
def load_data():
    data=pd.read_csv(url)
    data['tweet_created']=pd.to_datetime(data['tweet_created'])
    return data
data=load_data()
st.sidebar.subheader('Show Random Tweet')
random_tweet=st.sidebar.radio('Sentiment',('positive','negative','neutral'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0,0])
st.sidebar.markdown("Number of Tweets by Sentiment")
select=st.sidebar.selectbox('Visualization Type:',['Histogram','Pie-Chart'],key='1')
sentiment_count=data['airline_sentiment'].value_counts()
sentiment_count=pd.DataFrame({'Sentiment':sentiment_count.index,'Tweets':sentiment_count.values})

if not st.sidebar.checkbox("Hide",True):
    st.markdown('The Number of Tweets by Sentiment:')
    if select=="Histogram":
        fig=px.bar(sentiment_count,x='Sentiment',y='Tweets',color='Tweets',height=300,width=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(sentiment_count,values='Tweets',names='Sentiment')
        st.plotly_chart(fig)
st.sidebar.markdown('When and Where users are Tweeting From?')
hour=st.sidebar.number_input("Hour",min_value=1,max_value=24)
mod_data=data[data['tweet_created'].dt.hour==hour]
st.map(mod_data)