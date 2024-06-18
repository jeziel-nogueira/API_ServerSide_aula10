Instalaçao das bibliotecas:
* pip install Flask
* pip install Flask-SQLAlchemy
* pip install pyjwt
* pip install Flask-Migrate

  #
Executando comandos e rodando a aplicação:
* Inicializa o banco:<br>
 flask db init
   
 
* Migra a aplicação para o banco: <br>
  flask db migrate

* SEMPRE realizar em caso de alteração no db <br>
  flask db upgrade

* Executa a aplicação na porta 5000 <br>
  flask run
