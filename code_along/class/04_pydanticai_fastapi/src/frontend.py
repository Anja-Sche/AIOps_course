import requests
import streamlit as st


def layout():
    st.markdown("# MovieBot")

    movie_str = st.text_input("Give a statement and it will give back a movie")

    movie = requests.post("http://127.0.0.1:8000/movie", json={"query": movie_str}).json()
    st.write(movie)

    genre = st.selectbox("Choose genre", options=["action", "comedy", "documentary", "cartoon", "romance", "adventure"])

    movies = requests.get(f"http://127.0.0.1:8000/movies?genre={genre}").json()

    st.dataframe(movies)



if __name__ == "__main__":
    layout()