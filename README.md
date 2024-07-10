# Data Cleaning in python

![image](https://github.com/allan-pg/Data-Cleaning-in-python/assets/62595869/b391f978-a6df-482a-abe5-75635b58aab9)

## Table of Contents:-
1.0 Introduction
1.1 Signs of dirty data 
1.2 Python data cleaning - prerequisites
1.3 Import python  libraries
1.4 Import necessary csv file in pandas
1.5 check how many columns and rows are in your csv file
1.6 check column names in your data
1.7 Rename columns
1.8 check for null values
1.9 check for duplicates
2.0 drop duplicates
2.1 drop unnecessary columns
2.2 Check column datatypes
2.3 Reorder the column labels
2.4 Reset Index values
Conclusion

## 1. Introduction
Data cleaning means fixing bad data in your data set.

Bad data could be:

- Empty cells
- Data in wrong format
- Wrong data
- Duplicates
The cricket data used in this project can be found on https://www.espncricinfo.com/records/highest-career-batting-average-282910

## 1.1 Signs of dirty data 

### Missing numerical values 
Missing numerical data needs to be identified and addressed. Either they need to be deleted or replaced with a suitable test statistic.

### Inconsistent column names
Column names contain inconsistent capitalizations and bad characters. 

### Duplicate rows and columns
Duplicate rows and columns make data redundant. They can bias an analysis. Hence, they needs to be found and dropped.

### Unexpected data values
A column should have consistent data values. Columns cannot contain mixed data types.

## 1.2 Python data cleaning
- prerequisites
We need three Python libraries for the data cleansing process
- NumPy
- Pandas
- Matplotlib.
 
## 1.3 Import necesary libraries
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

```
## 1.4 Import necessary csv file to clean
```
df = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\cricket_data.csv')
```
## 1.5 check how many columns and rows make up your csv file
```
df.shape
```
## 1.6 check column names in your data 
```
df.columns
```
## 1.7 Rename columns to a more readable format
- df.head() shows the first five columns
```
df = df.rename(columns = {'Mat' : 'Match_played', 
                          'Inns' : 'Inning_batted',
                          'NO' : 'Not_outs',
                          'HS' : 'Highest_inns_score',
                          'Ave' : 'Batted_average',
                          'BF' : 'Balls_faced',
                          'SR' : 'Strike_rate',
                           })
df.head()
```
## 1.8 check for null values 
```
df.isna().any()
```
- df.isna() returns a boolean either true or false
- run .sum() to get the number of null values per column
```
df.isna().sum()
```
#### to view rows with null values
```
df[df['Balls_faced'].isna() == 1]
```
### Fill nan with a zero value for our case
```
df['Balls_faced'] = df['Balls_faced'].fillna(0)
```
### fill nan values with statistical values 
```
df[‘col_name’].replace(to_replace = NaN, value = median, inplace = True)

df['col_name'].fillna(value = median, inplace = True )
```

## 1.9 check for duplicates in your data frame
```
df[df.duplicated()]
```

## 2.0 drop the duplicated rows to have a dataset without duplicates
```
df.drop_duplicates(inplace = True)
```
## 2.1 drop unnecessary columns
```
df.drop('Span', axis = 1)
```
- By specifying **axis = 1** we mean its a column we need to drop and **axis = 0** means we want to drop a row

## 2.2 Check column datatypes
```
df.dtypes()
```
#### Convert a column to its data type
```
df['Highest_inns_score'] = df['Highest_inns_score'].astype('int')
```
#### covert multiple columns to a specific datatype
```
df = df.astype({'start_year' : 'int', 'end_year' : 'int'})
```

## 2.3 Reorder the column labels
```
df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]
```
## 2.4  Reset Index values for the rows (Optional)
- As our final step, we reset the index values for rows of the dataset.
```
df = df.reset_index(drop=True)
```

## Conclusion
Now, when we look at our data, we can see that there are no missing or negative values. 
Data cleaning is a crucial step in the data preprocessing pipeline.
It involves identifying and rectifying issues in your dataset to ensure that it’s ready for analysis.
