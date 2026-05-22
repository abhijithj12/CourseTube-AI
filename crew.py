from crewai import Agent,Task,Crew
from crewai.project import CrewBase, agent , task, crew
from crewai.process import Process
from dotenv import load_dotenv
from tools import get_transcript,get_metadata,transcribe_with_wisper

load_dotenv()
@CrewBase

class Youtubecrew():
    agents_config='config/agents.yaml'
    tasks_config='config/tasks.yaml'

    @agent
    def TranscriptionAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["TranscriptionAgent"],
            tools=[get_transcript, transcribe_with_wisper],
            verbose=True
        )
    @agent
    def MetadataAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["MetadataAgent"],
            tools=[get_metadata],
            verbose=True
        )
    @agent
    def StructureAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["StructureAgent"],
            tools=[],
            verbose=True
        )
    
    @agent
    def NotesAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["NotesAgent"],
            tools=[],
            verbose=True
            )
    @agent
    def QuizAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["QuizAgent"],
            tools=[],
            verbose=True
        )
    @agent
    def AssignmentAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["AssignmentAgent"],
            tools=[],
            verbose=True
        )
    @agent
    def ReviewAgent(self) -> Agent:
        return Agent(
            config=self.agents_config["ReviewAgent"],
            tools=[],
            verbose=True
        )
    
    @task
    def TranscriptionTask(self) -> Task:
        return Task(
            agent=self.TranscriptionAgent(),
            config=self.tasks_config["TranscriptionTask"]
        )
    @task
    def MetadataTask(self) -> Task:
        return Task(
            agent=self.MetadataAgent(),
            config=self.tasks_config["MetadataTask"],
        )
    @task
    def StructureTask(self) -> Task:
        return Task(
            agent=self.StructureAgent(),
            config=self.tasks_config["StructureTask"],
            context=[self.TranscriptionTask()]
        )    
    @task
    def NotesTask(self) -> Task:
        return Task(
            agent=self.NotesAgent(),
            config=self.tasks_config["NotesTask"],
            context=[self.StructureTask()]
        )
    @task
    def QuizTask(self) -> Task:
        return Task(
            agent=self.QuizAgent(),
            config=self.tasks_config["QuizTask"],
            context=[self.NotesTask()]
        )
    @task
    def AssignmentTask(self) -> Task:   
        return Task(
            agent=self.AssignmentAgent(),
            config=self.tasks_config["AssignmentTask"],
            context=[self.NotesTask()]
        )
    @task
    def ReviewTask(self) -> Task:
        return Task(
            agent=self.ReviewAgent(),
            config=self.tasks_config["ReviewTask"],
            context=[self.NotesTask(), self.QuizTask(), self.AssignmentTask()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential
        )
    
if __name__=="__main__":
    youtube_crew=Youtubecrew()
    youtube_crew.crew().kickoff(inputs={"video_url":"https://youtu.be/gs9E7E0qOIc?si=g2Xmq5b-y3WrReAL"})