# ROE
# ROE Analysis 2

# ROE Analysis 1
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.rc('font', family='Microsoft JhengHei')

company = 'WBA'
years = 5
current_year = 2022
date = np.arange(current_year-years+1, current_year+1)
with open('./API.txt', 'r', encoding='utf-8') as f:
    API = f.read()
#print(date)
balance_sheet = requests.get(f'http://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={API}')
balance_sheet = balance_sheet.json()
#print(balance_sheet[0].keys())



income_statement = requests.get(f'http://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={API}')
income_statement = income_statement.json()
#print(income_statement[0].keys())


# revenue = list(reversed([income_statement[i]['revenue'] for i in range(len(date))]))
# revenue = [i / 1000000000 for i in revenue]

# net_income = list(reversed([income_statement[i]['netIncome'] for i in range(len(income_statement))]))
# net_income = [ i / 1000000000 for i in net_income]

# totalAssets = list(reversed([balance_sheet[i]['totalAssets'] for i in range(len(date))]))

# TL = list(reversed([balance_sheet[i]['totalLiabilities'] for i in range(len(balance_sheet))]))
# TL = [i / 1000000000 for i in TL]
# print(income_statement[0]['netIncome'] / balance_sheet[0]['totalStockholdersEquity'])
# verify = (balance_sheet[0]['totalLiabilities'] / balance_sheet[0]['totalStockholdersEquity']+1)*(income_statement[0]['netIncome']/income_statement[0]['revenue'])*(income_statement[0]['revenue'] / balance_sheet[0]['totalAssets'])
# print(verify)
#ROE = 淨利/權益總額
ROE = list(reversed([income_statement[i]['netIncome'] / balance_sheet[i]['totalStockholdersEquity'] for i in range(len(balance_sheet))]))
#Debt to Equity Ratio
DER = list(reversed([balance_sheet[i]['totalAssets'] / balance_sheet[i]['totalStockholdersEquity'] for i in range(len(balance_sheet))]))
# Net Profit Margin(淨利潤率)=net_income/revenue
NPM = list(reversed([income_statement[i]['netIncome'] / income_statement[i]['revenue'] for i in range(len(date))]))
#Asset Turnover(資產週轉率)=revenue/total_assets
AT = list(reversed([income_statement[i]['revenue'] / balance_sheet[i]['totalAssets'] for i in range(len(date))]))

#plt.subplot(3, 1, 1)

plt.bar(date, ROE)
for i in range(len(date)):
    plt.text(date[i]-0.5, ROE[i], f'{ROE[i]:.2%}')
#plt.xticks([i for i in range(years)], [i for i in range(2013, 2023)])
plt.xticks(date)
plt.xlabel('Year')
plt.ylabel('ROE')
plt.title(f'{company} 股東權益報酬率(ROE)')
plt.show()

# #plt.subplot(3, 1, 2)
# plt.plot(date, TSE, color='g', label="Shareholder's Equity")
# plt.plot(date, net_income,color='b', label="Net Income")
# plt.plot(date, TL,color='r', label="Total Libilities")
# #for i in range(len(date)):
# #    plt.text(date[i], TSE[i], f'{TSE[i]:.2f}')
# plt.legend(loc='best')
# plt.xticks(date)
# plt.xlabel('Year')
# plt.ylabel("USD in Billions")
# #plt.title(f"{company} Total Stock Holder's Equity")
# plt.show()
ax1 = plt.subplot()
ax1.plot(date, DER, color='b', label="財務槓桿")
# for i in range(len(date)):
#     plt.text(date[i], DER[i], f'{DER[i]:.2%}')
ax1.plot(date, AT, color='r', label="資產週轉率")
# for i in range(len(date)):
#     plt.text(date[i], AT[i], f'{AT[i]:.2%}')
ax1.legend(loc='upper left')
ax1.set_xlabel('Year')
ax1.set_ylabel('財務槓桿 & 資產週轉率')
ax1.grid()

ax2 = ax1.twinx() #創建第二個Y軸
ax2.plot(date, NPM, color='g', label="淨利潤率", linestyle='--')
# for i in range(len(date)):
#     plt.text(date[i], NPM[i], f'{NPM[i]:.2%}')
ax2.set_ylabel('淨利潤率', color='g')
ax2.legend(loc='upper right')

plt.title(f'{company} 財務分析')
plt.show()



# 正規化函數
def normalize(data):
    return [(i - min(data)) / (max(data) - min(data)) for i in data]

# 正規化數據
DER_normalized = normalize(DER)
NPM_normalized = normalize(NPM)
AT_normalized = normalize(AT)

# 繪製正規化後的數據
plt.plot(date, DER_normalized, label="財務槓桿", color='b')
plt.plot(date, NPM_normalized, label="淨利潤率", color='g')
plt.plot(date, AT_normalized, label="資產週轉率", color='r')

plt.legend(loc='best')
plt.xticks(date)
plt.xlabel('Year')
plt.ylabel('Normalized Value')
plt.title(f'{company} 財務分析 (正規化)')
plt.grid()
plt.show()

