### 1. Install dependecies

```bash
cd SberLinks

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Database + Webserver (under http, for testing setup on localhost:8000)

```bash
docker-compose up -d
```

### 3. Now you can test app

```bash
http://localhost:8000/
```

### 4. Running tests

```bash
# Note, it will use second database declared in docker-compose.yml, not default one. Not working now :(
pytest                                                                    
```
