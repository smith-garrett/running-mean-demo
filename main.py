import dataclasses


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
    print("Hello from running-mean-demo!")


if __name__ == "__main__":
    main()
