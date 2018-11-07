from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from movies import *


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
      allCategories = list_movies_by_all_category()
      return render_template('movies_by_category.html',content=allCategories)

  @app.route('/year')
  def moviesByYear():
      allMoviesByYear = list_movies_by_all_year()
      return render_template('movies_by_year.html',content=allMoviesByYear)

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
