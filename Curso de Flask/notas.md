
## Ambiente

> Instalar o Virtualenv

    pip install virtualenv

> Criar um ambiente virtual - venv pode ser outro nome

    virtualenv venv

> se tiver várias versões:

    virtualenv -p Python3 venv

> ativar o ambiente de virtualização - Win10

    venv\Scripts\activate.bat  

> instalar o Flask

     pip install flask

> Saber as biblioteca instaladas

    pip freeze

> Se quiser criar um ficheiro para mais tarde criar uma maquina com as mesmas bibliotecas

    pip freeze > requirements.txt

na outra "maquina"

    pip install -r requirements.txt


## Models 

### Flask SQLAlchemy
    pip install flask-sqlalchemy


### Migrações

### Flask Script

    pip install flask-script


### Flask Migrate

    pip install flask-migrate

> Para executar a app

    python run.py runserver

> Creates a new migration repository
 
    py .\run.py  db init

> Alias for 'revision --autogenerate'

    py .\run.py db migrate

### Flask WTF - formulários

     pip install flask-wtf

### Flask Login

    pip install flask-login