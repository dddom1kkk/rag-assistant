# What this file is about

Here will be kept all my decisions for this project and reasons I made these choices.

## Fetching FastAPI Documentation

Release that is being fetched is 0.142.2. I fetched all the documentation from GitHub repo, using sparse checkout, as repo contains unnecessary data that I don't need for now. I separately fetched `docs/en/docs` and `docs_src` because first folder contains all the documentation and the second folder contains code parts that are referenced in the first folder.