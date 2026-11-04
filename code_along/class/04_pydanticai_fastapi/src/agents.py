from pydantic_ai import Agent 
from model import nvidia_model
from data_models import Movie


movie_agent = Agent(model=nvidia_model(), 
                    instructions="You are an expert in finding a movie based on a text", 
                    output_type=Movie)



# be able to run as standalone script
# __name__ is __main__ when run directly
# __name__ is 'agents' (modulens namn) when imported
if __name__ == "__main__":

    # To test an Agent in .py script -> use run_sync
    movie = movie_agent.run_sync("I'll be back")
    print(movie)

