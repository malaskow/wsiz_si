import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


curr_exchange = pd.read_json('http://api.nbp.pl/api/exchangerates/rates/A/USD/2019-09-01/2019-09-30/')


def load_from_range(date_from, date_to, currency='USD'):
    data = pd.read_json(f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date_from}/{date_to}/')
    data['effectiveDate'] = data['rates'].map(lambda d: d['effectiveDate'])
    data['mid'] = data['rates'].map(lambda d: d['mid'])
    data.drop('rates', axis=1, inplace=True)
    data = data.set_index(['effectiveDate'])
    return data


usd = load_from_range('2019-09-01', '2019-09-30')
chf = load_from_range('2019-09-01', '2019-09-30', 'chf')

chf = chf.rename(columns={'mid': 'chf_mid'})
together = usd.merge(chf, left_index=True, right_index=True)
print("Correlation")
print(np.corrcoef(together['mid'], together['chf_mid']))

print("Normal plot")

diag = together['mid']

diag2 = together['chf_mid']
plt.plot(diag, label='USD')
plt.tick_params(axis='x', rotation=70)
plt.xlabel('Effective Date')
plt.ylabel('Mid')

plt.plot(diag2, label='CHF')
plt.legend(loc='upper left')

plt.show()

print("Subplots")
fig, ax = plt.subplots(3, 1, tight_layout=True)

usd.plot(ax=ax[0])
chf.plot(ax=ax[1])

usd.plot(ax=ax[2])
chf.plot(ax=ax[2])
for i in ax:
    i.set_xlabel('Effective Date')
    i.set_ylabel('Mid')

ax[0].legend(['USD'], loc='upper left')
ax[1].legend(['CHF'], loc='upper left')
ax[2].legend(['USD', 'CHF'], loc='upper left')
ax[2].set_title('Together')

fig.show()

