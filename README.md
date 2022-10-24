<h2>Project of the First Semester Fundamentals of Programming (Curso <22>/<23>)</h2>

Author: Pablo Buezas Humanes; uvus:pabbuehum

Houses prices in California.

<p>This project is based on the houses prices in California, the project analyzes the house prices data published in 
this Kaggle dataset (https://www.kaggle.com/datasets/ahmedzaky01/housing?select=housing.csv). The dataset has 10 columns.

<h3>Structure of the project´s folders</h3>
src: Contain different Python´s modules that form the project.
<housing.py>: 
<housing_test.py>:
data: Contain the dataset of the project.
 housing.csv
  

<h3>Structure of the datset</h3>

Each row of the dataset collects data for the houses. For each house, 10 pieces of data are recorded. Therefore, the dataset is composed of 10 columns, with the following description:

longitude: of type float, represents the longitude where the house is located.
latitude: of type float, represents the latitude where the house is located.
housing_median_age: of type int, represents the age of the owners of the houses.
total_rooms: of type int, represents the number of rooms.
total_bedrooms: of type int, represents the number of bedrooms.
population: of type int, represents the number of population.
households: of type int, represents the number of households.
median_income: of type float, represents the average household income rates fluctuate.
median_house_value: of type int, represents the value of the houses.
ocean_proximity: of type str, represents the proximity to the ocean.


 <h3>Implemented types</h3>
 
To work with the data in the dataset, the following named tuple has been defined:

Info = namedtuple( "Info","longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value, ocean_proximity")

Where the types of each of the fields are as follows:

Info(float, float, int, int, int, int, int, float, int, str)
 
 
 <h3>Implemented functions</h3>

The following functions have been implemented in this project, which are classified according to the blocks and types of functions required in each of the deliverables. The main module is the housing.py module, so this is where each of the blocks of the deliverables will be referred to.

Housing module.
 
lee_fichero(fichero): reads the data from the csv file and returns a list of Info type tuples with the data from the file. 
 
 
