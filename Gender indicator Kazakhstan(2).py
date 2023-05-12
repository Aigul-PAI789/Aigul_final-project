# -*- coding: utf-8 -*-
"""
Created on Thu May 11 02:11:07 2023

@author: Aigul
"""
#Gender indicators analysis: case of Kazakhstan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.dpi']=300


#%%
#The gender inequality index in the Republic of Kazakhstan: read the dataframework

gii_KZ=pd.read_csv('GII_KZ_dynamics.csv', index_col="Year")
gii_KZ_1=gii_KZ["The gender inequality index"]
#Set a index
#Kazakhstan
fig,ax1=plt.subplots()
gii_KZ_1.plot.line(ax = ax1)
fig.suptitle('The Gender Inequality Index in Kazakhstan')
fig.tight_layout()
fig.savefig("The_Gender Inequality Index _in_Kazakhstan.png")

#x="The gender inequality index", 

#%%
#create a figure to see the subcompositions of main GII indicator in Kazakhstan
gii_KZ_2=gii_KZ["Maternal mortality ratio (deaths per 100,000 live births)"]

gii_KZ_3=gii_KZ["Adolescent fertility ratio (births per 1000 women ages 15-19)"]
fig,(ax1,ax2)=plt.subplots(2,1)
gii_KZ_2.plot.line(ax=ax1)
gii_KZ_3.plot.line(ax=ax2)
ax1.set_ylabel("deaths per 100,000\n live births")
ax2.set_ylabel("births per 1000 women\n ages 15-19")

fig.suptitle('Maternal mortality & Adolescent fertility ratios in Kazakhstan')
fig.tight_layout()
fig.savefig("Maternal_mortality_&_Adolescent_fertility_ratios_in_Kazakhstan.png")

#%%

#See the dynamics of Seats in the Mazhilis of the Parliament, 
#the ratio of men and women, male
gii_KZ_4=gii_KZ["Seats in the Mazhilis of the Parliament, the ratio of men and women, male"]
gii_KZ_5=gii_KZ["Seats in the Mazhilis of the Parliament, the ratio of men and women, female"]

fig,(ax4,ax5)=plt.subplots(2,1)
gii_KZ_3.plot.line(ax=ax4)
gii_KZ_4.plot.line(ax=ax5)
ax4.set_ylabel("male")
ax5.set_ylabel("female")

fig.suptitle('Seats in the Mazhilis of the Parliament,\n the ratio of men and women in Kazakhstan')
fig.tight_layout()
fig.savefig("Seats_in_the_Mazhilis_of_the_Parliament,_the_ratio_of_men_and_women_in_Kazakhstan.png")

#%%

#See the dynamics of Percentage of population aged 15 years 
#and older having at least secondary education
gii_KZ_6=gii_KZ["Percentage of population aged 15 years and older having at least secondary education, male"]
gii_KZ_7=gii_KZ["Percentage of population aged 15 years and older having at least secondary education, female"]

fig,(ax6,ax7)=plt.subplots(2,1)
gii_KZ_6.plot.line(ax=ax6)
gii_KZ_7.plot.line(ax=ax7)
ax6.set_ylabel("male")
ax7.set_ylabel("female")

fig.suptitle('Percentage of population aged 15 years\n and older having at least secondary education in Kazakhstan')
fig.tight_layout()
fig.savefig("Percentage_of_population_aged_15_years_and_older_having_at_least_secondary_education_in_Kazakhstan.png")

#%%

#See the dynamics of Proportion of the economically 
#active population of working age
gii_KZ_8=gii_KZ["Proportion of the economically active population of working age, male"]
gii_KZ_9=gii_KZ["Proportion of the economically active population of working age, female"]

fig,(ax8,ax9)=plt.subplots(2,1)
gii_KZ_8.plot.line(ax=ax8)
gii_KZ_9.plot.line(ax=ax9)
ax8.set_ylabel("male")
ax9.set_ylabel("female")

fig.suptitle('Proportion of the economically active population of working age in Kazakhstan')
fig.tight_layout()
fig.savefig("Proportion_of_the_economically_active population_of_working_age_in_Kazakhstan.png")

#%%
# See the correlation between GDP growth and GII in selected countries

gdp_gii = pd.read_csv('GDP_GII.csv', dtype={'Year':str})
grouped = gdp_gii.groupby('Country')
correlation=grouped.apply(lambda x: x['GDP,%'].corr(x['GII']))
correlation.head()

#%%
# There are no correlation between GDP growth and GII 
#scatter plots with liner regression line and saving them
for country, data in grouped:
    sns.regplot(x='GDP,%', y = 'GII', data = data)
    plt.xlabel('GDP(%)')
    plt.ylabel('GII')
    plt.title('Scatter Plot of GDP growth and Gender Inequality')
    plt.savefig('Scatter_Plot_of_GDP_growth_and_Gender_Inequality.png')
    plt.clf()

#%%              
# Now we are going to look are there correlation between 
#Gender Development Index and GDP growwth
gdp_gii = pd.read_csv('GDP_GII.csv', dtype={'Year':str})
grouped_1 = gdp_gii.groupby('Country')
correlation_1=grouped_1.apply(lambda x: x['GDP,%'].corr(x['GDI']))
correlation.head()

#%%
# There are no correlation between GDP growth and GDI 
#scatter plots with liner regression line and saving them
for country, data in grouped_1:
    sns.regplot(x='GDP,%', y = 'GDI', data = data)
    plt.xlabel('GDP(%)')
    plt.ylabel('GDI')
    plt.title('Scatter Plot of GDP growth and Gender Development')
    plt.savefig('Scatter_Plot_of_GDP_growth_and_Gender_Development.png')
    plt.clf()


 

