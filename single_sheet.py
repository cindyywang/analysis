import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_excel(file, name_sheet):
	return pd.read_excel(file, sheet_name = name_sheet, index_col = 0, comment='#')

def print_1st_n_rows(n, some_df):
	print(some_df.head(n))

def unique_agents(some_df):
	return len(some_df['Buyer'].unique())

def agent_order_counts(some_df):
	print(some_df['Buyer'].value_counts())
	sns.countplot(data=some_df, x='Buyer').figure.savefig("agent_order_counts.png")

def catplot(some_df, x_axis, y_axis, kind_type):
	sns.catplot(data=some_df, x = x_axis, y = y_axis, kind= kind_type).savefig(kind_type +".png")

def main():
	
	sp_purchase_df = read_excel('Order Managment Overview.xlsx', 'SP Sales')
	print_1st_n_rows(10, sp_purchase_df)
	num_agents = unique_agents(sp_purchase_df)
	print(num_agents)
	agent_order_counts(sp_purchase_df)
	catplot(sp_purchase_df, "Contract Value" , "Fapiao Date", "violin")

if __name__ == '__main__':
	main()
	