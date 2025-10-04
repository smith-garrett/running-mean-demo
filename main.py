from ast import Dict
import pydantic
import fastapi


app = fastapi.FastAPI()


class CurrentState(pydantic.BaseModel):
    running_mean: float
    count: int


class NewValue(pydantic.BaseModel):
    new_value: float


def calculate_new_state(current_state: CurrentState, new_value: float) -> CurrentState:
    new_count = current_state.count + 1
    new_mean = (
        new_value + current_state.count * current_state.running_mean
    ) / new_count
    return CurrentState(running_mean=new_mean, count=new_count)


current_state = CurrentState(running_mean=0.0, count=0)


@app.get("/")
async def get_current():
    return current_state


@app.post("/update/")
async def update_running_mean(new_value: NewValue):  # -> CurrentState:
    global current_state
    current_state = calculate_new_state(current_state, new_value.new_value)
    return current_state
    # return new_value
