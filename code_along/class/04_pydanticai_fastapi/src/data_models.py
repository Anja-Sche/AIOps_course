from pydantic import BaseModel, Field
from typing import Literal

# inherits from BaseModel
class Movie(BaseModel):
    title: str = Field(description="Title of movie")
    year: int = Field("Year when this movie came out")
    genre: Literal["action", "comedy", "romance", "cartoon", "adventure", "documentery"] = Field(
        description="main genre, if there is more than one, choose the most characteristic one")
    rating: int = Field(description=("Give a rating between 1 and 5," 
                        "the higher the more popular the movie is"),
                        ge=1, 
                        le=5) 
    summary: str = Field(description="Short exiting summary of the movie, 1-2 scentences")




class Prompt(BaseModel):
    prompt: str
