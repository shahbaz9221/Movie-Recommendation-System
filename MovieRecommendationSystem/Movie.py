import numpy as np
import pandas as pd
import time

movies_data=pd.read_csv('Movie_Dataset/movies.dat',sep='::',names=['MovieId','Title','Genere'])
users_data=pd.read_csv('Movie_Dataset/users.dat',sep='::',header=None)
ratings_data=pd.read_csv('Movie_Dataset/ratings.dat',sep='::',names=['UserId','MovieId','Rating','timestamp'])


movies_data.column=['MovieId','Title','Genere']
movies=pd.merge(movies_data,ratings_data,on='MovieId')
n_users = movies.UserId.unique().shape[0]
n_items = movies.Title.unique().shape[0]
ratings = np.zeros((n_users, n_items))
movie_user = movies.pivot_table(index='UserId', columns='Title', values='Rating')
#print(moviemat.head())


print("\n\nThere are 2 Recommendation System")
print("  1: Item Base Recommendation System")
print("  2: User Base Recommendation System\n")
print("Press 1 for Item Base Recommendation ")
print("Press 2 for User Base Recommendation ")
x = int(input())


while x!=0:
    if x==1:
        
        selected_movie = movie_user['$1,000,000 Duck (1971)']
        movies_corelation = movie_user.corrwith(selected_movie)
        corr_DataFram = pd.DataFrame(movies_corelation, columns=['Correlation']) 
        print("\nFollowing movies are liked by most of the users who liked this movie")
        print("These movies are Recommended For You\n")
        print(corr_DataFram.sort_values('Correlation', ascending=False).head())
        
    else:
        
        movie_user_Transpose=movie_user.T
        selected_user=movie_user_Transpose[8]
        users_corelation = movie_user_Transpose.corrwith(selected_user)
        corr_User = pd.DataFrame(users_corelation, columns=['Correlation'])
        print("\nFollowing Users are similar to selected User")
        print(corr_User.sort_values('Correlation', ascending=False).head())
        
        
    print("\n\nPress 1 for Item Base Recommendation ")
    print("Press 2 for User Base Recommendation ")
    print("Press 0 To Exit")
    x = int(input())

print("Good Luck")
time.sleep(2)