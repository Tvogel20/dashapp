#how to deploy this app: https://dash.plotly.com/deployment
#https://www.youtube.com/watch?v=b-M2KQ6_bM4
#windows virtual env
#https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate
#libs
from gettext import install
#import requests
#import json
#import prettytable
import pandas as pd
import plotly
from matplotlib.pyplot import scatter
import plotly.graph_objects as go
import numpy as np
pd.options.plotting.backend ='plotly'
import plotly.io as pio
pio.templates.default = 'plotly_dark'

#Dash
from dash import Dash, html, dcc, dash_table
import plotly.express as px



#linear regression
#from sklearn.linear_model import LinearRegression
#import yfinance as yf

import matplotlib.pyplot as plt
#import seaborn as sbn# Configuring Matplotlib
import matplotlib as mpl





#load monthly data from FRED
today= pd.to_datetime('today').strftime('%Y-%m-%d')

#df_nber_mth = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=968&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PAYEMS,CE16OV,INDPRO,CMRMTSPL,W875RX1,PCEC96&scale=left,left,left,left,left,left&cosd=1968-05-25,1968-05-25,1968-05-25,1968-05-25,1968-05-25,2002-01-01&coed=2022-08-01,2022-08-01,2022-07-01,2022-06-01,2022-07-01,2022-07-01&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b,%233d96ae,%23db843d&link_values=false,false,false,false,false,false&line_style=solid,solid,solid,solid,solid,solid&mark_type=none,none,none,none,none,none&mw=3,3,3,3,3,3&lw=2,2,2,2,2,2&ost=-99999,-99999,-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999,99999,99999&mma=0,0,0,0,0,0&fml=a,a,a,a,a,a&fq=Monthly,Monthly,Monthly,Monthly,Monthly,Monthly&fam=avg,avg,avg,avg,avg,avg&fgst=lin,lin,lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4,5,6&transformation=lin,lin,lin,lin,lin,lin&vintage_date=2022-09-07,2022-09-07,2022-09-07,2022-09-07,2022-09-07,2022-09-07&revision_date=2022-09-07,2022-09-07,2022-09-07,2022-09-07,2022-09-07,2022-09-07&nd=1939-01-01,1948-01-01,1919-01-01,1967-01-01,1959-01-01,2002-01-01',
#                        na_values='.')
#reset date to today
df_nber_mth = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=968&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PAYEMS,CE16OV,INDPRO,CMRMTSPL,W875RX1,PCEC96&scale=left,left,left,left,left,left&cosd=1968-05-25,1968-05-25,1968-05-25,1968-05-25,1968-05-25,2002-01-01&coed={x},{x},{x},{x},{x},{x}&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b,%233d96ae,%23db843d&link_values=false,false,false,false,false,false&line_style=solid,solid,solid,solid,solid,solid&mark_type=none,none,none,none,none,none&mw=3,3,3,3,3,3&lw=2,2,2,2,2,2&ost=-99999,-99999,-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999,99999,99999&mma=0,0,0,0,0,0&fml=a,a,a,a,a,a&fq=Monthly,Monthly,Monthly,Monthly,Monthly,Monthly&fam=avg,avg,avg,avg,avg,avg&fgst=lin,lin,lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4,5,6&transformation=lin,lin,lin,lin,lin,lin&vintage_date={x},{x},{x},{x},{x},{x}&revision_date={x},{x},{x},{x},{x},{x}&nd=1939-01-01,1948-01-01,1919-01-01,1967-01-01,1959-01-01,2002-01-01'.format(x=today),
                        na_values='.')
df_nber_mth.set_index('DATE',inplace=True)

#monthly datasets

all_employees_tot_nonfarm = df_nber_mth['PAYEMS'] #All Employees: Total Nonfarm

"""
Units:  Thousands of Persons, Seasonally Adjusted


Frequency:  Monthly

All Employees: Total Nonfarm, commonly known as Total Nonfarm Payroll, is a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed. This measure accounts for approximately 80 percent of the workers who contribute to Gross Domestic Product (GDP).

Citation:
U.S. Bureau of Labor Statistics, All Employees, Total Nonfarm [PAYEMS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PAYEMS, September 10, 2022.
"""

employment_level = df_nber_mth['CE16OV'] #Employment Level

"""

Units:  Thousands of Persons, Seasonally Adjusted

Frequency:  Monthly

The civilian noninstitutional population is defined as: persons 16 years of age and older residing in the 50 states and the District of Columbia, who are not inmates of institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.

The series comes from the 'Current Population Survey (Household Survey)'

The source code is: LNS12000000

Citation:
U.S. Bureau of Labor Statistics, Employment Level [CE16OV], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CE16OV, September 10, 2022.

Nonfarm vs level: Nonfarm payroll reflects the short-term job market growth, while unemployment rate represents the long-term trend.
"""

