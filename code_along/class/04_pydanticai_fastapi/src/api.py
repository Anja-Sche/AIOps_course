from fastapi import FastAPI
from pydantic_ai import Agent
from utils import query_duckdb
from data_models import Movie, Prompt
import os
from model import nvidia_model

app = FastAPI()

@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")

@app.post("/movie")
async def create_movie(query: Prompt):
    result = await agent.run(query.prompt)
    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?)",
        parameters=(movie.title, movie.year, movie.genre, movie.rating)
    )

    return movie