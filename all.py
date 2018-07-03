from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import read_csv
import pandas as pd
from Question_2 import question_2
from Question_1 import question_1
from Question_3 import question_3
from Question_4 import question_4
from Question_5 import question_5


matplotlib.rcParams.update({'font.size': 1})

data = read_csv('Building_Permits.csv')
style.use(['seaborn-poster'])
fig = plt.figure()

ax_1 = fig.add_subplot(321)
#ax_1.set_title("Question 1")
question_1(data)

ax_2 = fig.add_subplot(322)
#ax_2.set_title("Question 2")
question_2(data)

ax_3 = fig.add_subplot(323)
#ax_3.set_title("Question 3")
question_3(data)

font = {'family': 'normal',
            'size': 7}
matplotlib.rc('font', **font)

ax_4 = fig.add_subplot(324)
question_4(data)

#matplotlib.rcParams.update({'font.size': 6})

# ax_5 = fig.add_subplot(325)
ax_5 = fig.add_subplot(3, 2, 5, projection='3d')
question_5(ax_5, data)


plt.show()