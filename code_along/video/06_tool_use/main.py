from agents import weather_agent
import asyncio
from tools import WeatherDeps


async def main(prompt, **kwargs):
    result = await weather_agent.run(prompt, **kwargs)
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main("What is the weather in Järvsö", deps = WeatherDeps(city="Järvsö")))
    asyncio.run(main("What is the weather in Paris", deps = WeatherDeps(city="Paris")))
    asyncio.run(main("Give me a fun joke about Paris", deps = WeatherDeps(city="Paris")))