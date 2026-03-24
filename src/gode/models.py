from enum import Enum

from pydantic import BaseModel, Field


class AgentRole(str, Enum):
    ORCHESTRATOR = "orchestrator"
    SPECIALIST = "specialist"
    REVIEWER = "reviewer"


class AgentSpec(BaseModel):
    name: str
    role: AgentRole
    goal: str
    tools: list[str] = Field(default_factory=list)


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"


class Task(BaseModel):
    id: str
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    assigned_agent: str | None = None


class RunState(BaseModel):
    objective: str
    agents: list[AgentSpec] = Field(default_factory=list)
    tasks: list[Task] = Field(default_factory=list)
