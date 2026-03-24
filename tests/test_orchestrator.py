from gode.orchestrator import create_seed_state


def test_seed_state_contains_tasks() -> None:
    state = create_seed_state("Prototype agent workflows")
    assert state.objective == "Prototype agent workflows"
    assert len(state.tasks) >= 1
