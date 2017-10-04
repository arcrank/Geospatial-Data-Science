# Geospatial Data Science
An overview of methods and tips for performing analysis, applying machine learning, and visualizing geospatial data
Geospatial data analysis is a vast and interesting domain that allows for locational based anaylsis.  There are many facets of what you can do, however this will focus more on how to quickly bootstrap and implement some forms of analysis and visualization.

Because this is for data science, it will cover how a data scientist could use these techniques, and we will use favorite libraries like pandas and related ones. 

Visualization is a key feature of geospatial data because it is inherent, a point representing a place on a map is semi meaningless without said map.  That being said, visualization for geospatial data encompasses a different m.o. than traditional methods (such as a graph) because you have to render the data on a map, and nowadays there exist ways to simply generate maps that are much easier to use and interact with (e.g. allow for zooming).
 
Some key features of what you should eventually be able to accomplish is getting and understanding how geospatial data is stored, analyzing geospatial data, analyzing meta data, and visualization.  

There are many modules and libraries available for these uses, this one uses a few key ones that can get your data up on a map within a matter of minutes, due to the dependencies for many of these modules, it is recommended that you use an anaconda build to interact with them

    folium
    geopandas
    pandas
    requests (for scraping)
    
    
## PART ONE: GETTING COORDINATES
**A simple method for translating data so that it can be ported to a map**

A fundamental aspect of geospatial data is a *geometry* , if you are at all familiar with GIS data this will not be something new to you, the geometry of an object is a way that information about its physical features can be stored easily in a table.  For simplicities sake there are only a few to be aware of, but we will touch on most of them later
-points
-polygons
-rasters

### To start, we will show you how to get coordinate representations for a location or address, and store it in a pandas dataframe.### 

Say you have a list of locations (representing something such as stores, crime spots, or bike racks),  we will be able to generate coordinates for them by webscraping google maps json API to pull coordinates.

    Get_coordinates.py
Has the key features and functions that we will need here. Make sure you have requests installed, and also a very useful parsing tool called [usaddress](https://github.com/datamade/usaddress).  Please note as of now this is only for US based locations.

Running the code
In order to run the code you need to input some sort of data file with addresses.  Load a file in as a dataframe or even create a test one that includes at least addresses.  

The main feature of this file is the function *get_coordinates(address)* .  Using the Usaddress module, we can take addresses that are imperfect or not even fully correct and it will usually parse out key components of the address into an ordered dict. The output also so happens to directly align with google maps geocoder, which we can access without the need for an API key by generating the URL for the address, and using requests to pull in the coordinate point.  

Running the script will iterate through your dataframe and then pull the coordinates for each address, two things of note here that will most likely sound familiar.  Pandas *hates* when you try to upload or update values in a dataframe, and we also need to make sure that if we cannot pull the address that it is properly noted.  We use numpy and nan to create a series of the dataframe length, and then iterate over the dataframe, updating values of the series at the correct dataframe index, and then once this is complete, appending the series to the dataframe, this avoids the major headaches that usually come with changing values in dataframes as you iterate over rows. 

    0 name1   1600 Pennsylvania Ave, Baltimore, MD 21217   {'lat': 39.3030243, 'lng': -76.6342229}   
    1  name2  1600 Pennsylvania Ave NW, Washington, DC 20500  {'lat': 38.8976633, 'lng': -77.0365739}


*That's it!* we have now translated non geospatial data into discrete point objects that can be represented on a map.  In the next section we will see how to visualize these items on a map.


