from fastapi import FastAPI


app = FastAPI(title='Leaning FastAPI App')


@app.get('/hello')
def hello_handler():
    return {'result': 'Hello World!'}
