from gode.models import AgentSpec


def default_agents() -> list[AgentSpec]:
    return [
        AgentSpec(
            name="planner",
            role="orchestrator",
            goal="Break research objectives into executable coding tasks.",
            tools=["task_queue", "shell"],
        ),
        AgentSpec(
            name="builder",
            role="specialist",
            goal="Implement and modify code based on the current task.",
            tools=["shell", "git", "tests"],
        ),
        AgentSpec(
            name="reviewer",
            role="reviewer",
            goal="Inspect outputs for regressions, gaps, and next-step recommendations.",
            tools=["diff", "tests"],
        ),
    ]
