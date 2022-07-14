from unittest import result
from Die import Die
import pygal

die=Die()
results=[]
for num in range(1000):
    result=die.roll()
    results.append(result)

frequencies=[]
for value in range(1,die.side+1):
    frequence=results.count(value)
    frequencies.append(frequence)

hist=pygal.Bar()
hist.title='result of rolling'
hist.xlabels=['1','2','3','4','5','6']
hist.x_title='result'
hist.y_title='Frequence'
hist.add('D6',frequencies)
#hist.render_to_file('die.svg')