# Game Project (Rock, paper, scissors)

Para correr el juego, sigue las siguientes instrucciones en la terminal

```sh
cd game
python3 main.py
```

# Countries project

Para correr el proyecto de countries, sigue las siguientes instrucciones en la terminal

```sh
cd csv_app
python3 -m venv env
source env/Scripts/activate
pip3 install -r requirements.txt
python3 main.py
```

# Dependencias

Para instalar una dependencia con pip ejecutar

```sh
pip3 install {dependency_name}
```

Para instalar una versión en específico

```sh
pip3 install {dependency_name}=={version}
```

# Entornos virtuales

Para desde donde se está ejecutando algo

```sh
which pip3
```

Para crear un entorno virtual en python

```sh
python3 -m venv {enviroment_name}
```

Para activar un entorno virtual

```sh
source env/Scripts/activate
```

Para desactivarlo

```sh
deactivate
```

Para ver que dependencias hay en ese entorno

```sh
pip3 freeze
```

Crear un archivo con las dependencias del proyecto

```sh
pip3 freeze > requirements.txt
```

Instalar las dependencias de un proyecto

```sh
pip install -r requirements.txt
```
