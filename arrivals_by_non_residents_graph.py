from codes.csv_cut_into_dict import dict7,dict8
import matplotlib.pyplot as plt
import numpy as np

#delete the name of country which is unseccery for the graphs
del dict7['Country']
del dict8['Country']

#key and val of the dictionaries converted to int
for key in dict7:
        dict7[key] = dict7[key]
for key in dict8:
        dict8[key] = dict8[key]
for val in dict7:
        dict7[val] = dict7[val]
for val in dict8:
        dict8[val] = dict8[val]

years = [2008,2009,2010,2011]
gr_numbers = [dict7.get('2008 '),dict7.get('2009 '),dict7.get('2010 '),dict7.get('2011 ')]
spain_numbers = [dict8.get('2008 '),dict8.get('2009 '),dict8.get('2010 '),dict8.get('2011 ')]

x = np.arange(len(years))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gr_numbers, width, label='Greece')
rects2 = ax.bar(x + width/2, spain_numbers, width, label='Spain')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of arrivals')
ax.set_xlabel('Year')
ax.set_title('Arrivals at tourist accommodation establishments by non residents')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

