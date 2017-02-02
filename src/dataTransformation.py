
# coding: utf-8

# import libraries
# this wont be necesary further on

import pickle
import pandas as pd
import numpy as np


#Load pickle from download and clean data

cleanData = pickle.load( open( "cleanData.p", "rb" ) )
cleanData.sort_values(by=['line','terminal','depart'],inplace=True)
cleanData.reset_index(drop=True, inplace=True)
cleanData.head()


#only dispatched trains
delayData = cleanData.loc[cleanData.dispached == 'S' ,['line','depart']].copy()
delayData['departLag'] = delayData.depart.shift(1)
delayData['delay'] = delayData.depart - delayData.departLag
delayData.head()




#create days of each depart, a variable stating wich delays are between diferent days, removing those delay times
delayData['departDay'] = delayData.depart.map(lambda x: x.day)
delayData['departLagDay'] = delayData.departLag.map(lambda x: x.day)
delayData['departDifferentDay'] = ~(delayData.departDay == delayData.departLagDay)
delayData.delay[delayData.departDifferentDay] = pd.NaT
delayData.drop(['departDay','departLag','departLagDay','departDifferentDay'], axis = 1 , inplace=True)



#remove outliers based on each line top 0.5%
delayData.groupby(by=delayData.line)
delayByLineOutliers = delayData.delay[~delayData.delay.isnull()].groupby(by=delayData.line).quantile(0.995)


delayDataA = delayData[delayData.line == 'A']
delayDataA.delay[delayDataA.delay > delayByLineOutliers['A']] =  pd.NaT

delayDataB = delayData[delayData.line == 'B']
delayDataB.delay[delayDataB.delay > delayByLineOutliers['B']] =  pd.NaT

delayDataC = delayData[delayData.line == 'C']
delayDataC.delay[delayDataC.delay > delayByLineOutliers['C']] =  pd.NaT

delayDataD = delayData[delayData.line == 'D']
delayDataD.delay[delayDataD.delay > delayByLineOutliers['D']] =  pd.NaT

delayDataE = delayData[delayData.line == 'E']
delayDataE.delay[delayDataE.delay > delayByLineOutliers['E']] =  pd.NaT

delayDataH = delayData[delayData.line == 'H']
delayDataH.delay[delayDataH.delay > delayByLineOutliers['H']] =  pd.NaT

delayDataP = delayData[delayData.line == 'P']
delayDataP.delay[delayDataP.delay > delayByLineOutliers['P']] =  pd.NaT


#Append in a full dataset

delayDataFinal = delayDataA.append(delayDataB)
delayDataFinal = delayDataFinal.append(delayDataC)
delayDataFinal = delayDataFinal.append(delayDataD)
delayDataFinal = delayDataFinal.append(delayDataE)
delayDataFinal = delayDataFinal.append(delayDataH)
delayDataFinal = delayDataFinal.append(delayDataP)
delayDataFinal.shape



#convert timedelta into integers en create a month category, remove unnecesary columns
delayDataFinal['delayInt'] = delayDataFinal.delay / np.timedelta64(1, 'm')
delayDataFinal['month'] = delayDataFinal.depart.map(lambda x: str(x.month) + '-' + str(x.year))
delayDataFinal['departHour'] = delayDataFinal.depart.map(lambda x: x.hour)
delayDataFinal.drop(['line','depart'], axis = 1 , inplace=True)




# Merge into subway final data
subwayData = pd.merge(cleanData,delayDataFinal,how='left',left_index=True, right_index=True)



# store data into pickle
pickle.dump(subwayData, open( "subwayData.p", "wb" ))








