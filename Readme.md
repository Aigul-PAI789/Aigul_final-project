# Gender equality exploration

## Background

The role of gender equality is recognized by the international community as a defining one in the political agenda of countries. The issue of gender equality is integrated into the key Development Indices, which today are an effective tool for assessing progress in the world: the Gender Development Index, the Gender Inequality Index, the SDG Gender Index, the Social Institutions and Gender Issues Index, the Gender Gap Index, etc. About This is evidenced by the status of structures declaring the importance of gender equality, including the UN,WEF, the World Bank, etc. 

In this project, we provide an overview of the main indicators that are presented by the above-mentioned international organizations in the context of three countries: Iceland, the USA and Kazakhstan. In the latest ranking of the World Economic Forum, these countries are ranked 1, 27 and 65, respectively.

## Input Data

We used a differet sources of data such as: 
Global Gender Gap Report 2022, World Economic Forum 
![report] https://www.weforum.org/reports/global-gender-gap-report-2022/

![Gender data]  https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII GENDER INEQUALITY INDEX (GII) prepared by UNDP

![World bank Gender data] https://data.worldbank.org/

![SDG progress data] https://gender.stat.gov.kz/en prepared by BUREAU OF NATIONAL STATISTICS
AGENCY FOR STRATEGIC PLANNING AND REFORMS OF THE REPUBLIC OF KAZAKHSTAN

We also compiled tables for analysis using reports submitted by the World Economic Forum, the UN, the World Bank and the National Bureau of Statistics, in PDF format. The data that we took from these reports was processed into Excel format and saved in csv mode. This allowed us to work with the data that Spyder (Python 3.9) reads.

During analysis data is cleaned up to the required variables for the project purpose.

## Deliverables and Instructions

Analysis is done in 5 Python scripts, and all results of the analysis were presented by plots. 

The project contains two scripts: Gender Gap analysis(1).py and Gender indocator Kazakhstan(2).py which should be run in the following order:

## I. Script Gender Gap analysis(1).py

This script is designed to analyze the gender indicators of the selected countries: Iceland, United States and Kazakhstan. The content of the script is conventionally divided into 13 parts using the #%% sign. The scrip divided by 14 parts due to analysis of several indicators given by international organizations. These parts of the script need to be run in order to avoid overlapping graphs.

1. First part analyse the Gender inequality index developed by United Nation. Then the data is cleaned up to the necessary variables for analysis. After production data is grouped by countries and  year, it was reshaped so that each row represents a country and each column represents a year. After that, script builds a figure on Gender ineuqlity index by country. On that figure you can see what Iceland marked an 8th rank, United States - 44th and Kazakhstan - 41st. The figure is saved as png file named Gender_inequality_rating.png.

2. The second part of the script analyse the progress of The Global Gender Gap Index (GGGI), devised by the World Economic Forum in 2022.  We used a table was created by our self by using the GGGI report. It because the World Economic Forum doesn't provide data in excel type. You can find a data in file GGGI_by_KZ_US.csv It begins with filtering out the data on wheat production from total agriculture production data. Further, we creare a dataframe and constructs second figure that shows the global gender gap scores across the four main components (subindexes) of the index: Economic Participation and Opportunity,Educational Attainment, Health and Survival, and Political Empowerment. The heatmap is saved as "The_Global_Gender_Gap_Index_by_countries-in_2022.png".

3. The third part of the script create a dataframe to see the progress of The Global Gender  Gap Index (GGGI), devised by the World Economic Forum - case of Kazakhstan (ranked 65th). It also shows the GGGI across the four main components. The result was given by figure "The_Global_Gender_Gap_Index_in_Kazakhstan.png".

4.  The fourth part of the script create a dataframe to see the progress of The Global Gender  Gap Index (GGGI), devised by the World Economic Forum - case of United States (ranked 27th). The result was given by figure "The_Global_Gender_Gap_Index_in_US.png".

5. In the fifth part of the script we use the same approach to see the progress of The Global Gender  Gap Index (GGGI), devised by the World Economic Forum - case of Iceland which is ranked fisrt over the last 5 years. The result was given by figure "The_Global_Gender_Gap_Index_in_Iceland.png".

