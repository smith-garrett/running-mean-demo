import dataclasses
from functools import reduce


@dataclasses.dataclass
class CurrentState:
    running_mean: float
    count: int


def calculate_new_state(current_state: CurrentState, new_value: float) -> CurrentState:
    new_count = current_state.count + 1
    new_mean = (
        new_value + current_state.count * current_state.running_mean
    ) / new_count
    return CurrentState(new_mean, new_count)


def main():
    vals = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    init_state = CurrentState(0, 0)
    print(init_state)
    for v in vals:
        init_state = calculate_new_state(init_state, v)
        print(init_state)


if __name__ == "__main__":
    main()
