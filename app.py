import streamlit as st
import joblib
import re

# Load pre-saved data
cosine_sim_df = joblib.load('cosine_sim_df.pkl')
movies_df = joblib.load('movies_df.pkl')
title_to_movie_id = joblib.load('title_to_movie_id.pkl')
movie_id_to_title = joblib.load('movie_id_to_title.pkl')

# Recommender function
def get_content_based_recommendations(movie_title, cosine_sim_df, movies_df, top_n=5):
    movie_title_cleaned = re.sub(r'\s*\(\d{4}\)', '', movie_title).strip()
    if movie_title_cleaned not in title_to_movie_id:
        return ["Movie not found."]
    movie_id = title_to_movie_id[movie_title_cleaned]
    sim_scores = cosine_sim_df[movie_id].sort_values(ascending=False)
    sim_scores = sim_scores[sim_scores.index != movie_id]
    top_similar_movies = sim_scores.head(top_n)
    return [movie_id_to_title[m_id] for m_id in top_similar_movies.index]

# Streamlit UI
st.title("🎬 Movie Recommender (Content-Based)")

movie_input = st.text_input("Enter a movie name (e.g., Toy Story (1995)):")

if st.button("Recommend"):
    if movie_input:
        recommendations = get_content_based_recommendations(movie_input, cosine_sim_df, movies_df)
        st.subheader("Top 5 Similar Movies:")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
    else:
        st.warning("Please enter a movie title.")
