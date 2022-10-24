import csv
from collections import namedtuple
from datetime import datetime


Info = namedtuple( "Info","longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value, ocean_proximity")

def lee_fichero(fichero):
    with open(fichero, encoding = "utf-8") as f:

        lector = csv.reader
        next(lector)
        res = []
        for longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value, ocean_proximity in lector :
            
            tuple = Info(float(longitude), float(latitude), int(housing_median_age), int(total_rooms), int(total_bedrooms), int(population), int(households), float(median_income), int(median_house_value), str(ocean_proximity))
            
            res.append(tuple)
    
    return(res)

