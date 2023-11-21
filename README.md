### 1. Install dependecies

```bash
cd SberLinks

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### 2. Database + Webserver (under http, for testing setup on localhost:8000)

```bash
docker-compose up -d
```

### 3. Now you can test app

```bash
http://localhost:8000/
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
