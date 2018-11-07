from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from movies import *
from db import *


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  app.config['SECRET_KEY'] = 'devkey'

  @app.route('/', methods=('GET', 'POST'))

  @app.route('/index')
  def index():
      return render_template('index.html')

  @app.route('/category')
  def moviesByCategory():
      connect()
      allCategories = db.get_movies_by_all_categories()
      return render_template('movies_by_category.html',content=allCategories)

  @app.route('/year')
  def moviesByYear():
      return render_template('movies_by_year.html')

  @app.route('/addMovie')
  def addMovie():
      return render_template('add_movie.html')

  @app.route('/deleteMovie')
  def deleteMovie():
      return render_template('delete_movie.html')

  return app

# create an app instance
app = create_app()

app.run(debug=True)