industrial_production = df_nber_mth['INDPRO'] #Industrial Production Index: Total Index

"""
Units:  Index 2017=100, Seasonally Adjusted

Frequency:  Monthly

The industrial production (IP) index measures the real output of all relevant establishments located in the United States, regardless of their ownership, but not those located in U.S. territories.

For more information, see the explanatory notes issued by the Board of Governors. For recent updates, see the announcements issued by the Board of Governors

Source Code: IP.B50001.S

Citation:
Board of Governors of the Federal Reserve System (US), Industrial Production: Total Index [INDPRO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/INDPRO, September 10, 2022.
"""


real_manufacturing_sales = df_nber_mth['CMRMTSPL'] #Real Manufacturing and Trade Industries Sales

"""
Units:  Millions of Chained 2012 Dollars, Seasonally Adjusted

Frequency:  Monthly

Real Manufacturing and Trade Industries Sales (CMRMTSPL) was first constructed by the Federal Reserve Bank of St. Louis in June 2013. It is calculated using Real Manufacturing and Trade Industries Sales (HMRMT) (https://fred.stlouisfed.org/series/HMRMT) and Real Manufacturing and Trade Industries (CMRMT) (https://fred.stlouisfed.org/series/CMRMT).

Citation:
Federal Reserve Bank of St. Louis, Real Manufacturing and Trade Industries Sales [CMRMTSPL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CMRMTSPL, September 9, 2022.
"""

real_pers_income_ex_curr_transfer_receipts = df_nber_mth['W875RX1'] #Real personal income ex current transfer receipts

"""
Units:  Billions of Chained 2012 Dollars, Seasonally Adjusted Annual Rate

Frequency:  Monthly

BEA Account Code: W875RX
A Guide to the National Income and Product Accounts of the United States (NIPA) - (http://www.bea.gov/national/pdf/nipaguid.pdf)

Citation:
U.S. Bureau of Economic Analysis, Real personal income excluding current transfer receipts [W875RX1], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/W875RX1, September 9, 2022.
"""


real_pers_consumption_expenditures = df_nber_mth['PCEC96'] #Real personal consumption expenditures 

"""
Units:  Billions of Chained 2012 Dollars, Seasonally Adjusted Annual Rate

Frequency:  Monthly

BEA Account Code: DPCERX
A Guide to the National Income and Product Accounts of the United States (NIPA)

Citation:
U.S. Bureau of Economic Analysis, Real Personal Consumption Expenditures [PCEC96], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PCEC96, September 10, 2022.
"""

#load quarterly data from FRED, 

#df_nber_q = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=968&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1,A261RX1Q020SBEA&scale=left,left&cosd=1947-04-01,1947-04-01&coed=2022-04-01,2022-04-01&line_color=%234572a7,%23aa4643&link_values=false,false&line_style=solid,solid&mark_type=none,none&mw=3,3&lw=2,2&ost=-99999,-99999&oet=99999,99999&mma=0,0&fml=a,a&fq=Quarterly,Quarterly&fam=avg,avg&fgst=lin,lin&fgsnd=2020-02-01,2020-02-01&line_index=1,2&transformation=lin,lin&vintage_date=2022-09-07,2022-09-07&revision_date=2022-09-07,2022-09-07&nd=1947-01-01,1947-01-01')
#reset date to today
df_nber_q = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=968&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1,A261RX1Q020SBEA&scale=left,left&cosd=1947-04-01,1947-04-01&coed={x},{x}&line_color=%234572a7,%23aa4643&link_values=false,false&line_style=solid,solid&mark_type=none,none&mw=3,3&lw=2,2&ost=-99999,-99999&oet=99999,99999&mma=0,0&fml=a,a&fq=Quarterly,Quarterly&fam=avg,avg&fgst=lin,lin&fgsnd=2020-02-01,2020-02-01&line_index=1,2&transformation=lin,lin&vintage_date={x},{x}&revision_date={x},{x}&nd=1947-01-01,1947-01-01'.format(x=today))

df_nber_q.set_index('DATE',inplace=True)

#quarterly datasets
real_gdp = df_nber_q['GDPC1'] #Gross Domestic Product
real_gdi = df_nber_q['A261RX1Q020SBEA'] #Real Gross Domestic Income#load monthly data from FRED
#additons not great below as we delete last datapoint, quick fix
real_gdi = real_gdi.iloc[:-1]
real_gdi = real_gdi.astype(float)

