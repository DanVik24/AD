#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Импортирт библиотек
import pandas as pd
import datetime as dt 
from scipy import stats as st 
import numpy as np 
import math as mth 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import folium
from folium import Map, Choropleth 
from folium import Map, Marker 
from folium.plugins import MarkerCluster 


# In[2]:


# импортируем библиотеки
import pandas as pd
from sqlalchemy import create_engine

db_config = {'user': 'praktikum_student', # имя пользователя
            'pwd': 'Sdf4$2;d-d30pp', # пароль
            'host': 'rc1b-wcoijxj3yxfsf3fs.mdb.yandexcloud.net',
            'port': 6432, # порт подключения
            'db': 'data-analyst-zen-project-db'} # название базы данных

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                db_config['pwd'],
                                                db_config['host'],
                                                db_config['port'],
                                                db_config['db'])

engine = create_engine(connection_string)


# In[ ]:




