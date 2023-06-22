# ETF Analyzer Web Application

## Overview
The ETF Analyzer is a comprehensive financial web application developed to analyze and visualize the performance of a hypothetical Fintech Exchange Traded Fund (ETF). This ETF consists of four stocks: GOST, GS, PYPL, and SQ. The application focuses on performing in-depth analysis on these ETF stocks both individually and as a whole.

## Technologies
This application leverages a mix of robust technologies:

- **Python**: The primary programming language used for data analysis and manipulation.
- **SQL**: Used for querying and managing the financial data stored in a database.
- **Pandas**: A powerful data manipulation library used extensively in the application for the creation and manipulation of dataframes.
- **hvPlot**: A high-level plotting API for the PyData ecosystem built on HoloViews. In this application, it's used for creating interactive and professional styled visualizations.
- **Voilà**: This library transforms Jupyter notebooks into standalone web applications, enhancing the accessibility and user interaction with our findings.

## Application Details

### Analyzing Single Asset Performance
The application dives into the performance analysis of a single asset in the ETF, specifically PYPL. SQL queries in combination with Python and Pandas are used to fetch, frame, and analyze the PYPL data. This includes creating interactive visualizations using the hvPlot library to demonstrate daily and cumulative returns.

### Optimizing Data Access
Advanced SQL queries are leveraged to optimize data access, focusing on the retrieval of specific data subsets that satisfy certain conditions, such as closing prices higher than a certain threshold, and top daily return values. This enables precise, efficient, and relevant data analysis.

### ETF Portfolio Analysis
The application builds the entire ETF portfolio by combining all the individual asset data using SQL joins. It calculates the average daily returns for all assets in the portfolio to understand the portfolio's performance as a whole. This portfolio data is then used to compute annualized and cumulative returns, providing insight into long-term investment outcomes.

### Web Application Deployment
The ETF Analyzer application, developed in a Jupyter notebook, is deployed as a standalone web application using the Voilà library. This enhances accessibility and interactivity, allowing users to explore the ETF analysis findings interactively.


## Screenshots/Video
Visual representation of the deployed web application:

- [Screenshot 1](Screenshots/screenshot_1.png)
- [Screenshot 2](Screenshots/screenshot_2.png)

For a detailed analysis and in-depth understanding of the ETF portfolio, please refer to the `etf_analyzer.ipynb` notebook.
