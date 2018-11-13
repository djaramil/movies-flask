from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from movies import *
import os

port = int(os.getenv('PORT', 8000))


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
        return render_template('movies_by_category.html', content=allCategories)

    @app.route('/year')
    def moviesByYear():
        allMoviesByYear = list_movies_by_all_year()
        return render_template('movies_by_year.html', content=allMoviesByYear)

    @app.route('/addMovie', methods=['POST', 'GET'])
    def addMovie():
        all_categories = list_all_category()
        if request.method == "POST":
            movie_name = request.form['movieName']
            category_id = request.form['movieCategory']
            movie_year = request.form['movieYear']
            movie_minutes = request.form['movieMinutes']
            print movie_name
            print category_id
            print movie_year
            print movie_minutes
            add_movie(movie_name, movie_year, movie_minutes, category_id)
            message = "Movie successfully added " + movie_name
            # flash(message, "info")
            return render_template('index.html',message=message)
        return render_template('add_movie.html', content=all_categories)

    @app.route('/deleteMovie')
    def deleteMovie():
        all_categories = list_movies_by_all_category()
        return render_template('delete_movie.html', content=all_categories)

    @app.route('/deleteMovieWithId')
    def deleteMovieWithId():
        movie_id_to_delete = request.args.get("movieId")
        delete_movie(movie_id_to_delete)
        all_categories = list_movies_by_all_category()
        return render_template('delete_movie.html', content=all_categories)

    return app


# create an app instance
app = create_app()

app.run(host='0.0.0.0', port=port, debug=True)
