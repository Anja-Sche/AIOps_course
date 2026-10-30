from fastapi import FastAPI
from pydantic_ai import Agent
from dotenv import load_dotenv
from utils import query_duckdb
from data_models import Movie, Prompt
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import os


load_dotenv()

model = OpenAIChatModel(
    model_name="nvidia/nemotron-3.5-lightning-30b-a3b",
    provider=OpenAIProvider(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = os.environ["NVIDIA_API"]
    ),
)

agent = Agent(model=model, output_type=Movie)

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