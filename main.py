
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import preprocessor, helper
st.sidebar.title("Whats app Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
     bytes_data = uploaded_file.getvalue()
     data =bytes_data.decode("utf-8")
     
     df=preprocessor.preprocess(data)

     st.dataframe(df)

     user_list = df['user'].unique().tolist()
     user_list.remove('group_notification')
     user_list.sort()
     user_list.insert(0,'Overall')
     selected_user = st.sidebar.selectbox('Show analysis wrt',user_list)

     if st.sidebar.button("Show Analysis"):

        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        col1, col2,col3,col4 =st.columns(4)
        with col1:
            st.subheader("Total Messages")
            st.title(num_messages)

        with col2:
            st.subheader("Total words")
            st.title(words)
        with col3:
            st.subheader("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.subheader("Links Shsred")
            st.title(num_links)
       
       #monthly timline 
st.title("Monthly Timeline")
timeline = helper.monthly_timeline(selected_user,df)
fig,ax = plt.subplots()
ax.plot(timeline['time'], timeline['message'],color='green')
plt.xticks(rotation='vertical')
st.pyplot(fig)