import json

import typer
from rich.console import Console
from rich.table import Table

from gode.orchestrator import create_seed_state
from gode.registry import default_agents

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command()
def doctor() -> None:
    """Print a quick environment and project sanity check."""
    console.print("[bold green]gode[/bold green] is ready for terminal-first R&D.")
    console.print("Python package imports resolve correctly.")


@app.command()
def agents() -> None:
    """List the seed agents for the research sandbox."""
    table = Table(title="Seed Agents")
    table.add_column("Name")
    table.add_column("Role")
    table.add_column("Goal")
    table.add_column("Tools")

    for agent in default_agents():
        table.add_row(agent.name, agent.role.value, agent.goal, ", ".join(agent.tools))

    console.print(table)


@app.command()
def demo(
    objective: str = typer.Argument(
        "Prototype a terminal-native multi-agent coding workflow.",
        help="Research objective for the seed run state.",
    ),
) -> None:
    """Print a seed orchestration state for further experimentation."""
    state = create_seed_state(objective)
    state.agents = default_agents()
    console.print_json(json.dumps(state.model_dump(), indent=2))


if __name__ == "__main__":
    app()
