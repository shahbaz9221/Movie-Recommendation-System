import numpy as np
import pandas as pd
import time
import logging

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_movie_data():
    """
    Load movie data from the CSV file.
    Returns:
        movies_data (DataFrame): Movie data with columns: MovieId, Title, Genre.
    """
    movies_data = pd.read_csv('Movie_Dataset/movies.dat', sep='::', names=['MovieId', 'Title', 'Genre'])
    return movies_data

def load_user_data():
    """
    Load user data from the CSV file.
    Returns:
        users_data (DataFrame): User data with default columns.
    """
    users_data = pd.read_csv('Movie_Dataset/users.dat', sep='::', header=None)
    return users_data

def load_ratings_data():
    """
    Load ratings data from the CSV file.
    Returns:
        ratings_data (DataFrame): Ratings data with columns: UserId, MovieId, Rating, Timestamp.
    """
    ratings_data = pd.read_csv('Movie_Dataset/ratings.dat', sep='::', names=['UserId', 'MovieId', 'Rating', 'Timestamp'])
    return ratings_data

def main():
    movies_data = load_movie_data()
    users_data = load_user_data()
    ratings_data = load_ratings_data()

    # Corrected column name assignment
    movies_data.columns = ['MovieId', 'Title', 'Genre']

    # Merge movie and ratings data
    movies = pd.merge(movies_data, ratings_data, on='MovieId')

    n_users = movies['UserId'].nunique()
    n_items = movies['Title'].nunique()

    # Create a ratings matrix
    ratings = np.zeros((n_users, n_items))

    # Create a movie-user pivot table
    movie_user = movies.pivot_table(index='UserId', columns='Title', values='Rating')

    logging.info("There are 2 Recommendation Systems:")
    logging.info("  1: Item-Based Recommendation System")
    logging.info("  2: User-Based Recommendation System")

    while True:
        user_choice = int(input("Select an option (1 for Item-Based, 2 for User-Based, 0 to exit): ")
        if user_choice == 0:
            break
        elif user_choice == 1:
            selected_movie = movie_user['$1,000,000 Duck (1971)']
            movies_correlation = movie_user.corrwith(selected_movie)
            correlation_df = pd.DataFrame(movies_correlation, columns=['Correlation'])
            logging.info("Movies liked by users who liked the selected movie:")
            logging.info("Recommended movies for you:")
            logging.info(correlation_df.sort_values('Correlation', ascending=False).head())
        elif user_choice == 2:
            movie_user_transpose = movie_user.T
            selected_user = movie_user_transpose[8]
            users_correlation = movie_user_transpose.corrwith(selected_user)
            correlation_user = pd.DataFrame(users_correlation, columns=['Correlation'])
            logging.info("Users similar to the selected user:")
            logging.info(correlation_user.sort_values('Correlation', ascending=False).head())
        else:
            logging.error("Invalid option. Please select 1, 2, or 0 to exit.")

    logging.info("Good Luck")
    time.sleep(2)

if __name__ == '__main__':
    main()