housing_data = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1169&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=MSACSR,UNRATE&scale=left,left&cosd=1963-01-01,1961-07-15&coed={x},{x}&line_color=%234572a7,%23aa4643&link_values=false,false&line_style=solid,solid&mark_type=none,none&mw=3,3&lw=2,2&ost=-99999,-99999&oet=99999,99999&mma=0,0&fml=a,a&fq=Monthly,Monthly&fam=avg,avg&fgst=lin,lin&fgsnd=2020-02-01,2020-02-01&line_index=1,2&transformation=lin,lin&vintage_date={x},{x}&revision_date={x},{x}&nd=1963-01-01,1948-01-01'.format(x=today),
                           na_values='.')


#tab 2 datasets

#seasonally adjusted CPI data
df_cpi=pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=749&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCSL&scale=left&cosd=1947-01-01&coed={x}&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date={x}&revision_date={x}&nd=1947-01-01'.format(x=today))
df_cpi.set_index('DATE',inplace=True)
df_cpi['yoy_cpi']=df_cpi['CPIAUCSL'].pct_change(12)*100
cpi = df_cpi['CPIAUCSL'] 
#Yoy CPI SA data
yoy_cpi_series=df_cpi['yoy_cpi'].dropna()

#inflation expectiation data
inflation_expectation = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1169&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=MICH,EXPINF1YR&scale=left,left&cosd=1978-01-01,1982-01-01&coed={x},{x}&line_color=%234572a7,%23aa4643&link_values=false,false&line_style=solid,solid&mark_type=none,none&mw=3,3&lw=2,2&ost=-99999,-99999&oet=99999,99999&mma=0,0&fml=a,a&fq=Monthly,Monthly&fam=avg,avg&fgst=lin,lin&fgsnd=2020-02-01,2020-02-01&line_index=1,2&transformation=lin,lin&vintage_date={x},{x}&revision_date={x},{x}&nd=1978-01-01,1982-01-01'.format(x=today),
na_values='.')
inflation_expectation.set_index('DATE',inplace=True)
inflation_expectation.index = pd.DatetimeIndex(inflation_expectation.index).to_period('M').to_timestamp('M')

#gas & oil prices, for eom data last period value was used
gas_oil_prices = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1169&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DCOILWTICO,DHHNGSP&scale=left,left&cosd=1997-01-07,1997-01-07&coed={x},{x}&line_color=%234572a7,%23aa4643&link_values=false,false&line_style=solid,solid&mark_type=none,none&mw=3,3&lw=2,2&ost=-99999,-99999&oet=99999,99999&mma=0,0&fml=a,a&fq=Monthly,Monthly&fam=eop,eop&fgst=lin,lin&fgsnd=2020-02-01,2020-02-01&line_index=1,2&transformation=lin,lin&vintage_date={x},{x}&revision_date={x},{x}&nd=1986-01-02,1997-01-07'.format(x=today)
,na_values='.')
gas_oil_prices.set_index('DATE',inplace=True)
gas_oil_prices.index=pd.DatetimeIndex(gas_oil_prices.index).to_period('M').to_timestamp('M')
gas_oil_prices_pct = gas_oil_prices.pct_change(12)*100

#capacity utilization
capacity_utilization = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1169&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TCU&scale=left&cosd=1967-01-01&coed={x}&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date={x}&revision_date={x}&nd=1967-01-01'.format(x=today),
na_values='.')
capacity_utilization.set_index('DATE',inplace=True)
capacity_utilization.index = pd.to_datetime(capacity_utilization.index).to_period('M').to_timestamp('M')
capacity_utilization

#hiking barometer data
hiking_barometer_data = pd.concat([inflation_expectation,gas_oil_prices_pct,capacity_utilization],axis=1)
hiking_barometer_data.fillna(method='ffill',inplace=True)
hiking_barometer_data.dropna(inplace=True)

#barometer model

oil_indicator = pd.DataFrame({"oil_indicator":np.where(hiking_barometer_data['DCOILWTICO'].diff().values>=0,1,-1)})
gas_indicator = pd.DataFrame({"gas_indicator":np.where(hiking_barometer_data['DHHNGSP'].diff().values>=0,1,-1)})
mich_inflation_expec_indicator = pd.DataFrame({"mich_inflation_expec_indicator":np.where(hiking_barometer_data['MICH'].pct_change(12).values>=0,1,-1)})
#if capacity is falling its positive, thus a difference of <0 is a positive indicator
fed_clev_inflation_epec_indicator = pd.DataFrame({"fed_clev_inflation_epec_indicator":np.where(hiking_barometer_data['EXPINF1YR'].pct_change(12).values>=0,1,-1)})
#3 month change in capacity utilization
capacity_utilization_indicator = pd.DataFrame({"capacity_utilization_indicator":np.where(hiking_barometer_data['TCU'].pct_change(3).values<=0,0.25,-0.25)})

