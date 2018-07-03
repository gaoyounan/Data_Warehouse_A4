from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def question_3(data):

    data['DATE_OF_APPLICATION'] = pd.to_datetime(data['DATE_OF_APPLICATION'])
    data['DATE_OF_PERMIT_ISSUANCE'] = pd.to_datetime(data['DATE_OF_PERMIT_ISSUANCE'])
    data['GAP'] = data['DATE_OF_PERMIT_ISSUANCE'] - data['DATE_OF_APPLICATION']
    data_3 = data[['DATE_OF_APPLICATION', 'DATE_OF_PERMIT_ISSUANCE', 'BP_ID', 'GAP']]
    data_3 = data_3.sort_values(by='GAP', ascending=False)
    data_3 = data_3.head(4)
    data_3['GAP'] = data_3['GAP'].astype('timedelta64[D]')

    x = np.arange(4)
    plt.plot(x, data_3['GAP'], 'o-')
    plt.xticks(x, data_3['BP_ID'], fontsize=6)
    plt.yticks(fontsize=6)



# data = read_csv('Building_Permits.csv')
# question_3(data)
# plt.show()





