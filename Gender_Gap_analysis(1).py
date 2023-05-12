# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:33:40 2023

@author: Aigul
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:22:29 2023

@author: akosh
"""
# Gender equality exploration
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.dpi']=300
#%%

# We start with read a dataframe by Gender inequality 
#index developed by United Nation
gender_equality_rating = pd.read_csv('HDR21-22_Statistical_Annex_GII_Table.csv')
# Create list of countries to analysis 
list_of_countries = ['Kazakhstan', 'United States', 'Iceland']
# set an index
gender_equality_rating = gender_equality_rating.loc[
    gender_equality_rating['Country'].isin(list_of_countries)]

gender_equality_rating  = gender_equality_rating.set_index(
    ['Country','GII','Rank'])
gender_equality_rating = gender_equality_rating.reset_index()

#select columns called 'GII'
gender_equality_rating_new = gender_equality_rating[['Country','Rank']].copy()

#view new DataFrame
gender_equality_rating_new['Rank']=gender_equality_rating_new['Rank'].astype(float)
gender_equality_rating_new = gender_equality_rating_new.set_index('Country')

# Create a plot to see GII by selected countries

fig1,ax=plt.subplots()
gender_equality_rating_new.plot.barh(ax=ax)
fig1.suptitle("Gender inequality rating")
fig1.tight_layout()
fig1.savefig("Gender_inequality_rating.png")

#%%
#Now we are going to create a dataframe to see the progress of The Global Gender 
#Gap Index (GGGI), devised by the World Economic Forum 
# Comparisons between Kazakhstan and United Sates
fig,ax1=plt.subplots()
gggi = pd.read_csv('GGGI_by_KZ_US.csv', index_col="country")
gggi.plot.barh(ax=ax1)
fig.suptitle('The Global Gender Gap Index by countries in 2022')
fig.tight_layout()
fig.savefig("The_Global_Gender_Gap_Index_by_countries-in_2022.png")

#%%
# Now we are going to create a dataframe to see the progress of The Global Gender 
#Gap Index (GGGI), devised by the World Economic Forum
#Kazakhstan
fig,ax1=plt.subplots()
gender_gap_kaz = pd.read_csv('gender_gap_index_wef_kaz.csv', index_col="Indicators")
gender_gap_kaz.plot.barh(ax=ax1)
fig.suptitle('The Global Gender Gap Index in Kazakhstan')
fig.tight_layout()
fig.savefig("The_Global_Gender_Gap_Index_in_Kazakhstan.png")

#%%
# United States
fig,ax1=plt.subplots()
gender_gap_us = pd.read_csv('US_GGGI_WEF.csv', index_col="Indicators")
gender_gap_us.plot.barh(ax=ax1)
fig.suptitle('The Global Gender Gap Index in US')
fig.tight_layout()
fig.savefig("The_Global_Gender_Gap_Index_in_US.png")

#%%
# Iceland which is ranked fisrt over the last 5 years

fig,ax1=plt.subplots()
gender_gap_ic = pd.read_csv('Iceland_GGGI_WEF.csv', index_col="Indicators")
gender_gap_ic.plot.barh(ax=ax1)
fig.suptitle('The Global Gender Gap Index in Iceland')
fig.tight_layout()
fig.savefig("The_Global_Gender_Gap_Index_in_Iceland.png")

#%%
# Indicate parity between girls and boys in order to understand 
#why some countries has a lower rank of educational attainment 
# Educational Attainment acoordintg World Bank data
gender_parity = pd.read_csv('gender_parity.csv')
gender_parity = gender_parity.loc[gender_parity['Country Name'].isin(list_of_countries)]

# selected years

year = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

# set an index

gender_parity = gender_parity.set_index(['Country Name', 'Indicator Name'])
gender_parity = gender_parity[year]
gender_parity = gender_parity.reset_index()
gender_parity = gender_parity.drop(columns = 'Indicator Name')
gender_parity = gender_parity.melt(id_vars = 'Country Name', var_name = 'year', 
                                   value_name = 'gender parity index')

#%%
# Develop a figure for gender parity index
sns.set_style("whitegrid")
plt.figure(figsize=(12,8))
sns.lineplot(data=gender_parity, x='year', y='gender parity index', hue='Country Name', linewidth=2.5)
plt.title('Gender Parity Index by Country and Year (WB)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('GPI', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig('Gender_Parity_Index_(World_bank).png',dpi=300,bbox_inches='tight')

#%%
# Visualizations for unemployment of female in comparison with man
# Read a DataFrame for unemployment given by World bank
unemployment_fem = pd.read_csv('unemployment_female.csv')
unemployment_male = pd.read_csv('unemployment_male.csv')

# Strusturaze data (female) by selected year and country
unemployment_fem = unemployment_fem.loc[unemployment_fem ['Country Name'].isin(list_of_countries)]

# set an index

unemployment_fem = unemployment_fem.set_index(['Country Name', 'Indicator Name'])
unemployment_fem = unemployment_fem[year]
unemployment_fem = unemployment_fem.reset_index()
unemployment_fem = unemployment_fem.drop(columns = 'Indicator Name')
unemployment_fem = unemployment_fem.melt(id_vars = 'Country Name', var_name = 'year', value_name = 'Unemployment female')
# Structuraze data (male) by selected year and country
unemployment_male = unemployment_male.loc[unemployment_male ['Country Name'].isin(list_of_countries)]

# set an index

unemployment_male = unemployment_male.set_index(['Country Name', 'Indicator Name'])
unemployment_male = unemployment_male[year]
unemployment_male = unemployment_male.reset_index()
unemployment_male = unemployment_male.drop(columns = 'Indicator Name')
unemployment_male = unemployment_male.melt(id_vars = 'Country Name', var_name = 'year', value_name = 'Unemployment male')

# Create a dataframe
combined = unemployment_fem.merge(unemployment_male)
averages = combined.groupby('Country Name').mean()
stack =averages.stack().reset_index()

#rename two columns 
stack.rename(columns = {'level_1':'sex',0:'rate_unemployment'},inplace=True)
#%%
# Create a figire which provide a comparison between unemployment rates of female and male

g=sns.catplot(data=stack,x='rate_unemployment', y = 'Country Name', 
              col='sex', kind='bar',orient='h') 
g.figure.suptitle("Comparison of female and male unemployment")
g.figure.tight_layout()              
#Save a replot

g.savefig("Comparisons_of_female_and_male_unemployment.png")

#%%
# Read a dataframe by employed women by type of activity: industry

employed_ind_fem = pd.read_csv('employment_industry_female.csv')

# set an index

employed_ind_fem = employed_ind_fem.set_index(['Country Name', 'Indicator Name'])
employed_ind_fem = employed_ind_fem[year]
employed_ind_fem  = employed_ind_fem .reset_index()
employed_ind_fem = employed_ind_fem.drop(columns = 'Indicator Name')
employed_ind_fem  = employed_ind_fem.melt(id_vars = 'Country Name', var_name = 'year', value_name = 'employed women by industry')
employed_ind_fem  = employed_ind_fem.loc[employed_ind_fem ['Country Name'].isin(list_of_countries)]
employed_ind_fem.head()

#%%
# Read a dataframe by employed women by type of activity: agriculture

employed_agro_fem = pd.read_csv('employed_agriculture_female.csv')

# set an index

employed_agro_fem = employed_agro_fem.set_index(['Country Name', 'Indicator Name'])
employed_agro_fem = employed_agro_fem[year]
employed_agro_fem = employed_agro_fem.reset_index()
employed_agro_fem = employed_agro_fem.drop(columns = 'Indicator Name')
employed_agro_fem = employed_agro_fem.melt(id_vars = 'Country Name', var_name = 'year', value_name = 'employed women by agriculture')
employed_agro_fem = employed_agro_fem.loc[employed_agro_fem['Country Name'].isin(list_of_countries)]
employed_agro_fem.head()
#%%
# Read a dataframe by employed women by type of activity: service

employed_serv_fem = pd.read_csv('employed_services_female.csv')

# set an index

employed_serv_fem  = employed_serv_fem.set_index(['Country Name', 'Indicator Name'])
employed_serv_fem  = employed_serv_fem [year]
employed_serv_fem = employed_serv_fem .reset_index()
employed_serv_fem  = employed_serv_fem.drop(columns = 'Indicator Name')
employed_serv_fem  = employed_serv_fem.melt(id_vars = 'Country Name', var_name = 'year', value_name = 'employed women by service')
employed_serv_fem  = employed_serv_fem.loc[employed_serv_fem ['Country Name'].isin(list_of_countries)]
employed_serv_fem.head()

# Merge data of employed female
employed_fem = employed_ind_fem.merge(employed_serv_fem)
employed_fem_comb = employed_fem.merge(employed_agro_fem)
employed_fem_comb.head()
#%%

piedata = employed_fem_comb.query('year =="2019"')

piedata = piedata.rename(columns = {
    'employed women by industry':'ind',
    'employed women by service':'serv',
    'employed women by agriculture':'agri'})
piedata = piedata.drop(columns = 'year').set_index('Country Name')
fig1,ax1=plt.subplots()
piedata.plot.barh(stacked=True,ax=ax1)
fig1.suptitle("Employed women by type of activity")
fig1.tight_layout()
fig1.savefig("Employed_women_by_type_of_activity.png")

