#!/usr/bin/env/python3

import db
from objects import Movie

def list_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    #for category in categories:
    #    print(str(category.id) + ". " + category.name)
    print(categories)
    return categories

def list_movies_by_all_category():
    db.connect()
    movies = db.get_movies_by_all_categories()
    return(movies)

def list_movies_by_category():
    category_id = int(input("Category ID: "))
    print()
    category = db.get_category(category_id)
    movies = db.get_movies_by_category(category_id)
    list_movies(movies, category.name.upper())
    
def list_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def list_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    list_movies(movies, str(year))

def list_movies_by_all_year():
    db.connect()
    movies = db.get_movies_by_all_year()
    return(movies)

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    movie = Movie(name=name, year=year, minutes=minutes,
                  category=category)
    db.add_movie(movie)    
    print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    db.delete_movie(movie_id)
    print("Movie ID " + str(movie_id) + " was deleted from database.\n")
        