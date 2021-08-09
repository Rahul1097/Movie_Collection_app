#Movie Collection App
from tabulate import tabulate

movies=[]
MENU_PROMPT = "1.Enter 'a' to add a movie.\n2.Enter 'l' to see your movies.\n3.Enter 'f' to find a movie by title.\n4.Enter 'r' to remove movie from collection.\n5.Enter 'q' to quit.\n"

def add_movie():
    title = input("Enter the movie title: ").lower().strip()
    director = input("Enter the movie director: ").lower().strip()
    year = input("Enter the movie release year: ").lower().strip()

    for index in range(len(movies)):
        if movies[index]['title'] == title:
            print("Movie is already present in collection.")
            break
    else:
        movies.append({
            'title':title,
            'director':director,
            'year':year
        })

def show_movies():
    if movies == []:
        print("Sorry! No movies in your collection.")
    else:
        print_movie(movies)

def print_movie(movies):
    movie_list = []
    for movie in movies:
        movie_list.append([movie['title'].title(),movie['director'].title(),movie['year'].title()])

    print("\n")
    print(tabulate(movie_list, headers=["Title", "Director", "Release year"]))
    print("\n")

def find_movie():
    search_title = input("Enter the title of the moviw you want to search:").lower().strip()

    for movie in movies:
        if movie['title'] == search_title:
            print("Movie present in collection")
            found_movie = [movie]
            print_movie(found_movie)
            break
    else:
        print("Movie not present in collection.")


def remove_movie():
    search_title = input("Enter the title of the movie you want to remove:").lower().strip()

    for index in range(len(movies)):
        if movies[index]['title'] == search_title:
            del movies[index]
            print("Movie successfully removed from collection")
            break
    else:
        print("Movie not present in collection.")

user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie,
    "r": remove_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection !='q':
        if selection in user_options:
            selection_function = user_options[selection]
            selection_function()
        else:
            print('Unknown command. Please try again.')
    
        selection = input(MENU_PROMPT)

menu()