6. In order to understand  why some countries has a lower rank of educational attainment, in part 6 we analyse the parity between girls and boys. That indicator measured by World Bank and used by us as a additional measuring to show Educational Attainment. The World bank data was cleaned and used to develop a figure by selected countries. The resul presented by figure saved as "Gender_Parity_Index_(World_bank).png"

7. The same approach uses in order to visualize unemployment of female in comparison with man. The results was given by figure "Comparisons_of_female_and_male_unemployment.png".

8. The final part of first scrip give us the picture of employed women by type of activity: industry, agriculture and service. The data was taken from World bank, then cleaned up and finally used to construct the figure "Employed_women_by_type_of_activity.png"

## II. Second script "Gender indicator Kazakhstan(2).py

Second script aims to analyze gender progress of the Republic of Kazakhstan. This script  has 9 conventional parts that are divided by the #%% sign.

1. We start from reading the dataframe which shows us the dynamics og gender inequality index in the Republic of Kazakhstan from the 2008 till 2020 year. The dataframe created by using the United Nation's report on gender inequlity. The result presented by figure "The_Gender Inequality Index _in_Kazakhstan.png"

2. Then we moved to the analysis of the subcompositions of main GII indicator in Kazakhstan: Maternal mortality ratio, Adolescent fertility ratio. The dynamics of that indicators development presented by figure "Maternal_mortality_&_Adolescent_fertility_ratios_in_Kazakhstan.png".

3. The political empowerement was seeing through following indicator "Seats in the Mazhilis of the Parliament, the ratio of men and women. The figure "Seats_in_the_Mazhilis_of_the_Parliament,_the_ratio_of_men_and_women_in_Kazakhstan.png" presents the result of our analysis. 

4. Next part of the script shows the dynamics of population aged 15 years and older having at least secondary education. The data after preparation shows us the result where we can see a balance between female and male. Figure "Percentage_of_population_aged_15_years_and_older_having_at_least_secondary_education_in_Kazakhstan.png" shows that resume. 

5. The dynamics of Proportion of the economically active population of working age was monitoring in the next part of script. The same appoach was used to analyse such indicator and result was presented by figure "Proportion_of_the_economically_active population_of_working_age_in_Kazakhstan.png".

6. Finally we test the correlation between GDP growth and GII ans GDI. Our analysis shows that the gender inequality index and Gender development index does not depend on real GDP growth rates. There are no correlations between them. The results was received by using scatter plots with liner regression line. Two figures show the main results: 'Scatter_Plot_of_GDP_growth_and_Gender_Inequality.png' and 'Scatter_Plot_of_GDP_growth_and_Gender_Development.png'

## Analysis/discuss the results

Kazakhstan is progressing towards gender equality according to the international indicators used for measuring the progress and comparing results across the UN member states.

According to the latest World Economic Forum report on the Gender Gap, Kazakhstan ranks 65th out of 146 countries. The first three places remain with Iceland, Finland and Norway. 

Our analysis shows that the gender equality index does not depend on real GDP growth rates.

The positive development of gender processes is noted in countries with a high human development index. This leads them to achieve gender equality.

A composite measure reflecting inequality in achievement between women and men in three dimensions: reproductive health, empowerment and the labour market. As we can see from the table 3 Kazakhstan in comparison with high ranked country’s has some limits of growth. First of all, it’s regards Political Empowerment and a bid ratio of a maternal mortality. It should be note that labour force participation today is very important factor. 

If we turn to the Global Gender Gap Index we have to stress that there is a same limitation: Political Empowerment. 

One of the limits to growth could also be high unemployment. In this regard, it is important to apply the principles of good governance.

Women's economic empowerment is critical to achieving gender equality and poverty alleviation, as well as in terms of women's economic potential and their contribution to a country's economic development. 

## Note

Kazakhstan, as a full member of the UN, among other 193 countries, in September 2015 at the anniversary UN Summit joined the Global Development Agenda until 2030, which includes 17 Sustainable Development Goals. The global development agenda until 2030 is comprehensive, combining the social, economic and environmental components of sustainable development.
