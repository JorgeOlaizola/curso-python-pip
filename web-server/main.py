import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5, 6]


@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return f"""
        <h1>Hola, soy una página</h1>
        <p>Esto es una respuesta directa de la ruta</p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()
