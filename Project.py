'''
# Project - 1
# Step 1: Import necessary libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("telecom_customer_churn.csv")  # Telecom churn dataset
# Telecom churn dataset customer details

# Step 3: Basic structure of dataset
print("Dataset shape (rows,columns):- ",df.shape)
print("Dataset columns: ",df.columns)

#Step 4: View the first 5 records to understand the data
print(df.head()) 

#Step 5: Summary of the dataset (columns + datatype + non-null info.)
print(df.info())

#Step 6: Checking missing values in each columns
print(df.isnull().sum())

#Step 7: Basic statistics of numeric columns
print("Basic statistic information of the dataset \n: ",df.describe)

#Step 8: Count of unique values in categorical features:
for col in df.select_dtypes(include="object"):
    print(col,": ",df[col].nunique(),'unique values')

#Step 9: Plot distribution of 
ax = sns.countplot(x='Customer Status',data=df)
ax.bar_label(ax.containers[0]) # Shows the exact number of the each container
plt.title("Customer Status")
plt.show()

#Step 10: Plot gender distribution
plt.figure(figsize=(3,4))  # Adjusting the graph size
ax = sns.countplot(x='Gender',data= df)
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

#Step 11: Plotting the payment method
plt.figure(figsize=(5,5))  # Adjusting the graph size
ax = sns.countplot(x='Payment Method',data=df)
ax.bar_label(ax.containers[0])
plt.title("Customer's different method of payment")
plt.show()

#Bivariate Analysis (2 features at a time)
#Step 12: Customer status based on gender 
plt.figure(figsize=(4,5))
ax = sns.countplot(x='Customer Status',hue='Gender',data=df)
ax.bar_label(ax.containers[0])
plt.title('Status Based On Gender')
plt.show()

#Step 13: Customer Status based on payment method
plt.figure(figsize=(5,5))
ax = sns.countplot(x='Customer Status',hue='Payment Method',data=df)
ax.bar_label(ax.containers[0])
plt.title('Customer Status Based on Payment Method')
plt.show()

#Data Cleaning
#Step 14: Handling missing values
print(df.isnull().sum().sort_values(ascending=False)) #checking how many columns have missing values
#Multiple Lines is a categorial columns ,so the missing values are filled with mode
df['Multiple Lines'].fillna(df['Multiple Lines'].mode()[0],inplace=True) 
# Drop the columns which has not very important role in making insights or having high values
df.drop(columns=['Device Protection Plan','Streaming Music','Avg Monthly GB Download','Online Security','Online Backup','Device Protection Plan','Premium Tech Support','Streaming TV','Streaming Movies','Unlimited Data'],inplace=True)

df['Offer'].fillna(df['Offer'].mode()[0],inplace=True)
df['Churn Category'].fillna(df['Churn Category'].mode()[0],inplace=True)
df['Churn Reason'].fillna(df['Churn Reason'].mode()[0],inplace=True)
df['Internet Type'].fillna(df['Internet Type'].mode()[0],inplace=True)
df['Avg Monthly Long Distance Charges'].fillna(df['Avg Monthly Long Distance Charges'].mode()[0],inplace=True)
# Check Again
print(df.isnull().sum())

#Feature Engineering 
# Step 15: Cleaning the data by converting the spaces in NaN
df['Total Charges'] = pd.to_numeric(df['Total Charges'],errors='coerce')  
print(df['Total Charges'].dtype)
print(df["Total Charges"].isnull().sum())
#Unique ID is not necessary for analysis data
df.drop('Customer ID',axis=1,inplace=True)
print('Customer ID' in df.columns)
# Step 16: converting the categorial to numeric values
df = pd.get_dummies(df,drop_first=True)
print(df.columns)

#Final Output Summary
#Step 17: Final Cleaned Dataset Info
print("Final dataset shape:",df.shape)
print("Final dataset perivew: \n",df.head())
'''

#Project - 2
#ATM Machine
#atm card ko enter kar
#jitni cash chiya amount enter kar
#Password fill kar
#apki payment done

print("Welcome TO The Online ATM")
card_num = [101,102,103,104,105]
Customer_details = {
    "card" : [101,102,103,104,105],
    "names" : ['sonu','sumit','anil','ayush','lokesh'],
    "T_amount" : [200000,365000,47000,10000,39020,],
    "password" : [1234,4322,8767,3457,9770]
}
card = int(input("Enter the card number: "))
#idx = Customer_details['card'].index(card)
#password = Customer_details['password'][idx]
import sys
if card in card_num:
        index = Customer_details['card'].index(card)
        idx = Customer_details['card'].index(card)
        password = Customer_details['password'][idx]
        print("Name: ",Customer_details['names'][index],"\n","Total Amount: ",Customer_details['T_amount'][index])
else:
        print("Your card number is wrong or May be not registerd at our bank")
        sys.exit()

print("What do you want? ")
nxt = input("Deposite or Withdraw the money: ")
if nxt == "Deposite" or nxt == "Withdraw":
        amt = int(input("Enter your amount: "))
        print(amt)
else: 
     print("Somthing went wrong")
     sys.exit()
    
pswrd = int(input("Please enter your password: "))
if pswrd == password:
        if nxt == "Deposite":
                print("congratulations!"," \n"," Your Transaction is done.")
        elif nxt=="Withdraw":
                        print("Withdrawl successful!")
else:
                print("You enter the wrong password")
                sys.exit()


