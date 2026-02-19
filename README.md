# innovation-backend
** API TO MANAGE THE USERS, CLASSROOMS, ROUTES AND CHECKPOINTS **

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements .txt

run the .sql in your database and fill out the database url in the .env


run: 
openssl rand -hex 32

to get the secret key


fastapi dev app/main.py

