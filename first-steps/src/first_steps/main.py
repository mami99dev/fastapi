from fastapi import FastAPI

app = FastAPI(title='Mini Blog')


@app.get('/')
def home():
    return {
        'message': 'Bienvenidos a rimart health por Isaac Martinez'
    }
