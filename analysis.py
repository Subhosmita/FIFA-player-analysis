import pandas as pd
import matplotlib.pyplot as plt
import numpy as n

url="https://docs.google.com/spreadsheets/d/1UviDfkcdfkOjgV2eSlOPI3jl9rLV___s/edit?usp=sharing&ouid=110138448096973297414&rtpof=true&sd=true"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]

df=pd.read_excel(url)

#Average age of the athletes in the dataset
age=df['Age'].mean()
print("Average age of athlete = ", age)

#Which country has the highest no of athlete
result=df['Country'].value_counts().idxmax()
print('The country having highest no. of athlete = ', result)

#How many diff sports are represented in the dataset
sports= df['Sport'].unique()
print(sports)

#What is the total number of gold, silver, and bronze medals won by all athletes
gold=df["Gold Medals"].sum()
print("Total number of gold medals won by all athlete = ",gold)
silver=df["Silver Medals"].sum()
print("Total number of silver medals won by all athlete = ",silver)
bronze=df["Bronze Medals"].sum()
print("Total number of bronze medals won by all athlete = ",bronze)

#Which soprts have highest number of Gold medel
allsports= df.groupby(['Sport']).count()
medals=allsports['Gold Medals'].idxmax()
print("The highest gold medel recived by =",medals)

#How many medals did each country win in total
def myFunc(g):
    return g['Total Medals'].sum()
print(df.groupby(['Country']).apply(myFunc))

#What is the distribution of medals among different sports
def myFunc(g):
    return g['Total Medals'].sum()
print(df.groupby(['Sport']).apply(myFunc))

#Is there any correlation between the age of the athlete and the number of medals won
x = df['Total Medals']
y = df['Age']
plt.scatter(x, y)
 
plt.plot(n.unique(x),n.poly1d(n.polyfit(x, y, 1))(n.unique(x)), color = 'green')
plt.show()

#How has the number of athletes and medals changed over the years
plt.hist(df['Year'], bins=20)
plt.show()

#Which country has the highest overall medal count
def myFunc(g):
    return g['Total Medals'].sum()
print(df.groupby(['Country']).apply(myFunc).idxmax())
