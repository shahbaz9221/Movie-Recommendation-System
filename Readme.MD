# Movie Recommendation System Documentation

## Introduction

The Movie Recommendation System is a Python script that provides two types of movie recommendation algorithms: Item-Based Recommendation and User-Based Recommendation. This system is designed to help users discover movies or users that are similar to their preferences, based on movie ratings and user interactions.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To use the Movie Recommendation System, you need to have the following Python libraries installed:

- Pandas
- NumPy

## Getting Started

1. **Download the Movie Dataset**: Obtain a dataset containing the following CSV files:
   - `movies.dat`: Movie data with columns MovieId, Title, and Genre.
   - `users.dat`: User data.
   - `ratings.dat`: Ratings data with columns UserId, MovieId, Rating, and Timestamp.

2. **Dataset Structure**: Ensure that the CSV files are organized within a directory named "Movie_Dataset." This directory should be located in the same directory as the script.

3. **Running the Script**: Open a terminal or command prompt and navigate to the directory where the script is located. Run the script using the following command:

   ```bash
   python your_script_name.py

## Usage

Upon running the script, you will be presented with the following options:

### Item-Based Recommendation System

This system recommends movies similar to a selected movie.

1. Enter `1` when prompted to select this option.
2. You will be asked to enter the title of the movie for which you want recommendations.

### User-Based Recommendation System

This system recommends users who are similar to a selected user.

1. Enter `2` when prompted to select this option.
2. You will be asked to enter the user ID for which you want to find similar users.

### Exit

To exit the program, simply enter `0` when prompted.

## Features

### Item-Based Recommendation

- Provides movie recommendations based on the similarity to a selected movie.
- Recommends movies that users who liked the selected movie also liked.

### User-Based Recommendation

- Recommends users who are similar to a selected user based on their movie preferences.
- Suggests users who have rated movies similarly to the selected user.

## Examples

Here are a few examples of how to use the Movie Recommendation System:

1. To get recommendations for a movie:
   - Select "Item-Based Recommendation System" by entering `1`.
   - Enter the title of the movie you want recommendations for.

2. To find similar users:
   - Select "User-Based Recommendation System" by entering `2`.
   - Enter the user ID for which you want to find similar users.

3. To exit the program, enter `0` at any time.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request to the original repository.

Happy recommending and happy contributing! 🍿🎬


