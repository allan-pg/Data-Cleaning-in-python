# Data Cleaning in python
## Introduction
Data cleaning means fixing bad data in your data set.

Bad data could be:

- Empty cells
- Data in wrong format
- Wrong data
- Duplicates
The cricket data used in this project can be found on https://www.espncricinfo.com/records/highest-career-batting-average-282910

## Signs of dirty data 

### Missing numerical values 
Missing numerical data needs to be identified and addressed. Either they need to be deleted or replaced with a suitable test statistic.

### Inconsistent column names
Column names contain inconsistent capitalizations and bad characters. 

### Duplicate rows and columns
Duplicate rows and columns make data redundant. They can bias an analysis. Hence, they needs to be found and dropped.

### Unexpected data values
A column should have consistent data values. Columns cannot contain mixed data types.

### Python data cleaning
 - prerequisites
We need three Python libraries for the data cleansing process –
- NumPy
- Pandas
- Matplotlib.
