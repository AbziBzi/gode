from gode.registry import default_agents


def test_default_agents_are_named_uniquely() -> None:
    agents = default_agents()
    assert len({agent.name for agent in agents}) == len(agents)
