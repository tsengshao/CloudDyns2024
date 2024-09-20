import numpy as np
import pandas as pd
import os, sys

datPath = '../../data/hw03/'

c = pd.read_csv(datPath+'no_2305_20210402_0559_L4.csv')
columns = ['P[hPa]', 'T[K]', 'Qv[g/kg]', 'U[m/s]', 'V[m/s]']
P = c['P']
p1000 = np.argmin(np.abs(P-1000))
p700  = np.argmin(np.abs(P-700))

def create_sounding_file(use_cols, foutname):
  df = c[use_cols].iloc[p1000:p700+1]
  df = df.set_axis(columns[:3],axis=1)
  df['T[K]'] += 273.15
  df[columns[3]] = np.zeros(df.shape[0])
  df[columns[4]] = np.zeros(df.shape[0])
  df.to_csv(datPath+foutname,sep='\t', index=False, float_format='%8.3f')
  

# raw data
use_cols = ['P','T','q']
create_sounding_file(use_cols, 'tainan_raw.txt')

# qc data
use_cols = ['P','T_new','q_new']
create_sounding_file(use_cols, 'tainan_QC.txt')

