### 1. Install dependecies

```bash
cd SberLinks

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### 2. Setup databases

```bash
### Setup two databases, one db for test
docker-compose up -d

### Alembic migrations upgrade
bash init.sh
```

### 3. Now you can run app

```bash

uvicorn app.main:app --reload

```

### 5. Activate pre-commit

[pre-commit](https://pre-commit.com/) is de facto standard now for pre push activities like isort or black.

Refer to `.pre-commit-config.yaml` file to see my opinionated choices.

```bash
# Install pre-commit
pre-commit install

# First initialization and run on all files
pre-commit run --all-files
```

### 6. Running tests

```bash
# Note, it will use second database declared in docker-compose.yml, not default one. Not working now :(
pytest                                                                    
```
