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
            # print movie_name
            # print category_id
            # print movie_year
            # print movie_minutes
            add_movie(movie_name, movie_year, movie_minutes, category_id)
            message = "Movie successfully added " + movie_name
            # flash(message, "info")
            return render_template('index.html',message=message)
        return render_template('add_movie.html', content=all_categories)

    @app.route('/editMovie', methods=['POST', 'GET'])
    def editMovie():
        movie_id_to_get = request.args.get("movieId")
        all_categories = list_all_category()
        if movie_id_to_get and movie_id_to_get != "": # Display edit form for movie when specified movie id
            movie_to_edit = get_movie_by_id(movie_id_to_get)
            return render_template('edit_movie.html', movie_to_edit=movie_to_edit, categories=all_categories)
        elif request.method != "POST":  # Display list of movies if movie id is not supplied
            movies_by_all_category = list_movies_by_all_category()
            return render_template('edit_movie_list.html', content=movies_by_all_category)
        elif request.method == "POST":  # Make actual update to movie details when submitted update request
            movie_id = request.form['movieId']
            movie_name = request.form['movieName']
            category_id = request.form['movieCategory']
            movie_year = request.form['movieYear']
            movie_minutes = request.form['movieMinutes']
            # print movie_id
            # print movie_name
            # print category_id
            # print movie_year
            # print movie_minutes
            edit_movie(movie_id, movie_name, movie_year, movie_minutes, category_id)
            message = "Movie successfully edited " + movie_name
            # flash(message, "info")
            return render_template('index.html', message=message)
        movies_by_all_category = list_movies_by_all_category()
        return render_template('edit_movie_list.html', content=movies_by_all_category)

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
