from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import squarify
from mpl_toolkits.mplot3d import Axes3D

def question_5(ax, data):
    #data['ESTIMATED_VALUE_OF_PROJECT'] = data['ESTIMATED_VALUE_OF_PROJECT'].astype(np.int64)

    data_5 = data[['ALTERNATE_BUILDING_TYPE', 'ESTIMATED_VALUE_OF_PROJECT', 'COMMUNITY']]
    data_5 = data_5[data_5['ALTERNATE_BUILDING_TYPE'].str.contains("COMMERCIAL", na=False)]
    #print data_5

    community = data_5[['COMMUNITY']]
    community = community.drop_duplicates()
    community_list = community['COMMUNITY'].values.tolist()

    building_type = data_5[['ALTERNATE_BUILDING_TYPE']]
    building_type = building_type.drop_duplicates()
    building_type_list = building_type['ALTERNATE_BUILDING_TYPE'].values.tolist()

    #print "======"

    data_5 = data_5.groupby(['ALTERNATE_BUILDING_TYPE','COMMUNITY']).filter(
        lambda x: x['ESTIMATED_VALUE_OF_PROJECT'].count() > 0
    )


    data_5 = data_5.groupby(['COMMUNITY', 'ALTERNATE_BUILDING_TYPE'])['ESTIMATED_VALUE_OF_PROJECT'].agg(['count'])
    data_5 = data_5['count']

    x = []
    y = []
    z = []

    size = data_5.size
    for i in range(size):
        community = data_5.keys()[i][0]
        type = data_5.keys()[i][1]
        value = data_5.values[i]
        x.append(community_list.index(community))
        y.append(building_type_list.index(type))
        z.append(value)

    print data_5

    ax.scatter(x, y, z, alpha=0.8, c="red", edgecolors='none')

    #plt.title('Matplot 3d scatter plot')
    plt.legend(loc=2)
    #plt.xticks(fontsize=6)
    plt.xticks(np.arange(len(community_list)), community_list, fontsize=4)
    #plt.yticks(fontsize=6)
    plt.yticks([0,1], building_type_list, fontsize=6)
    ax.set_xlabel('$X$', fontsize=6)
    ax.set_ylabel('$Y$', fontsize=6)
    ax.zaxis.set_rotate_label(False)
    ax.set_zlabel(r'$\gamma$', fontsize=6, rotation=0)




data = read_csv('Building_Permits.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

question_5(ax, data)
plt.show()




