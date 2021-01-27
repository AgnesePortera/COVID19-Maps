# COVID19-Maps

[![Python: 3.4](https://img.shields.io/badge/Python-3.4-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
![GitHub](https://img.shields.io/github/license/AgnesePortera/Covid19-Maps?style=plastic)

Analyses of covid-19  with Python choropleth maps.

## Covid-19 data
The DataFrame is updated from the github repository of **Dipartimento Protezione Civile** (see [pcm-dpc](https://github.com/pcm-dpc/COVID-19)).

## Geojson reference
The maps are done using geojson file from [openpolis](https://github.com/openpolis/geojson-italy).

## Project structure
### Deaths analysis
Under the folder "Deaths", there is the data analyses related to Italy regions.

The output file is an html file with Italy map gray scale colored depending on the covid-19 deaths number.
Moving the mouse on a region, a message will appear with numeric data.

![alt image](https://github.com/AgnesePortera/COVID19-Maps/blob/master/Deaths/ITA%20-%20Total%20Deaths%20by%20region.gif)

### Hospitals
Under the folder "Hospitals", there is the data analyses of ICU (Intensive Care Unit) related to Italy regions, as the previous section.

After that there is the ICU total analyses over time:

![alt image](https://github.com/AgnesePortera/COVID19-Maps/blob/master/Hospitals/ICU_date.gif)

It is used the `Cufflinks` library for `Plotly` integration on `Pandas`.
Also the interactive plot (`iplot`) shows information on hover and permits control on the plot look. 
