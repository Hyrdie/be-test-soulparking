# todo-list-soul-parking
For the soul parking dev test
Build with python 3.8 + FastAPI

Virtual Environment
====================
To run the project, you must create and activate the virtual environment first.

Windows : 
```
python3 -m venv env
cd env/Script/activate
```

Linux : 
```
python3 -m venv env
source ./env/bin/activate
```
install dependencies from requirements.txt (file is inside the app folder)
```
pip3 install -r requirements.txt
```

after that, you must create .env file with the value below (copy all of this):
.env is located inside app folder 
app/.env
```
APP_NAME = "todolist-rest-api"
ORIGINS=["*"]
CORS_ALLOW_METHODS=["*"]
CORS_ALLOW_HEADERS=["*"]
DATETIME_FORMAT= "%d-%m-%Y %H:%M:%S"
```
and then you can run it by:
```
python3 main.py
```
you can see the postman collection in the main directory

