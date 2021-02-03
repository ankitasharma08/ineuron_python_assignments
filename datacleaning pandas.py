import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

#1
Flight = []
for i in range(10045,10095,10):
          
        Flight.append(i)
Flight
df['Flight Number']= Flight
del df['FlightNumber']

#2
df[['From','To']] = df.From_To.str.split("_",expand=True)

#3
df['From'] = df['From'].str.capitalize()
df['To'] = df['To'].str.capitalize()

#4
del df['From_To']

#5
df[['delay_1','delay_2','delay_3']] = pd.DataFrame(df.RecentDelays.tolist(), index= df.index)
del df['RecentDelays']
df


