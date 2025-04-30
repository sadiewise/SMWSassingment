import pandas as pd
import numpy as np
import statistics 


# List of "Likes" values from the image
likes = [
    15430, 1450, 365, 672, 4875, 7749, 57200, 115786, 3751, 87632, 9823,
    11658, 3002, 9990, 96675, 36912, 290135, 81134, 220134, 1622, 31900,
    1360, 603, 562800, 68300, 809700, 26500, 33100, 85647, 331200, 1965,
    1446, 25300, 102000, 86200, 17300, 520300, 236700, 4836, 179500, 452,
    461400, 317, 21200, 761500, 17400, 29200, 111, 618, 4855
]

likes_series = pd.Series(likes)
total_likes = likes_series.sum()
total_likes


comments = [
    15436,132,148,249,376,2792,3510,854,604,1159,600,6960,285,624,2168,632,
    3614,2613,1988,51,2661,17,475,14900,23000,9053,279,6923,1109,6733,34,63,
    1093,385,897,179,5190,2355,4,2851,60,2601,15,196,14700,143,1671,15,169,322

]

comments_series = pd.Series(comments)
total_comments = comments_series.sum()
total_comments

favourites = [1836,262,
93,110,781,2687,19800,13100,688,16500,1357,1946,1222,1481,34300,5603,53421,25100,
20600,569,5806,196,83,58500,10500,91300,3214,2170,102036,151900,242,597,1695,12000,
23000,1542,22400,38500,835,30600,183,69900,163,3772,149500,1187,9651,52,92,2139

]

favourites = pd.Series(favourites)
total_favourites = favourites_series.sum()
total_favourites

quantities = [
    6,1,1,1,0,6,1,0,3,0,0,1,0,1,1,0,1,3,0,0,2,0,0,2,0,3,1,0,1,5,3,5,0,0,3,0,1,1,5,
    1,0,1,2,0,3,6,3,2,1,4

]
quantites_series = pd.Series(quantities)

# Calculate mode, median, and range
mode = quantities_series.mode().tolist()
median = quantities_series.median()
range_val = likes_series.max() - likes_series.min()
print(statistics.mean(quantities_series))

mode, median, range_val