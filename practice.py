import pandas as pd
import numpy as np

#read the files
frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')


#viewing files
print("rating_final file ")
print(frame.head(),'\n')
print("chefmozfinal file ")
print(cuisine.head(),"\n")

#groupby the column rating
rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
print("rating_count is")
print(rating_count.head(),"\n")

#arrange in descending order to get most popular restraunts
rating_count.sort_values('rating', ascending=False).head()




#sort the rating in descending order
print(rating_count.sort_values('rating',ascending = False ).head(),"\n")

most_rated_places = pd.DataFrame([135085,132825,135032,135052,132834],index=np.arange(5),columns = ['placeID'])

#merge the two files with placeId to get cuisine names
summary = pd.merge(most_rated_places,cuisine, on = 'placeID')
print(summary,"\n")

#observe the Rcuisine description
print("Rcuisine description")
print(cuisine['Rcuisine'].describe())