barometer = pd.concat([oil_indicator,gas_indicator,mich_inflation_expec_indicator,fed_clev_inflation_epec_indicator,capacity_utilization_indicator],axis=1)
barometer.index = hiking_barometer_data.index
sum_barometer= barometer.sum(axis=1)

#translate barometer into hiking environment


fed_rate=pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1169&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DFF&scale=left&cosd=2021-12-25&coed={x}&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=eop&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date={x}&revision_date={x}&nd=1954-07-01'.format(x=today),
                      na_values='.')

fed_rate.set_index('DATE',inplace=True)
fed_rate.index = pd.to_datetime(fed_rate.index).to_period('M').to_timestamp('M')
fed_rate1=fed_rate.copy()
fed_rate1.index=pd.DatetimeIndex(fed_rate1.index)
fed_rate1.loc['2022-07-31']=2.33 #Problem is that this value gets not replaced but added to the dataframe
fed_rate1.drop_duplicates(inplace=True)
fed_rate1 = fed_rate1.diff()

fed_change=pd.DataFrame(fed_rate1['DFF'].rename('fed_change',inplace=True))

fed_rate.fillna(method='ffill',inplace=True)
fed_rate.index = pd.to_datetime(fed_rate.index).to_period('M').to_timestamp('M')

fed_rate_and_barometer_df = pd.merge(fed_rate,pd.DataFrame({'sum':sum_barometer}),how='left',left_index=True,right_index=True).fillna(method='ffill')

fed_rate_and_fed_change_and_barometer_df = pd.merge(fed_rate_and_barometer_df,fed_change,how='left',left_index=True,right_index=True).ffill()


#if between -0.5 and 0.5, then no change in fed rate, if >=0.5 then increase in fed rate by 0.25, if >1 then increase by 0.5, if - then vice versa
little_dovish_fed = np.where((fed_rate_and_fed_change_and_barometer_df['sum'].values < -0.5) & (fed_rate_and_fed_change_and_barometer_df['sum'].values >= -1),fed_rate_and_fed_change_and_barometer_df['fed_change'] -0.25,None)
big_dovish_fed = np.where(fed_rate_and_fed_change_and_barometer_df['sum'].values < -1,fed_rate_and_fed_change_and_barometer_df['fed_change'] - 0.5,None)


hawkish_fed = np.where(fed_rate_and_fed_change_and_barometer_df['sum'].values > 1, fed_rate_and_fed_change_and_barometer_df['fed_change'] + 0.25 ,None)

carry_on_fed=np.where((fed_rate_and_fed_change_and_barometer_df['sum'].values <= 1) & (fed_rate_and_fed_change_and_barometer_df['fed_change'].values >=-0.5),fed_rate_and_fed_change_and_barometer_df['fed_change'],None)

#create a new dataframe which translates the hiking barometer into a fed rate change

fed_rate_change = pd.DataFrame({'little_dovish_fed':little_dovish_fed,'big_dovish_fed':big_dovish_fed,'hawkish_fed': hawkish_fed,'carry_on_fed':carry_on_fed})

fed_rate_change['fed_change_model'] = fed_rate_change['little_dovish_fed']
fed_rate_change['fed_change_model'].fillna(fed_rate_change['big_dovish_fed'],inplace=True)

fed_rate_change['fed_change_model'].fillna(fed_rate_change['hawkish_fed'],inplace=True)

fed_rate_change['fed_change_model'].fillna(fed_rate_change['carry_on_fed'],inplace=True)

fed_rate_change['fed_change_model'].index=fed_rate_and_fed_change_and_barometer_df['sum'].index



final_fed_model = pd.merge(fed_rate1,fed_rate_change['fed_change_model'],how='right',left_index=True,right_index=True).fillna(method='ffill')




#common functions

def scatter_plot(x,y,name,xlabel,ylabel):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name))
    fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
    return fig


def difference(df):
    change = pd.DataFrame(df.diff())
    change = change.reset_index(inplace=False)[::-1]
    #barometer data

    return change


def percentage_change(df):
    perc_change = pd.DataFrame(((df - df.shift(12)) / df.shift(12)) *100).round(3)
    perc_change = perc_change.reset_index(inplace=False)[::-1]
    return perc_change


def annual_rate_of_change(df):
    annual_rt_chg = ((df - df.shift(1)) / df.shift(1))
    comp_annual_rt_chg = pd.DataFrame((((1 + annual_rt_chg)**4) - 1)*100).round(3)
    comp_annual_rt_chg = comp_annual_rt_chg.reset_index(inplace=False)[::-1]
    return comp_annual_rt_chg

