# Housing Rental Analysis for San Francisco

In this project, we delve into the San Francisco housing market to discover lucrative property investment opportunities. Using Python's data science and visualization libraries, including Pandas, hvPlot, and GeoViews, we successfully navigate through a plethora of housing data, apply aggregation, and create interactive and geospatial visualizations.

## Technology Stack

This project relies heavily on the following Python libraries and tools:

* **Jupyter Notebook**: This open-source web application allows creation and sharing of documents containing live code, equations, visualizations and narrative text.
* **Pandas**: This library offers data structures and operations for manipulating numerical tables and time series.
* **hvPlot**: A high-level plotting API for the PyData ecosystem built on HoloViews.
* **GeoViews**: This library makes it easy to explore and visualize geographical, meteorological, and oceanographic datasets, such as the GeoDataFrame we are using for this project.

## Project Overview

First, I load the dataset **'sfo_neighborhoods_census_data.csv'** from the **'Resources'** folder into a Pandas DataFrame for ease of manipulation and analysis.

With this dataset, I calculate and plot the average number of housing units per year. I group the data by year and use the mean to aggregate it. Using hvPlot, I create a bar chart to visualize this trend. Through my visualization, I draw insights about the overall progression of housing units over the period analyzed.

Next, I proceed to calculate and plot the average sale prices per square foot over time. By grouping the data by year, I derive the average prices and lowest gross rent for the years covered in the dataset. I create another DataFrame, **prices_square_foot_by_year**, and visualize the data with hvPlot to create a line plot. This visualization reveals any potential drops in the average sale price per square foot and how the gross rent may have changed during those years.

I then compare the average sale prices by neighborhood, creating an interactive line plot that allows me to explore the average sale price per square foot and gross rent. With this interactive tool, I'm able to examine neighborhood-specific trends such as the change in the average sale price per square foot in the Anza Vista neighborhood from 2012 to 2016.

For the geospatial analysis, I build an interactive neighborhood map using the **sfo_data_df** DataFrame, which contains neighborhood location data along with average prices. I read in the **'neighborhood_coordinates.csv'** file from the **'Resources'** folder to create the **neighborhood_locations_df** DataFrame. Combining these data, I create a points plot for the **all_neighborhoods_df** DataFrame using hvPlot with GeoViews enabled, displaying neighborhoods color-coded by gross rent and sized by sale price per square foot. This interactive map allows me to identify which neighborhood has the highest gross rent and the highest sale price per square foot.

Finally, I use the visualizations created in the project to compose a narrative, detailing the trend comparison between rental income growth and sales prices, and the viability of the company's one-click, buy-and-rent strategy.