from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import read_csv
import pandas as pd

from pandas import Series, DataFrame

def question_1(data):
    data_permit_type_num = data[['X', 'Y', 'PERMIT_NUMBER']]
    data_group_by = data_permit_type_num.groupby(['X', 'Y']).count()

    #print data_group_by
    size = data_group_by.iloc[:, 0].size
    lngs = []
    lats = []
    cons = []
    for i in range(size):
        lngs.append(data_group_by.iloc[i].name[0])
        lats.append(data_group_by.iloc[i].name[1])
        cons.append(data_group_by.iloc[i].PERMIT_NUMBER / 15)
    lngs = Series(lngs)
    lats = Series(lats)
    cons = Series(cons)

    #earth = Basemap(projection='hammer', lon_0 = 10, lat_0 = 50, ax=ax0)
    earth = Basemap()
    # 105.3,-13.9,151.6,22.1 Phillipines
    # earth = Basemap(llcrnrlon=105.3,llcrnrlat=-13.9,urcrnrlon=151.6,urcrnrlat=22.1)
    earth.drawcoastlines(color='0.50', linewidth=0.25)
    # earth.fillcontinents(color='0.95')
    # earth.bluemarble(alpha=0.95)
    earth.shadedrelief()
    plt.scatter(lngs, lats, cons,
                c='blue', alpha=0.5, zorder=10)

# data = read_csv('Building_Permits.csv')
# style.use(['seaborn-poster'])
# fig = plt.figure()
#
# ax_1 = fig.add_subplot(111)
# #ax_1.set_title("Question 1")
# question_1(data)
# plt.show()