def table(df):
    table_df = dash_table.DataTable(df.to_dict('records'),
                            #[{"name": i, "id": i} for i in df.columns],
                            [{"name": df.columns[0], "id": df.columns[0]},{"name": "VALUE", "id": df.columns[1]}],
                            style_table={'height': '400px', 'overflowY': 'auto'},
                            style_cell={'textAlign': 'center'})
    return table_df

def table2(df):
    table_df = dash_table.DataTable(df.to_dict('records'),
                            [{"name": i, "id": i} for i in df.columns],
                            #[{"name": df.columns[0], "id": df.columns[0]},{"name": "VALUE", "id": df.columns[1]},{"name": "VALUE", "id": df.columns[2]}],
                            style_table={'height': '400px', 'overflowY': 'auto'},
                            style_cell={'textAlign': 'center'})
    return table_df


#list data pairs



#first data pair
#chart of all_employees_tot_nonfarm
fig_all_employees_total_nonfarm_payrolls = scatter_plot(all_employees_tot_nonfarm.index,
                                                        all_employees_tot_nonfarm.values,
                                                        'all_employees_total_nonfarm_payrolls',
                                                        'Date',
                                                        'Thousands of Persons'
                                                        )
#net difference in all_employees_tot_nonfarm
all_employees_tot_nonfarm_change = difference(all_employees_tot_nonfarm)

all_employees_tot_nonfarm_change.iloc[0]
#second data pair
#chart of employment_level
fig_employment_level = scatter_plot(employment_level.index,
                                    employment_level.values,
                                    'employment_level',
                                    'Date',
                                    'Thousands of Persons')
#net difference in employment_level
employment_level_change = difference(employment_level)

#third data pair
#chart of industrial production

fig_industrial_production = scatter_plot(industrial_production.index,
                                         industrial_production.values,
                                         'industrial_production',
                                         'Date',
                                         'Index 2012=100')
#pct change in industrial_production
industrial_production_pct_change = percentage_change(industrial_production)

#fourth data pair
#chart of real manufacturing and trade sales
fig_real_manufacturing_sales = scatter_plot(real_manufacturing_sales.index,
                                            real_manufacturing_sales.values,
                                            'real_manufacturing_sales',
                                            'Date',
                                            'Millions of Chained 2012 Dollars')
#net difference in real_manufacturing_sales
real_manufacturing_sales_pct_change = percentage_change(real_manufacturing_sales)

#fifth data pair
#chart of real personal income excluding current transfer receipts

fig_real_pers_income_ex_curr_transfer_receipts = scatter_plot(real_pers_income_ex_curr_transfer_receipts.index,
                                                                real_pers_income_ex_curr_transfer_receipts.values,
                                                                'real_pers_income_ex_curr_transfer_receipts',
                                                                'Date',
                                                                'Billions of Chained 2012 Dollars')
#pct change in real_pers_income_ex_curr_transfer_receipts
real_pers_income_ex_curr_transfer_receipts_pct_change = percentage_change(real_pers_income_ex_curr_transfer_receipts)

#sixth data pair
#chart of real personal consumption expenditures
fig_real_pers_consumption_expenditures = scatter_plot(real_pers_consumption_expenditures.index,
                                                        real_pers_consumption_expenditures.values,
                                                        'real_pers_consumption_expenditures',
                                                        'Date',
                                                        'Billions of Chained 2012 Dollars')
#pct change in real_pers_consumption_expenditures
real_pers_consumption_expenditures_pct_change = percentage_change(real_pers_consumption_expenditures)

#seventh data pair
#chart of real gross domestic product
fig_real_gdp = scatter_plot(real_gdp.index,
                            real_gdp.values,
                            'real_gdp',
                            'Date',
                            'Billions of Chained 2012 Dollars')
#annual rate of change in real_gdp
real_gdp_annual_rate_of_change = annual_rate_of_change(real_gdp)

#eighth data pair
#chart of real gross domestic income
fig_real_gdi = scatter_plot(real_gdi.index,
                            real_gdi.values,
                            'real_gdi',
                            'Date',
                            'Billions of Chained 2012 Dollars')
#annual rate of change in real_gdi
real_gdi_annual_rate_of_change = annual_rate_of_change(real_gdi)

#ninth data pair
#chart of real average of gdp and gdi
#last item
real_avg_gdp_gdi=df_nber_q.mean(axis=1) 

