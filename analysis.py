# Importing required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid") #Setting visual grid style

print("Libraries imported successfully.")

file_path = 'train.csv'

try:
    df = pd.read_csv(file_path) # Fetching the properly formatted dataset from csv file and storing it in a variable df
    print('Data loaded successfully. DataFrame/DataSet Info Details : ')
    df.info() # Fetching details related to the dataset using info()
    print("\nFirst 5 rows of the dataset:")
    print(df.head()) # getting first five rows of data set as sample using head()

    print('/nMissing Values : ', df.isnull().sum()) # checking for null values using isnull() While sum() helps getting the number of it
    df.dropna(subset = ['Postal Code'], inplace=True) # removing null value rows from dataset using dropna() While subset asks for only missing values in Postal Code and inplace=True means if null is there in the place
    print('/nMissing Values Handled: ')
    df.info() #rechecking dataframe after handling missing values

    category_sales = df.groupby('Category')['Sales'].sum().reset_index() #Fetching categorical sales by selecting to group by category taking sum of sales in each category then reseting the index to return dataset to orignal state
    print(f'Category Sales Without Sort: \n{category_sales}')
    category_sales = category_sales.sort_values(by=['Sales'], ascending=False) # sorting the categorical sales data by descending order
    print(f'Categorical Sales DataSet : {category_sales}') # returning properly formatter categorical sales data

    print('Plotting Data : ')
    plt.figure(figsize = (10,6)) #plotting a graph of size x=10,y=6
    sns.barplot(
        x='Sales',
        y='Category',
        data=category_sales,
        order=category_sales['Category'],
        errorbar=None,
    ) #assigning sales as x axis and category as y axis from categorical_sales data then Will label both axis and plt and atlast will show the outcome.
    plt.title('Categorical Sales')
    plt.xlabel('Category')
    plt.ylabel('Sales')
    plt.show()

    df['Order Date'] = pd.to_datetime(df['Order Date'], format = '%d/%m/%Y') # Conversion of Order Date to proper DateTime format.
    df['Order Month'] = df['Order Date'].dt.to_period('M') # Adding a column that will contain then month of sale
    print('Converted Order Date to datetime format and added Order Month Column')
    monthly_sales = df.groupby('Order Month')['Sales'].sum().reset_index() # Creating a monthly sales dataset from main dataset by grouping order month and taking the sum of all sales in each
    monthly_sales['Order Month'] = monthly_sales['Order Month'].astype(str) # Converting Order Month back to str to create a chart
    print(f'Monthly Sales DataSet : {monthly_sales}')
    print('Plotting monthly sales trend data : ')

    plt.figure(figsize = (15,7)) # setting size of chart of 15*7
    sns.lineplot(x='Order Month',y='Sales', data=monthly_sales, marker='o')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    sub_categorical_sales = df.groupby('Sub-Category')['Sales'].sum().reset_index()
    sub_categorical_sales = sub_categorical_sales.sort_values(by=['Sales'], ascending=False)
    print(f'Sub-Categorical Sales DataSet : {sub_categorical_sales}'
          f'\nSub-Categorical Sales DataSet Info : ')
    sub_categorical_sales.info()
    print('Plotting sub-categorical sales data : ')
    plt.figure(figsize = (17,10))
    sns.barplot(x='Sub-Category',y='Sales', data=sub_categorical_sales)
    plt.title('Sub-Categorical Sales Data')
    plt.xlabel('Sub-Category')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(e)