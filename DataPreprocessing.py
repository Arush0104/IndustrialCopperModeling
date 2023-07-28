import pandas as pd
from matplotlib import pyplot as plt


#-----------------Data preprocessing starts here---------------------------#

df = pd.read_excel('copper.xlsx')
i=1
df1 = df.fillna(value=0)
while i<156150:
    col=str(df1.loc[i,'material_ref'])
    col1=df1.loc[i,'quantity_tons']
    col2=df1.loc[i,'selling_price']
    col3 = str(df1.loc[i,'status'])
    if len(col)>35:
        df1['material_ref'].replace([col],[0], inplace=True)
    if type(col1)==str:
        df1['quantity_tons'].replace([col1],[0], inplace=True)
    if col2<0:
        df1['selling_price'].replace([col2],[0], inplace=True)
    if len(col3)>4:
        df1['status'].replace([col3],[0], inplace=True)
        
    i=i+1


q1=df1['quantity_tons'].quantile(0.25)
q3=df1['quantity_tons'].quantile(0.75)
iqr = q3-q1
lower_limit=q1-1.5*iqr
higher_limit=q3+1.5*iqr

df_no_outlier_quantity_tons = df1[(df1.quantity_tons>lower_limit) & (df1.quantity_tons<higher_limit)]


Q1=df1['selling_price'].quantile(0.25)
Q3=df1['selling_price'].quantile(0.75)
IQR = Q3-Q1
Lower_limit=Q1-1.5*IQR
Higher_limit=Q3+1.5*IQR
df_no_outlier_selling_price = df_no_outlier_quantity_tons[(df_no_outlier_quantity_tons.selling_price>Lower_limit) & (df_no_outlier_quantity_tons.selling_price<Higher_limit)]


df_no_outlier_selling_price.to_excel('C:/Users/jimmy/Desktop/c/copper3.xlsx')

print("succ")
#seaborn visualisation for quantity_tons
"""
#sns.boxplot(df_no_outlier_selling_price['quantity_tons'])
plt.scatter(data=df_no_outlier_selling_price, x='selling_price', y='quantity_tons')
plt.rcParams['figure.figsize']=(150,150)
plt.ylim(-50,160)
plt.xlim(250,1450)
plt.show()
sns.distplot(sqrt_quantity_tons)
plt.show()
#bins=[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15]
#plt.hist(sqrt_selling_price,bins=bins)
#plt.hist(sqrt_quantity_tons,bins=bins)
#plt.show()
"""
#-----------------Data preprocessing ends here---------------------------#





























