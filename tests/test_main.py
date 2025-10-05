import running_mean_demo
import pytest


@pytest.fixture()
def init_state():
    return running_mean_demo.CurrentState(running_mean=0.0, count=0)


@pytest.fixture()
def state_1_1():
    return running_mean_demo.CurrentState(running_mean=1.0, count=1)


class Testrunning_mean_demo:
    def test_one_update(self, init_state):
        updated = running_mean_demo.calculate_new_state(init_state, 1.0)
        assert updated == state_1_1
