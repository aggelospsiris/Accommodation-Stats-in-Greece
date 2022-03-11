from codes.csv_cut_into_dict import dict5,dict6
import matplotlib.pyplot as plt
import numpy as np


#delete the name of country which is unseccery for the graphs
del dict5['Country']
del dict6['Country']

#key and val of the dictionaries converted to int
for key in dict5:
        dict5[key] = int(dict5[key])
for key in dict6:
        dict6[key] = int(dict6[key])
for val in dict5:
        dict5[val] = int(dict5[val])
for val in dict6:
        dict6[val] = int(dict6[val])

years = [2008,2009,2010,2011]
gr_numbers = [dict5.get('2008 '),dict5.get('2009 '),dict5.get('2010 '),dict5.get('2011 ')]
spain_numbers = [dict6.get('2008 '),dict6.get('2009 '),dict6.get('2010 '),dict6.get('2011 ')]

x = np.arange(len(years))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gr_numbers, width, label='Greece')
rects2 = ax.bar(x + width/2, spain_numbers, width, label='Spain')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of arrivals')
ax.set_xlabel('Year')
ax.set_title('Arrivals at tourist accommodation establishments')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()