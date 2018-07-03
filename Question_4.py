from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import read_csv
import pandas as pd
import squarify

def question_4(data):

    #data['ESTIMATED_VALUE_OF_PROJECT'] = data['ESTIMATED_VALUE_OF_PROJECT'].astype(np.int64)
    total_value = data['ESTIMATED_VALUE_OF_PROJECT'].count()
    print total_value
    print "=========="
    data_4 = data[['ALTERNATE_BUILDING_TYPE', 'ESTIMATED_VALUE_OF_PROJECT']]

    data_4 = data_4.groupby(['ALTERNATE_BUILDING_TYPE']).filter(
        lambda x: x['ESTIMATED_VALUE_OF_PROJECT'].count() > 0
    )

    data_4 = data_4.groupby(['ALTERNATE_BUILDING_TYPE'])['ESTIMATED_VALUE_OF_PROJECT'].agg(['count'])
    data_4 = data_4['count'].sort_values(ascending=False)
    print data_4

    labels = data_4.head(5).keys().values
    squarify.plot(sizes=data_4.values, label=labels, alpha=.7)
    plt.axis('off')



# data = read_csv('Building_Permits.csv')
# question_4(data)
# plt.show()






