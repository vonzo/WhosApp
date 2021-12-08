# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:54:46 2021

@author: vanch
"""

import argparse
import FileToDataFrame as ftd
import matplotlib.pyplot  as plt


def getTopMsgs(people_name, data_frame):
    top_list = []
    col_map = plt.get_cmap('Paired')
    for name in people_name:
        tmp_df_by_name = data_frame.loc[data_frame.Name == name]
        index = tmp_df_by_name.index
        number_of_rows = len(index)
        top_list.append([name, number_of_rows])
    ordered_list = sorted(top_list,key=lambda l:l[1], reverse=True)
    names_ordered, msgs = zip(*ordered_list)
    plt.figure(figsize=[14, 7])
    plt.bar(names_ordered, msgs, width=0.8, color=col_map.colors, edgecolor='k', 
        linewidth=2)
    
    plt.savefig('Top_Bars.png')
    print(*ordered_list, sep = "\n")
    
def plotMsgsPerDayPerPerson(people_name, data_frame):
    first = True
    plt.figure()
    for name in people_name:
        data_frame[name] = data_frame['Name'].eq(name).cumsum()
        if first:
            plt.figure();
            msg_cnt_x = data_frame[name].plot()
            first = False
        else:
            data_frame[name].plot(ax=msg_cnt_x)
            
    msg_cnt_x.legend(people_name);
    fig = msg_cnt_x.get_figure()
    fig.savefig('msgCountPerPerson.png')
    
def plotMsgsPerDay(data_frame):
    plt.figure()
    messages_per_day = data.groupby([data.index.year,data.index.month,data.index.day]).agg('count')
    messages_per_day.Msg.plot()
    
def plotTotalMsgs(people_name, data_frame):
    plt.figure()
    data_frame["Total"] = 0
    for name in people_name:
        data_frame["Total"] += data_frame[name]
    total_data_plot = data['Total'].plot()
    total_data_plot.legend("Total");
    fig = total_data_plot.get_figure()
    fig.savefig('TotalMngs.png')
    
def plotBarMsgsByMonth(data_frame):
    plt.figure();
    messages_per_month = data.groupby([data.index.year,data.index.month]).agg('count')
    monthly_plot = messages_per_month.Name.plot.bar()
    monthly_plot.legend("Grouped");
    fig2 = monthly_plot.get_figure()
    fig2.savefig('Monthly.png')
    

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='')
args = parser.parse_args()


print (args.filename)

#df = ftd.FileToDataFrame(args.filename)
df = ftd.FileToDataFrame("../../samples/Gunner.txt")
data = df.Df

data.set_index('Date', inplace =True) 

#Totals per person
people_name = data.Name.unique()
getTopMsgs(people_name, data)
plotMsgsPerDayPerPerson(people_name, data)

#Total Mesages per day
plotMsgsPerDay(data)
plotBarMsgsByMonth(data)

plotTotalMsgs(people_name, data)

from collections import Counter
mostCommonWords= Counter(" ".join(data["Msg"]).split()).most_common(100)
mostCommonCh = Counter(" ".join(data["Msg"])).most_common(10000)
    
