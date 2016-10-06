
# coding: utf-8

#import libraries
import pandas as pd
import numpy as np
import pickle


# read raw data

rawData = pd.read_csv('trenes-despachados.csv', sep = ';')
rawData.head()


# drop unnecesary columns

rawData.drop(['FR1_REGIST','FR1_KM','FR1_KMV'], axis = 1, inplace = True)
rawData.head()


# rename remaining columns

rawData.columns = ['date','line','dayType','travelId','trainId',
                   'notDispach1','notDispach1Details','notDispach2','notDispach2Details',
                  'amountCars1','amountCars2','dispached1','dispached2',
                  'time1','time2']

# split data into two dataframes, one for each terminal

t1 = rawData.drop(['notDispach2','notDispach2Details','amountCars2','dispached2','time2'], axis = 1)
t1['terminal']=1

t2 = rawData.drop(['notDispach1','notDispach1Details','amountCars2','dispached1','time1'], axis = 1)
t2['terminal']=2

#remane columns
t1.columns = ['date','line','dayType','travelId','trainId','notDispach',
              'notDispachDetails','amountCars','dispached','time','terminal']
t2.columns = t1.columns 


# join by rows

cleanData = t1.append(t2,ignore_index=True).reindex()
cleanData.head()


# Create a depart timestamp

cleanData['depart'] = cleanData.date + ' ' + cleanData.time
cleanData.depart = pd.to_datetime(cleanData.depart, format='%d/%m/%Y %H:%M:%S')
cleanData.drop(['date','time'], axis = 1, inplace = True)


# store data into pickle

pickle.dump(cleanData, open( "cleanData.p", "wb" ))





