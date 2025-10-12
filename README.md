# Demo project: Running mean in a web API

[![CI Jobs](https://github.com/smith-garrett/running-mean-demo/actions/workflows/ci.yaml/badge.svg)](https://github.com/smith-garrett/running-mean-demo/actions/workflows/ci.yaml)
[![Deploy to Render](https://github.com/smith-garrett/running-mean-demo/actions/workflows/deploy.yaml/badge.svg)](https://running-mean-demo.onrender.com/docs)

The purpose of this project is to learn/practice implementing, testing, and deploying machine learning models[^*]. I wanted to implement some good practices (automated linting, testing, deployment) using Github Actions. The unit tests are done using [`pytest`](https://docs.pytest.org/en/stable/), pre-commit checks with [`pre-commit`](https://pre-commit.com/), and the whole thing is wrapped in [FastAPI](https://fastapi.tiangolo.com/) and deployed to a couple of endpoints on [Render](https://www.render.com).

To view the current running average, you can `curl https://running-mean-demo.onrender.com` or just point a browser to the URL. To update the running mean, you can run `curl --json '{"new_value": XXX}' https://running-mean-demo.onrender.com/update/`, replacing `XXX` with a floating point number. The model will then update its estimate of the cumulative mean and return the result as JSON, e.g., `{"running_mean":-3.871,"count":1}`, where `running_mean` is the estimate and `count` is the number of data points that have been posted so far. Note that the estimate gets reset if the endpoint is inactive for too long.

This is a work in progress.

---
[^*]: I'm using the term "machine learning" loosely here. The "model" calculates the [cumulative mean](https://en.wikipedia.org/wiki/Moving_average#Cumulative_average). I guess you could construe it as a continuous-training system, where the model is "trained" every time someone POSTs to the endpoint.
