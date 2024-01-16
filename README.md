# machine-learning-engineering-for-production

Repository to reproduce the examples in the course [Machine Learning For Production][mlcourse-link].

This repo is a recreation based on the [original course repository][original-repo] for personal study.

[mlcourse-link]: https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/
[original-repo]: https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public

## Course 1 - Introduction to Machine Learning in Production

### Week 1

In a terminal, first enter the poetry terminal to have the dependencies, then start up the server

```shell
poetry shell
python server.py
```

You can then test by going to [http://localhost:8000/docs#/default/prediction_predict_post](http://localhost:8000/docs#/default/prediction_predict_post) and uploading an image.

You can also use the client script to test the endpoint:

```shell
poetry shell
python client.py
```

### Week 2

Explore the jupyter notebook
