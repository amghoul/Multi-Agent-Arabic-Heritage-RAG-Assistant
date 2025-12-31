from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
from .tools.heritage_tool import HeritageTool
from .tools.language_detection import LanguageDetectionTool
from .tools.weather_tool import WeatherTool
from transformers import pipeline


txt_tool = HeritageTool()
language_tool = LanguageDetectionTool()
weather_tool = WeatherTool()

@CrewBase
class RagCrewai():
    """RagCrewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def guidance(self) -> Agent:
        return Agent(
            config=self.agents_config['guidance'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            tools=[txt_tool, language_tool, weather_tool],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['guidance_task'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the RagCrewai crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
