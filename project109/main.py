import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('StudentsPerformance.csv')
scores = df['math score'].tolist

mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
stdev = statistics.stdev(scores)

print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Mode: {mode}')
print(f'Standard Deviation: {stdev}')

count = 0
for score in scores:
    if score > mean - stdev and score < mean + stdev:
        count += 1
perc = (count / len(scores))*100
print('1st Standard Deviation:', perc, '%')

count = 0
for score in scores:
    if score > mean - (stdev * 2) and score < mean + (stdev * 2):
        count += 1
perc2 = (count / len(scores))*100
print('2nd Standard Deviation:', perc2, '%')

count = 0
for score in scores:
    if score > mean - (stdev * 3) and score < mean + (stdev * 3):
        count += 1
perc3 = (count / len(scores))*100
print('3rd Standard Deviation:', perc3, '%')

fig = ff.create_distplot([scores], ['Math Scores'])
