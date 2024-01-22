import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movie_list=movies['title'].values

st.header("Movie Reccomender System")
select_value=st.selectbox("Select movie from dropdown",movie_list)

def reccomend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    reccomend_movie=[]  
    for i in distance[1:6]:
        reccomend_movie.append(movies.iloc[i[0]].title)
    return reccomend_movie

if st.button("Show reccomend"):
    reccomendation=reccomend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(reccomendation[0])
    with col2:
        st.text(reccomendation[1])
    with col3:
        st.text(reccomendation[2])
    with col4:
        st.text(reccomendation[3])
    with col5:
        st.text(reccomendation[4])