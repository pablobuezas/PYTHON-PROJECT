<h1>Project of the First Semester Fundamentals of Programming (Curso <22>/<23>)</h1>

Author: Pablo Buezas Humanes; uvus:pabbuehum

Houses prices in California.

<p>This project is based on the houses prices in California, the project analyzes the house prices data published in 
this Kaggle dataset (https://www.kaggle.com/datasets/ahmedzaky01/housing?select=housing.csv). The dataset has 10 columns.</p>

<h2>Structure of the project´s folders</h2>
 
<ul>
<li><p><strong>src</strong>: Contain different Python´s modules that form the project.<br></li>
<ul>
<li>housing.py: <br></li>
<li>housing_test.py: </p></li>
</ul>
<li><p><strong>data</strong>: Contain the dataset of the project.<br></li>
<ul>
<li>housing.csv </p></li>
</ul>
</ul>
  

<h2>Structure of the datset</h2>

<p>Each row of the dataset collects data for the houses. For each house, 10 pieces of data are recorded. Therefore, the dataset is composed of 10 columns, with the following description: </p>

<p>
<ul>
<li><strong>longitude</strong>: of type float, represents the longitude where the house is located. <br></li>
<li><strong>latitude</strong>: of type float, represents the latitude where the house is located. <br></li>
<li><strong>housing_median_age</strong>: of type int, represents the age of the owners of the houses. <br></li>
<li><strong>total_rooms</strong>: of type int, represents the number of rooms. <br></li>
<li><strong>total_bedrooms</strong>: of type int, represents the number of bedrooms. <br></li>
<li><strong>population</strong>: of type int, represents the number of population. <br></li></li>
<li><strong>households</strong>: of type int, represents the number of households. <br></li>
<li><strong>median_income</strong>: of type float, represents the average household income rates fluctuate. <br></li>
<li><strong>median_house_value</strong>: of type int, represents the value of the houses. <br></li>
<li><strong>ocean_proximity</strong>: of type str, represents the proximity to the ocean. </li>
</ul>
</p>


<h2>Implemented types</h2>
 
<p>To work with the data in the dataset, the following named tuple has been defined: </p>

<p>Info = namedtuple( "Info","longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, median_house_value, ocean_proximity") </p>

<p>Where the types of each of the fields are as follows: </p>

<p>Info(float, float, int, int, int, int, int, float, int, str) </p>
 
 
<h2>Implemented functions</h2>

<p>The following functions have been implemented in this project, which are classified according to the blocks and types of functions required in each of the deliverables. The main module is the housing.py module, so this is where each of the blocks of the deliverables will be referred to. </p>

<p><h3>housing module.</h3> </p>
 
<ul>
<li><p><strong>lee_fichero(fichero)</strong>: reads the data from the csv file and returns a list of Info type tuples with the data from the file. </p> </li>
</ul>
 
 
<p><h3>housing_test module.</h3> </p>
 
<p>The following test function has been defined in the test module, which is used to test the function with the same name. For example, the function test_lee_fichero tests the function lee_fichero. </p>

<ul>
<li><p><strong>test_lee_fichero(fichero)</strong> </p></li>
</ul>
 
 