fig_real_avg_gdp_gdi = scatter_plot(real_avg_gdp_gdi.index,
                                    real_avg_gdp_gdi.values,
                                    'real_avg_gdp_gdi',
                                    'Date',
                                    'Billions of Chained 2012 Dollars')
#annual rate of change in real_avg_gdp_gdi

real_avg_gdp_gdi_annual_rate_of_change = annual_rate_of_change(real_avg_gdp_gdi)
real_avg_gdp_gdi_annual_rate_of_change = real_avg_gdp_gdi_annual_rate_of_change.rename(columns={0:"test"})

#unemployment & housing
housing_data = housing_data.rename(columns={"UNRATE": "Unemployment Rate", "MSACSR": "Monthly Supply of new Houses"})
fig_housing_data = scatter_plot(housing_data['DATE'].values,
                                housing_data['Unemployment Rate'].values,
                                'Unemployment Rate',
                                'Date',
                                'Percent')
fig_housing_data.add_trace(go.Scatter(x=housing_data['DATE'].values,
                                        y=housing_data['Monthly Supply of new Houses'].values,
                                        name='Monthly Supply of new Houses',
                                        mode='lines',
                                        line=dict(color='firebrick', width=1)))
fig_housing_data.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
housing_data = housing_data[::-1]
#tab2 data
#chart of cpi
fig_yoy_cpi_series = scatter_plot(yoy_cpi_series.index,
                                    yoy_cpi_series.values,
                                    'yoy_cpi_series',
                                    'Date',
                                    'YoY- Change, Index 1982=100')

#CPI Table
CPI_change_table = pd.DataFrame(yoy_cpi_series[::-1].round(2).reset_index(inplace=False))


#final fed model table
final_fed_model_table = pd.DataFrame(final_fed_model[::-1].round(2).reset_index())
final_fed_model_table['DATE'] = final_fed_model_table['DATE'].dt.strftime('%Y-%m-%d')
final_fed_model_table = final_fed_model_table.rename(columns={'DFF':'FED FUNDS RATE CHANGE','fed_change_model':'MODEL FED RATE CHANGE'})
final_fed_model_chart = final_fed_model_table[::-1]
#chart of fed model
fig_final_fed_model = scatter_plot(final_fed_model_chart['DATE'],
                                    final_fed_model_chart['FED FUNDS RATE CHANGE'].values,
                                    'FED FUNDS RATE CHANGE',
                                    'Date',
                                    'FED FUNDS RATE CHANGE')
fig_final_fed_model.add_trace(go.Scatter(x=final_fed_model_chart['DATE'],
                                        y=final_fed_model_chart['MODEL FED RATE CHANGE'].values,
                                        mode='lines',
                                        name='MODEL FED RATE CHANGE'))

#GDP Model
forecasts = pd.read_csv("forecasts.csv")
group_impacts = pd.read_csv("group_impacts.csv")

group_impacts.index = group_impacts["Unnamed: 0"].astype(dtype='period[M]')
group_impacts = group_impacts.drop(columns=["Unnamed: 0"])
forecasts.index = forecasts["Unnamed: 0"].astype(dtype='period[M]')
forecasts = forecasts.drop(columns=["Unnamed: 0"])
forecasts = forecasts.squeeze()

# Stacked bar plot showing the impacts by group
gdpforecatchart = go.Figure(data=[go.Bar(
    x=group_impacts.index.strftime('%b'),
    y=group_impacts[col],
    marker=dict(color = px.colors.sequential.thermal[i+2]),
    name=col,
    hovertemplate='%{y:.2f}'
) for i, col in enumerate(group_impacts.columns) if col != 'Total'])

# Line plot showing the forecast for real GDP growth in 2020Q2 for each vintage
x = np.arange(len(forecasts))
gdpforecatchart.add_trace(go.Scatter(
    x=group_impacts.index.strftime('%b'),
    y=forecasts,
    mode='lines+markers',
    line=dict(color=px.colors.qualitative.Plotly[0] , width=2),
    marker=dict(symbol='circle', size=7, color = "white"),
    name='Forecast',
    hovertemplate='%{y:.2f}'
))
gdpforecatchart.update_layout(
    barmode='stack',
    yaxis=dict(
        tickfont=dict(size=14),
        ticks='inside',
        showticklabels=True,
        zeroline=False,
        showgrid=True
    ),
    title=dict(
        text='Real GDP growth forecast: 2023Q1',
        font=dict(size=22, color='White', family='Arial'),
        xanchor='left'
    ),
    legend=dict(
        orientation='h',
        xanchor='center',
        x=0.5,
        yanchor='bottom',
        y=-0.5,
        font=dict(size=13)
    ),
    margin=dict(l=50, r=50, t=80, b=50)
)

