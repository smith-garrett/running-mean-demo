from running_mean_demo import elements
import pytest


@pytest.fixture
def init_state():
    return elements.CurrentState(running_mean=0.0, count=0)


@pytest.fixture
def state_one_one():
    return elements.CurrentState(running_mean=1.0, count=1)


@pytest.fixture
def state_two_two():
    return elements.CurrentState(running_mean=1.5, count=2)


class Testrunning_mean_demo:
    def test_one_update(self, init_state, state_one_one):
        updated = elements.calculate_new_state(init_state, 1.0)
        assert updated == state_one_one

    def test_two_updates(self, init_state, state_two_two):
        updated = elements.calculate_new_state(init_state, 1.0)
        updated = elements.calculate_new_state(updated, 2.0)
        assert updated == state_two_two
