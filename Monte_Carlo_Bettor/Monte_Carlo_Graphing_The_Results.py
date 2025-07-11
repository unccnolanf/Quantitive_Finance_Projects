import matplotlib
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D


# This short code aids in graphing 3 variables to find correlation in ROI loss or gain
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def graph():
    with open('monteCarloLiberal.csv','r') as montecarlo:
        datas = csv.reader(montecarlo,delimiter=',')

        #Defining variables to graph
        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagersizepercentage = float(eachLine[1])
            wagercount = float(eachLine[2])
            pcolor = eachLine[3]

            ax.scatter(wagersizepercentage,wagercount,percentROI,color=pcolor)

            #Labeling variables for reader ease
            ax.set_xlabel('wager size percentage')
            ax.set_ylabel('wager count')
            ax.set_zlabel('percentROI')

        plt.show()

graph()