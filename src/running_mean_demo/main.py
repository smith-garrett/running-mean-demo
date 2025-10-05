from . import elements
import fastapi


app = fastapi.FastAPI()


current_state = elements.CurrentState(running_mean=0.0, count=0)


@app.get("/")
async def get_current():
    return current_state


@app.post("/update/")
async def update_running_mean(
    new_value: elements.NewValue,
):  # -> CurrentState:
    global current_state
    current_state = elements.calculate_new_state(current_state, new_value.new_value)
    return current_state
