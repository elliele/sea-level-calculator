import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')


    # Create scatter plot
    ax1 = df.plot.scatter(x='Year',
                      y='CSIRO Adjusted Sea Level')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_x = np.arange(df['Year'].min(), 2050)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y, 'r')

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.scatter(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    line_x = np.arange(df_2000['Year'].min(), 2050)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y, 'r')



    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()