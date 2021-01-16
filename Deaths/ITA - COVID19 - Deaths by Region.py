#!/usr/bin/env python
# coding: utf-8

# Import libraries and last updated data from *Protezione civile* (see [pcm-dpc](https://github.com/pcm-dpc/COVID-19)):

# In[48]:


from urllib.request import urlopen
import pandas as pd
import json
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")


# Check DataFrame:

# In[49]:


df.head()


# Consider **P.A. Trento** and **P.A. Bolzano** as standard code 4 (i.e. *Trentino Alto Adige*).

# In[50]:


df.loc[df['codice_regione'] >= 21,'codice_regione'] = 4


# Drop not used column and rename *Region* and *Deaths* columns:

# In[51]:


df.drop(columns=['stato','lat', 'long'], axis=1, inplace=True)
df = df[df['denominazione_regione'] != 'In fase di definizione/aggiornamento']
df = df.rename(columns={'codice_regione': 'Region'})
df = df.rename(columns={'deceduti': 'Deaths'})
df['Date'] = pd.to_datetime(df['data'], format="%Y-%m-%d")
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')


# Print map using geojson Italy region file ([openpolis](https://github.com/openpolis/geojson-italy)):

# In[52]:


fig = px.choropleth(df, 
    geojson='https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson', 
    locations='Region', color='Deaths', color_continuous_scale='Greys', 
    featureidkey='properties.reg_istat_code_num', animation_frame='Date', 
    range_color=(0, max(df['Deaths'])))
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_geos(fitbounds="locations", visible=False)
fig.write_html('Deaths_by_region_time_frame.html')
fig.show()


# Sum all deaths from the covid-19 start date:

# In[53]:


fig = px.choropleth(df, 
    geojson='https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson', 
    locations='Region', color='Deaths', color_continuous_scale='Greys', 
    featureidkey='properties.reg_istat_code_num',
    range_color=(0, max(df['Deaths'])))
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.update_geos(fitbounds="locations", visible=False)
fig.write_html('Total_deaths_by_region.html')
fig.show()

