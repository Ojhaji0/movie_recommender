# 🎬 Movie Recommender System (Content-Based)

This project implements a basic content-based movie recommender system using the MovieLens 100K dataset. The system recommends movies based on genre similarity.

## ✨ Features

* **Content-Based Filtering**: Recommends movies based on shared genres with a given input movie.
* **Cosine Similarity**: Uses cosine similarity to measure the likeness between movie genre vectors.
* **Streamlit Web App**: Provides an interactive user interface to get movie recommendations.

## ⚙️ Technologies Used

* **Python**
* **Pandas**: For data manipulation and analysis.
* **scikit-learn**: For `cosine_similarity` to compute movie similarities.
* **Streamlit**: For building the web application.
* **Joblib**: For saving and loading the trained model and data.
* **Regular Expressions (`re`)**: For cleaning movie titles.

## 📊 Dataset

The project utilizes the [MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/100k/).

* `u.item`: Contains movie metadata, including movie ID, title, release date, and binary genre flags.
* `u.data`: Contains user ratings (though primarily used here for initial exploration, not for the core content-based recommendation logic).

## 🚀 How to Run

https://ojhaji0-movie-recommender-app-oaftym.streamlit.app/
