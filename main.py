from fastapi import FastAPI


app = FastAPI(title='Leaning FastAPI App')


USERS = [
    {'id': 1, 'name': 'John', 'role': 'admin'},
    {'id': 2, 'name': 'Sarah', 'role': 'teacher'},
    {'id': 3, 'name': 'Antony', 'role': 'pupil'},
]


@app.get('/users/{users_id}')
def get_user_by_id(user_id: int) -> dict[str, str | int] | None:
    return next((item for item in USERS if item['id'] == user_id), None)
