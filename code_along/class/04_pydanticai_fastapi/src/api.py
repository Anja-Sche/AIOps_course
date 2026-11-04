from agents import movie_agent
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/movies")
# async is default in FastAPI
# write it for best practise
async def read_movies():
    # TODO: implement this
    return "testing reload"

@app.post("/movie")
async def create_movie(query): 
    result = await movie_agent.run(query)
    return result.output

    # TODO: save to database

    # query_duckdb(
    #     "INSERT INTO movies VALUES (?,?,?,?)",
    #     parameters=(movie.title, movie.year, movie.genre, movie.rating)
    # )

    # return movie
