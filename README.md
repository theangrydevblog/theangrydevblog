# theangrydevblog

## Instructions

### How to install dependencies

* This project uses pipenv for Python dependency management. All Python packages should be installed with `pipenv install <package>`
* Update `requirements.txt`. We also maintain a `requirements.txt` because we don't need another virtual environment inside a container. The `pip` installed inside the container uses this to install the Python dependencies in the container
    ```sh
    pipenv lock -r > requirements.txt
     ```

### How to add new environment variables

* For your local dev environment, just add it to the `.env` file (not checked into Git)
* For production, update `.k8s/deployment.yml` first, then add environment variable to CircleCI BEFORE deploying