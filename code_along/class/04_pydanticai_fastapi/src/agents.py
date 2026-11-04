from pydantic_ai import Agent 
from model import nvidia_model


movie_agent = Agent(model=nvidia_model(), 
                    instructions="Yot are an expert in finding a movie based on a text")

# To test an Agent in .py script -> use run_sync
movie = movie_agent.run_sync("I'll be back")
print(movie)

