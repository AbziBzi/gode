from gode.models import RunState, Task, TaskStatus


def create_seed_state(objective: str) -> RunState:
    return RunState(
        objective=objective,
        tasks=[
            Task(
                id="research-1",
                title="Define the orchestration loop",
                description="Describe how agents are scheduled, handed work, and reviewed.",
                status=TaskStatus.PENDING,
                assigned_agent="planner",
            ),
            Task(
                id="runtime-1",
                title="Choose the tool runtime boundary",
                description="Decide how shell commands, files, and model calls are exposed.",
                status=TaskStatus.PENDING,
                assigned_agent="builder",
            ),
        ],
    )
