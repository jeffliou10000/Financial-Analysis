# Free Cash Flow

company = 'WBA'
years = 10
date = []
with open('./API.txt', 'r', encoding='utf-8') as f:
    API = f.read()
cash_flow = requests.get(f'http://financialmodelingprep.com/api/v3/cash-flow-statement/{company}?limit={years}&apikey={API}')
cash_flow = cash_flow.json()
df = pd.DataFrame(cash_flow)
#print(df)
#print(cash_flow[0].keys())
for i in range(years):
    date.append(2022-i)
date = sorted(date)
fcf = list(reversed([cash_flow[i]['freeCashFlow'] for i in range(len(cash_flow))]))
fcf = [i / 1000000000 for i in fcf]
plt.bar(date, fcf)

for i in range(len(date)):
    plt.text(date[i], fcf[i], f'{fcf[i]:.2f}')
#plt.xticks([i for i in range(years)], [i for i in range(2013, 2023)])
plt.xticks(date)
plt.ylabel('USD(in Billions)')
plt.xlabel('Year')
plt.title(f'{company} Free Cash Flow')
plt.show()