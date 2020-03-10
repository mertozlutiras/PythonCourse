import numpy as np
import matplotlib.pyplot as pyplot
import math

# Function to get alpha and beta values of simple linear regression
def regress(xList, yList):

    # Transform xList & yList to numpy arrays
    x = np.array(xList)
    y = np.array(yList)

    # N equals the number of observations
    n = np.size(x)

    # Means and standard deviations are calculated
    xBar = np.mean(x)
    yBar = np.mean(y)
    SSxy = np.sum(y*x) - n*yBar*xBar
    SSxx = np.sum(x*x) - n*xBar*xBar

    # Regression coefficients are calculated with the help of formula
    beta = SSxy/SSxx
    alpha = yBar - beta*xBar

    # Estimated y values are calculated
    yEstimate = alpha + beta*x

    # Beta regression standard error is calculated
    stdErrorSquared = np.sum(np.square(yEstimate - y)) / ((n-2)*np.sum(np.square(x - xBar)))
    standardError = math.sqrt(stdErrorSquared)

    # 95% Confidence Interval is calculated for beta
    lowerBound = beta - 1.96*standardError
    upperBound = beta + 1.96*standardError

    return (alpha, beta, standardError, lowerBound, upperBound)

# Regression is plotted
def plotRegressionGraph(xList, yList, alpha, beta):
    # Plot the data points
    x = np.array(xList)
    y = np.array(yList)
    pyplot.scatter(x, y, color = "r", marker = "o", s = 30)
    # Get the estimated values
    yEstimate = alpha + beta*x
    # Plot the regression line
    pyplot.plot(x, yEstimate, color = "b")
    pyplot.xlabel('GDP Per Capita (Current US$)')
    pyplot.ylabel('Urban population (% of total)')
    pyplot.show()
