import streamlit as st
import pickle
import requests



def recommend(quotes):
    quote_index = quote_list_df[quote_list_df['og_quotes'] == quotes].index[0]
    distance = similarity[quote_index]
    quotes_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_quotes = []
    
    for i in quotes_list:
        id=quote_list_df.iloc[i[0]].id
        recommend_quotes.append(quote_list_df.iloc[i[0]].og_quotes)
        
    return recommend_quotes


quote_list_df = pickle.load(open('quotes_list.pkl','rb'))
quotes_title = quote_list_df['og_quotes'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Quotes Recommender System')

selected_quotes = st.selectbox(
'Quotes List',
quotes_title)

if st.button('Recommend'):
    recommend_quotes_name = recommend(selected_quotes)
    
    
    with st.container():
        st.write("Quote 1")
        st.markdown(recommend_quotes_name[0])
        
    with st.container():
        st.write("Quote 2")
        st.markdown(recommend_quotes_name[1])
        
    with st.container():
        st.write("Quote 3")
        st.markdown(recommend_quotes_name[2])
        
    with st.container():
        st.write("Quote 4")
        st.markdown(recommend_quotes_name[3])
        
    with st.container():
        st.write("Quote 5")
        st.markdown(recommend_quotes_name[4])
        
    
        
    # with c2:
    #     st.text(recommend_quotes_name[1])
        

    # with c3:
    #     st.text(recommend_quotes_name[2])
        
    # with c4:
    #     st.text(recommend_quotes_name[3])
        
    # with c5:
    #     st.text(recommend_quotes_name[4])
        


