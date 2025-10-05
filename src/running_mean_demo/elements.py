import pydantic


class CurrentState(pydantic.BaseModel):
    running_mean: float
    count: int


class NewValue(pydantic.BaseModel):
    new_value: float


def calculate_new_state(current_state: CurrentState, new_value: float) -> CurrentState:
    """https://en.wikipedia.org/wiki/Moving_average#Cumulative_average"""
    new_count = current_state.count + 1
    new_mean = (
        new_value + current_state.count * current_state.running_mean
    ) / new_count
    return CurrentState(running_mean=new_mean, count=new_count)
