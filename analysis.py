# Importing required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid") #Setting visual grid style

print("Libraries imported successfully.")

file_path = 'train.csv'

try:
    df = pd.read_csv(file_path) # Fetching the properly formatted dataset from csv file and storing it in a variable df
    print('Data loaded successfully. DataFrame/DataSet Info Details : ', df.info()) # Fetching details related to the dataset using info()
    print("\nFirst 5 rows of the dataset:")
    print(df.head()) # getting first five rows of data set as sample using head()
    print('/nMissing Values : ', df.isnull().sum()) # checking for null values using isnull() While sum() helps getting the number of it
    df.dropna(subset = ['Postal Code'], inplace=True) # removing null value rows from dataset using dropna() While subset asks for only missing values in Postal Code and inplace=True means if null is there in the place
    print('/nMissing Values Handled: ',df.info()) #rechecking dataframe after handling missing values
    category_sales = df.groupby('Category')['Sales'].sum().reset_index #Fetching categorical sales by selecting to group by category taking sum of sales in each category then reseting the index to return dataset to orignal state
    category_sales = df.sort_values(by=['Sales'], ascending=False) # sorting the categorical sales data by descending order
    print(f'Categorical Sales DataSet : {category_sales}') # returning properly formatter categorical sales data
    print('Plotting Data : ')
    plt.figure(figsize = (10,6)) #plotting a graph of size x=10,y=6
    sns.barplot(
        x='Sales',
        y='Category',
        data=category_sales,
        order=category_sales['Category'],
        errorbar=None,
    ) #assigning sales as x axis and category as y axis from categorical_sales data
    plt.title('Categorical Sales')
    plt.xlabel('Category')
    plt.ylabel('Sales')
    plt.show()


except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(e)