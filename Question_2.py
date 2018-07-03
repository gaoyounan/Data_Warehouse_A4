from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import read_csv


def question_2(data):
    data_permit_type_num = data[['PERMIT_TYPE', 'PERMIT_NUMBER']]
    data_group_by = data_permit_type_num.groupby(['PERMIT_TYPE'])
    result = data_group_by.count()

    size = result.iloc[:, 0].size
    permit_type = []
    count_permit = []
    for i in range(size):
        temp = result.iloc[i]
        permit_type.append(result.iloc[i].name)
        count_permit.append(result.iloc[i].PERMIT_NUMBER)

    x = np.arange(size)
    plt.bar(x, count_permit)
    plt.xticks(x, permit_type, fontsize=6)
    plt.yticks(fontsize=6)


# data = read_csv('Building_Permits.csv')
#
# fig, axes = plt.subplots(nrows=2, ncols=2)
# ax0, ax1, ax2, ax3 = axes.flatten()
#
# question_2(data)
# fig.tight_layout()
# plt.show()




