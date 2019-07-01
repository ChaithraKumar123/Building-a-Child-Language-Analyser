"""
Task 3: Visualise the statistics collected in Task 2
Author name :Chaithra Kumar 
Created Date :02-October -2018
Updated Date: 11-October -2018
Description of program :
Develop a visualization class to compare statistics of
SLI and TD group by implementing class in Task2
"""
# importing class Analyser
from Task2 import Analyser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Creating Class Statistics


class Statistics:

    """ Constructor __init__  to initial instance variable
            Instance Variables :
                self.analyser : data frame
                       data frame that contains all the statistics to be visualised

             Parameters :
                analyser : data frame
                    assign empty data frame with column names to the instance variable analyser


    """

    def __init__(self, analyser=pd.DataFrame(columns=['category', 'Length', 'vocab', 'Reps', 'Ret', 'error', 'pauses'])):
        self.analyser = analyser

    """
        compute_averages method to compute averages of two groups and store it in the list
        Return : list containing mean of two groups

    """

    def compute_averages(self):
        # list to contain mean of two groups
        list_mean = []
        # filter data of SLI category and calculating the mean of each statistics and append to the list
        df = self.analyser.query("category == 'SLI'")
        list_mean.append([np.mean(df['Length']), np.mean(df['vocab']), np.mean(df['Reps']), np.mean(df['Ret']),
                      np.mean(df['error']), np.mean(df['pauses'])])
        # filter data of TD category and calculating the mean of each statistics and append to the list
        df = self.analyser.query("category == 'TD'")
        list_mean.append([np.mean(df['Length']), np.mean(df['vocab']), np.mean(df['Reps']), np.mean(df['Ret']),
                      np.mean(df['error']), np.mean(df['pauses'])])
        return list_mean

    """
        visualise_statistics  method to construct bar graph to demonstrate the mean difference between the two groups 
        Return : None

    """

    def visualise_statistics(self):
        # list containing labels to plot bar graph
        labels = ['Average length', 'Average Size of Vocab', 'Average Repetition', 'Average Retracing', 'Average error',
                  'Average pauses']
        # store the computed averages of both graph and store it in the list
        list1 = self.compute_averages()
        # convert the list to data frame to plot the graph
        df = pd.DataFrame(np.array(list1[0]).reshape(6, 1), columns=list("a"))
        df1 = pd.DataFrame(np.array(list1[1]).reshape(6, 1), columns=list("b"))
        plt.figure(figsize=(10, 5))
        plt.bar(data=df, x=df.index, height='a', width=0.25,label='SLI')
        plt.bar(data=df1, x=df1.index+0.25, height='b', width=0.25, label='TD')
        plt.xticks(df.index+0.1, labels, size=6, rotation='horizontal')
        # assign label to each bar
        for i in range(6):
            if df.shape[0] != 0:
                plt.text(x=df.index[i]-0.1, y=df.iloc[i]+0.1, s=str(df.iloc[i]['a']), size=7)
            if df1.shape[0] != 0:
                plt.text(x=df1.index[i]+0.15, y=df1.iloc[i]+0.1, s=str(df1.iloc[i]['b']), size=7)
        plt.title("Visualization of SLI and TD Scripts Statistics")
        plt.xlabel("Statistics parameter")
        plt.ylabel("Average")
        plt.legend(loc='best')
        plt.show()

    # main function to construct objects of the class and visulaize the statistics


def main():
    list_vis = []
    path = 'SLI_Cleaned'
    if os.path.isdir(path):
        # iterate through SLI_Cleaned folder
        for filename in os.listdir(path):
                if filename == '.DS_Store':
                    continue
                obj = Analyser()
                obj.analyse_script(os.path.join(path, filename))
                # add instance variable of each SLI object to the list
                list_vis.append(['SLI', obj.length_trans, obj.size_vocab, obj.no_of_retracing, obj.no_of_rep, obj.no_of_error,
                              obj.no_of_pauses])
    else :
        print(path + " Not a directory")
    # iterate through TD Cleaned folder
    path = 'TD_Cleaned'
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if filename == '.DS_Store':
                continue
            obj = Analyser()
            obj.analyse_script(os.path.join(path, filename))
            # add instance variable of each TD object to the list
            list_vis.append(['TD', obj.length_trans, obj.size_vocab, obj.no_of_retracing, obj.no_of_rep, obj.no_of_error,
                          obj.no_of_pauses])
    else:
        print(path + " Not a directory")
    # convert the list to the data frame containing statics of all SLI and TD scripts
    df_stat = pd.DataFrame(list_vis, columns=['category', 'Length', 'vocab', 'Reps', 'Ret', 'error','pauses'])
    #  creating object of Statistics class
    s2 = Statistics()
    # assign the data frame constructed to the instance variable of class
    s2.analyser = df_stat
    print(s2.analyser)
    # call visualize method to plot the bar graph
    s2.visualise_statistics()



if __name__ == main():

    Statistics().main()


