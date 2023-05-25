## Fintech Challenge 10

This repository contains the Python Jupyter notebook for the Fintech Challenge 10. The challenge involves performing an analysis of cryptocurrency data to assemble investment portfolios. The tasks include finding the optimal number of clusters (k) using the elbow method, clustering the cryptocurrencies with K-Means, performing Principal Component Analysis (PCA) to optimize clusters, and visualizing and comparing results.

## Tools Used

Several Python libraries and tools are used to carry out the tasks in this challenge.

1. Pandas: The pandas library provides high-performance, easy-to-use data structures and data analysis tools. It is particularly suited for handling structured data, such as CSV files, SQL tables, or Excel spreadsheets.

`
import pandas as pd
`

2. hvPlot: hvPlot provides a high-level plotting API built on HoloViews that provides a general and consistent API for plotting data in different formats. It is used in this challenge to plot scatter plots and line charts for visual analysis.

`
import hvplot.pandas
`

3. Path from pathlib: The pathlib library is used for dealing with file paths in a more intuitive way. It provides a simple hierarchy of classes to handle filesystem paths.

`
from pathlib import Path
`

4. KMeans from sklearn.cluster: The KMeans algorithm from the sklearn.cluster module is used for clustering the cryptocurrencies based on their price changes. It aims to partition the data into k clusters in which each data point belongs to the cluster with the nearest mean.

`
from sklearn.cluster import KMeans
`

5. PCA from sklearn.decomposition: Principal Component Analysis (PCA) from the sklearn.decomposition module is used for reducing the dimensionality of the dataset.

`
from sklearn.decomposition import PCA
`

"6. StandardScaler from sklearn.preprocessing: The StandardScaler from the sklearn.preprocessing module is used for standardizing features by removing the mean and scaling to unit variance.

`
from sklearn.preprocessing import StandardScaler
`