#annual rate of change in yoy_cpi_series
#yoy_cpi_series_annual_rate_of_change = annual_rate_of_change(yoy_cpi_series)


#app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#list data pairs
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

tab_selected_style = {
    'borderTop': '0px solid #ff7f0e',
    'borderBottom': '4px solid #1f77b4',
    'borderLeft': '0px solid #ff7f0e',
    'borderRight': '0px solid #ff7f0e',
    'padding': '25px',
    'fontWeight': 'bold',
    'color': 'black',
    'backgroundColor': 'white'
}

tab_style = {
    'borderTop': '1px solid #1f77b4',
    'borderBottom': '4px solid #FFFFFF',
    'borderLeft': '1px solid #1f77b4',
    'borderRight': '1px solid #1f77b4',
    'backgroundColor': 'black',
    'color': '#1f77b4',
    'fontWeight': 'bold',
    'padding': '25px'
}


#google analytics
app.scripts.config.serve_locally = False
app.scripts.append_script({
    'external_url': 'https://www.googletagmanager.com/gtag/js?id=G-T4WV5HS8E8'
})
app.scripts.append_script({
    'external_url': 'https://cdn.jsdelivr.net/gh/Tvogel20/dashapp/gtag.js'
})

#Row items
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='US GDP Forecast, Fed Rate & CPI Monitor', style=tab_style,selected_style = tab_selected_style, children=[
            html.Div([
                      html.Div(children=[    
                        html.Br(),
                        html.H3('Recession Monitor Readme'),
                        html.Div(children='''
                            You can use the top two tabs (black and white) to navigate between the recession monitors and the recession indicators. You can download charts by clicking on the download button on the top right of each chart/table.
                        '''),
                        html.Div(children='''
                            For any questions or comments please reach out to: tom.vogel22@imperial.ac.uk
                        ''')
                        ], style={'padding': 10, 'flex': 1}),
                    #first item of first column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.H3('GDP Forecast'),
                        html.Div(children='''
                            GDP Forecast utilizing a dynamic factor model.
                        '''),
                        dcc.Graph(
                            id='gdp_forecast',
                            figure=gdpforecatchart
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of first column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            GDP Forecast (Pct_Change) will be updated once a month at the beginning of the consecutive month e.g. for gdp nowcast of mai, update will be given by beginning of April. 
                        ''')
                        
                    ],style={'padding': 15, 'flex': 1}),
                    #second item of first column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.H3('Fed Fund Rate Model Outlook based on Gas, Oil, Inflation expectations & Capacity Utilization'),
                        html.Div(children='''
                            Fed Fund Rate Change Model Outlook vs Fed Fund rate changes.
                        '''),
                        dcc.Graph(
                            id='final_fed_model',
                            figure=fig_final_fed_model
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #third item of first column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Fed fund barometer model - if no rate hike announced, FED FUNDS RATE CHANGE will take prev value. 
                        '''),
                        html.Div(children='''
                            The Model values offer a monthly indication for the pace of the fed hiking cycle, e.g. should the fed continue with 75bp hikes or will the fed increase / decrease the pace based on key inflation parameters.
                        '''),
                        table2(final_fed_model_table)
                        
                    ],style={'padding': 15, 'flex': 1}),
                    #second item of second column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.H3('CPI Monitor'),
                        html.Div(children='''
                            CPI.
                        '''),
                        dcc.Graph(
                            id='cpi',
                            figure=fig_yoy_cpi_series
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of second column tab 2
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            CPI YoY change in %.
                        '''),
                        table(CPI_change_table)
                        
                        ],style={'padding': 15, 'flex': 1})
                    
                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'column'})

        ]),
        dcc.Tab(label='NBER Recession Dashboard inc. Housing (click me)', style=tab_style, selected_style = tab_selected_style, children=[
            html.Div([
                html.H1('NBER Recession Indicators', style={'textAlign': 'center','margin-top': '50px'}),
                html.Br(),
                html.H3('All Employees (Total Nonfarm) & Employment level'),
                #Row 1
                html.Div([
                    #first row
                    #first item of first row
                    
                    html.Div(children=[
                        html.Br(),
                        html.Div(children='''
                            All Employees, Total Nonfarm.
                        '''),
                        dcc.Graph(
                            id='all_employees_total_nonfarm_payrolls',
                            figure=fig_all_employees_total_nonfarm_payrolls
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of first row
                    html.Div(children=[
                        html.Br(),
                        html.Div(children='''
                            All Employees, Total Nonfarm (Net Change).
                        '''),
                        table(all_employees_tot_nonfarm_change)
                        
                        ],style={'padding': 15, 'flex': 1}),
                    #second row
                    #third item of first row
                    html.Div(children=[
                        html.Br(),
                        html.Div(children='''
                            Employment level.
                        '''),
                        dcc.Graph(
                            id='employment_level',
                            figure=fig_employment_level
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #fourth item of first row
                    html.Div(children=[
                        html.Br(),
                        html.Div(children='''
                            Employment level (Net_Change).
                        '''),
                        table(employment_level_change)
                        
                    ],style={'padding': 15, 'flex': 1})
                    
                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'row'}),

                html.H3('Industrial Production & Real Manufaturning and Trade Industries Sales'),

                #Row 2
                html.Div([
                    #first row
                    #first item of second row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Industrial Production: Total Index.
                        '''),
                        dcc.Graph(
                            id='industrial_production',
                            figure=fig_industrial_production
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of second row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Industrial Production: Total Index (Pct_Change).
                        '''),
                        table(industrial_production_pct_change)
                        
                        ],style={'padding': 15, 'flex': 1}),
                    #third item of second row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Manufaturning and Trade Industries Sales.
                        '''),
                        dcc.Graph(
                            id='employment_level2',
                            figure=fig_real_manufacturing_sales
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #fourth item of second row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Manufaturning and Trade Industries Sales (Pct_Change).
                        '''),
                        table(real_manufacturing_sales_pct_change)
                        
                    ],style={'padding': 15, 'flex': 1})
                    
                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'row'}),
                html.H3('Real personal income exluding current transfer receipts & Real Personal Consumption Expenditures'),
                #Row 3
                html.Div([
                    #first row
                    #first item of third row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real personal income exluding current transfer receipts.
                        '''),
                        dcc.Graph(
                            id='real_pers_income_ex_curr_transfer_receipts',
                            figure=fig_real_pers_income_ex_curr_transfer_receipts
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of third row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real personal income exluding current transfer receipts (Pct_Change).
                        '''),
                        table(real_pers_income_ex_curr_transfer_receipts_pct_change)
                        
                        ],style={'padding': 15, 'flex': 1}),
                    #third item of third row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Personal Consumption Expenditures.
                        '''),
                        dcc.Graph(
                            id='employment_level3',
                            figure=fig_real_pers_consumption_expenditures
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #fourth item of third row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Personal Consumption Expenditures (Pct_Change).
                        '''),
                        table(real_pers_consumption_expenditures_pct_change)
                        
                    ],style={'padding': 15, 'flex': 1})
                    
                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'row'}),
                html.H3('Real GDP & GDI'),
                #Row 4
                html.Div([
                    #first row
                    #first item of fourth row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real GDP.
                        '''),
                        dcc.Graph(
                            id='real_gdp',
                            figure=fig_real_gdp
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of fourth row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real GDP (Annual Rate of Change).
                        '''),
                        table(real_gdp_annual_rate_of_change)
                        
                        ],style={'padding': 15, 'flex': 1}),
                    #third item of fourth row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real GDI.
                        '''),
                        dcc.Graph(
                            id='real_gdi',
                            figure=fig_real_gdi
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #fourth item of fourth row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real GDI (Annual Rate of Change).
                        '''),
                        table(real_gdi_annual_rate_of_change)
                        
                    ],style={'padding': 15, 'flex': 1})
                    
                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'row'}),
                html.H3('Real avg GDP + GDI, Recession Indicator Barometer'),
                #Row 5
                html.Div([
                    #first row
                    #first item of fith row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Average GDP + GDI.
                        '''),
                        dcc.Graph(
                            id='real_avg_gdp_gdi',
                            figure=fig_real_avg_gdp_gdi
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #second item of fith row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Real Average GDP + GDI (Pct_Change).
                        '''),
                        table(real_avg_gdp_gdi_annual_rate_of_change)
                        
                        ],style={'padding': 15, 'flex': 1}), 
                    #third item of fith row
                    
                    
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Housing & Unemployment.
                        '''),
                        dcc.Graph(
                            id='Housing & Unemployment',
                            figure=fig_housing_data
                        )
                        ], style={'padding': 10, 'flex': 1}),
                    #fourth item of fith row
                    html.Div(children=[
                        
                        html.Br(),
                        html.Div(children='''
                            Housing & Unemployment (Pct_Change).
                        '''),
                        table2(housing_data)
                        
                    ],style={'padding': 15, 'flex': 1})
                    

                ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'row'})



            ], style={'width': 'auto' , 'display': 'flex', 'flex-direction': 'column'})
        ])
    ])
])




if __name__ == '__main__':
    app.run_server(debug=True)












#test






#convert final_fed_model_table['DATE'] to YYYY-MM-DD format





















