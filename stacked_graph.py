
# coding: utf-8

# In[1]:


import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot ,plot_mpl
import matplotlib.pyplot as plt
from IPython.display import display, HTML, Image
import numpy as np
import pandas as pd

init_notebook_mode(connected=True)



# In[3]:


df = pd.read_csv('/home/deepak/files/emu_1.csv')


EMU_1 = FF.create_table(df.head())
py.iplot(EMU_1, filename='EMU_1')


# In[7]:


df1 = pd.read_csv('/home/deepak/files/emu_2.csv')


EMU_2 = FF.create_table(df1.head())
py.iplot(EMU_2, filename='EMU_2')


# In[6]:


df2 = pd.read_csv('/home/deepak/files/pec_1.csv')


PEC_1 = FF.create_table(df2.head())
py.iplot(PEC_1, filename='PEC_1')


# In[8]:


df3 = pd.read_csv('/home/deepak/files/pec_2.csv')


PEC_2 = FF.create_table(df3.head())
py.iplot(PEC_2, filename='PEC_2')


# In[9]:


df4 = pd.read_csv('/home/deepak/files/eec_1.csv')


EEC_1 = FF.create_table(df4.head())
py.iplot(EEC_1, filename='EEC_1')


# In[10]:


df5 = pd.read_csv('/home/deepak/files/pec_2.csv')


PEC_2 = FF.create_table(df5.head())
py.iplot(PEC_2, filename='PEC_2')


# In[72]:


trace0 = go.Scatter(
    x = df['Time'],
    y = df['WF'],
    name = 'WF-EMU_1',
    
)
trace1 = go.Scatter(
    x = df1['Time'],
    y = df1['WF'],
    name = 'WF-EMU_2',
   
)
trace2 = go.Scatter(
    x = df['Time'],
    y = df['MOP'],
    name = 'MOP-EMU_1',
    yaxis='y2'
)
trace3 = go.Scatter(
    x = df1['Time'],
    y = df1['MOP'],
    name = 'MOP-EMU_2',
    yaxis='y2'
)
trace4 = go.Scatter(
    x = df2['Time'],
    y = df2['CLA'],
    name = 'CLA-PEC_1',
    yaxis='y3'
    
)
trace5 = go.Scatter(
    x = df3['Time'],
    y = df3['CLA'],
    name = 'CLA-PEC_2',
    yaxis='y3'
   
)
trace6 = go.Scatter(
    x = df2['Time'],
    y = df2['BA'],
    name = 'BA-PEC_1',
    yaxis='y4'
    
)
trace7 = go.Scatter(
    x = df3['Time'],
    y = df3['BA'],
    name = 'BA-PEC_2',
    yaxis='y4'
   
)



# In[77]:


data = [trace0,trace1, trace2, trace3,trace4,trace5,trace6,trace7]
layout = go.Layout(title = 'Parameter_Comparison',
    xaxis=dict(title = 'time(secs)',color = ('rgb(205, 12, 24)')),       
    yaxis=dict(title = 'EMU_WF(lbs/hr)',
               side='right',
        
        color = ('rgb(205, 12, 24)'),
        
         domain=[0, 0.25]
    ),
     legend=dict(
        traceorder='normal'
    ),
    yaxis2=dict(title = 'MOP(psi)',
        color = ('rgb(205, 12, 24)'),
       
        domain=[0.25, 0.5]
    ),
         
    yaxis3=dict(title = 'CLA(deg)',
                side='right',
        color = ('rgb(205, 12, 24)'),
       
        domain=[0.5, 0.75]
    ),
    yaxis4=dict(title = 'BA(deg)',
                
        color = ('rgb(205, 12, 24)'),
       
        domain=[0.75, 1]
    ),
)
    

        


# In[80]:


fig = go.Figure(data=data, layout=layout)
config = {
    'showLink': False,
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': False
}

py.iplot(fig, config=config ,filename='stacked-subplots-shared-x-axis',image_width=800, image_height=600)

