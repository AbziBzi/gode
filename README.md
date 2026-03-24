# gode

Terminal-first R&D workspace for exploring multi-agent orchestration for coding workflows.

## Why this stack

This project should optimize for experimentation, not product polish. The recommended stack is:

- Python 3.13 for orchestration, process control, and AI SDK support.
- `Typer` for a clean CLI without building UI.
- `Pydantic` for typed agent, task, and run-state models.
- `Rich` for readable terminal output.
- `pytest` for quick validation as the orchestration logic grows.

Why Python over TypeScript:

- Better fit for rapid systems experimentation and agent research.
- Strong async/process tooling for driving CLIs, shells, and local code tools.
- Excellent LLM ecosystem without forcing a web stack too early.
- Easier to model graphs, planners, memory stores, and evaluators as plain code.

## Recommended architecture

Keep the core framework-light at first:

- `models.py`: typed definitions for agents, tasks, messages, tool calls, and execution state.
- `registry.py`: registers agents and tools.
- `orchestrator.py`: decides which agent runs next and how work is handed off.
- `runtime.py`: executes shell/tools and captures structured results.
- `cli.py`: developer entrypoint for experiments.

Avoid committing to LangGraph, CrewAI, or AutoGen immediately. They are useful reference points, but starting with your own thin orchestration layer will make the design space clearer.

## Getting started

If you use `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run gode doctor
uv run gode demo
```

If you do not use `uv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
gode doctor
gode demo
```

## Near-term roadmap

1. Add an agent spec with role, tools, and constraints.
2. Add a task graph and handoff protocol between agents.
3. Add a shell/tool runtime with logging and replay.
4. Add evaluator loops so one agent can review another agent's output.
5. Add model-provider adapters after the orchestration loop is stable.
