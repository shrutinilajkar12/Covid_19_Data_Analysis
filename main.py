import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from datetime import datetime 

df=pd.read_csv("state_level_daily.csv")
print(df)
# State_wise_report=df.groupby("State_Name")['Confirmed','Deceased','Recovered'].sum()
State_wise_report = df.groupby("State_Name")[['Confirmed', 'Deceased', 'Recovered']].sum()

print(State_wise_report)
print("\n\n")
print("State wise report of Covid-19\n")
print(State_wise_report)

print("\n\n")
print("State Wise confirmred cases in Ascending order\n")
State_wise_confirmed=State_wise_report['Confirmed'].sort_values(ascending=True)
State_wise_confirmed.to_excel('State_wise_confirmed.xlsx')
# print(State_wise_confirmed)
State_wise_Dceased=State_wise_report['Deceased'].sort_values(ascending=True)
State_wise_Dceased.to_excel('State_wise_Deceased.xlsx')

# print(State_wise_Dceased)
State_wise_recovered=State_wise_report['Recovered'].sort_values(ascending=True)
State_wise_recovered.to_excel('State_wise_recovered.xlsx')
print(State_wise_recovered)

swr=np.array(State_wise_report['Recovered'])
swd=np.array(State_wise_report['Deceased'])
swc=np.array(State_wise_report['Confirmed'])

plt.xlabel("Covid Cases")
plt.ylabel("Recovered and Deceased")
plt.plot(swd,color='k',lw=1.5,label='Death')
plt.plot(swr, color='m',lw=1.5,label='Recovered')
plt.plot(swc,color='r',lw=0.2,label="Confirmed",ls='-')
plt.legend()
plt.grid(True)
plt.show()

sn=pd.read_excel('State_wise_confirmed.xlsx').sort_values(by='Confirmed',ascending=False)
print(sn.head(10))
states=np.array(sn['State_Name'].head(10))
con_case=np.array(sn['Confirmed'].head(10))
print(states)
plt.axis('equal')
plt.pie(con_case,labels=states,autopct='%1.2f%%',shadow=True)
plt.legend()
plt.show()



df = pd.read_csv("state_level_daily.csv")
if not pd.api.types.is_datetime64_any_dtype(df['Date']):
    df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%d-%b-%y'))

df.sort_values(by='Date', inplace=True)

df.to_excel("state_level_daily_sorted.xlsx", index=False)
df['Month_Year'] = df['Date'].dt.to_period('M')
monthly_data = df.groupby('Month_Year').agg({'Confirmed': 'sum', 'Deceased': 'sum', 'Recovered': 'sum'})

monthly_data['Month_Year'] = monthly_data.index.strftime('%b-%Y')

plt.figure(figsize=(12, 8))

plt.plot(monthly_data['Month_Year'], monthly_data['Confirmed'], marker='o', linestyle='-', color='b', label='Confirmed')
plt.plot(monthly_data['Month_Year'], monthly_data['Recovered'], marker='o', linestyle='-', color='g', label='Recovered')
plt.plot(monthly_data['Month_Year'], monthly_data['Deceased'], marker='o', linestyle='-', color='r', label='Deceased')
plt.xlabel('Month')
plt.ylabel('Total Cases')
plt.title('Monthly Growth of COVID-19 Cases')
# plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


df = pd.read_excel('state_level_daily_sorted.xlsx')
df['Date'] = pd.to_datetime(df['Date'])
df['Recovery_Rate'] = (df['Recovered'] / df['Confirmed']) * 100
df['Death_Rate'] = (df['Deceased'] / df['Confirmed']) * 100
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Recovery_Rate'], label='Recovery Rate', color='green')
plt.plot(df['Date'], df['Death_Rate'], label='Death Rate', color='red')

plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.title('COVID-19 Recovery Rate and Death Rate Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

df['Date'] = pd.to_datetime(df['Date'])

df['Cumulative_Confirmed'] = df['Confirmed'].cumsum()
df['Cumulative_Recovered'] = df['Recovered'].cumsum()
df['Cumulative_Deceased'] = df['Deceased'].cumsum()

plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Cumulative_Confirmed'], label='Confirmed Cases', color='blue', alpha=0.7)
plt.fill_between(df['Date'], df['Cumulative_Recovered'], label='Recovered Cases', color='green', alpha=0.7)
plt.fill_between(df['Date'], df['Cumulative_Deceased'], label='Deaths', color='red', alpha=0.7)

plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Cumulative COVID-19 Cases Over Time')
plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

df['Recovery_Rate'] = (df['Recovered'] / df['Confirmed']) * 100
df['Confirmed_Rate'] = (df['Confirmed'] / df['Confirmed'].sum()) * 100
df['Death_Rate'] = (df['Deceased'] / df['Confirmed']) * 100
best_recovery_states = df.sort_values(by='Recovery_Rate', ascending=False).head(5)
worst_recovery_states = df.sort_values(by='Recovery_Rate').head(5)

best_confirmed_states = df.sort_values(by='Confirmed_Rate', ascending=False).head(5)
worst_confirmed_states = df.sort_values(by='Confirmed_Rate').head(5)
best_death_states = df.sort_values(by='Death_Rate').head(5)
worst_death_states = df.sort_values(by='Death_Rate', ascending=False).head(5)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10))
plt.subplots_adjust(hspace=0.5)
print("States with Best Recovery Rates:")
print(best_recovery_states[['State_Name', 'Recovery_Rate']])

print("\nStates with Worst Recovery Rates:")
print(worst_recovery_states[['State_Name', 'Recovery_Rate']])

print("\nStates with Best Confirmed Rates:")
print(best_confirmed_states[['State_Name', 'Confirmed_Rate']])

print("\nStates with Worst Confirmed Rates:")
print(worst_confirmed_states[['State_Name', 'Confirmed_Rate']])

print("\nStates with Best Death Rates:")
print(best_death_states[['State_Name', 'Death_Rate']])

print("\nStates with Worst Death Rates:")
print(worst_death_states[['State_Name', 'Death_Rate']])


# Plot best and worst recovery rates
best_recovery_states.plot(kind='bar', x='State_Name', y='Recovery_Rate', ax=axes[0, 0], color='green', legend=False)
worst_recovery_states.plot(kind='bar', x='State_Name', y='Recovery_Rate', ax=axes[0, 1], color='green', legend=False)
axes[0, 0].set_title('States with Best Recovery Rates')
axes[0, 1].set_title('States with Worst Recovery Rates')
axes[0, 0].set_ylabel('Recovery Rate (%)')
axes[0, 1].set_ylabel('Recovery Rate (%)')

# Plot best and worst confirmed rates
best_confirmed_states.plot(kind='bar', x='State_Name', y='Confirmed_Rate', ax=axes[1, 0], color='blue', legend=False)
worst_confirmed_states.plot(kind='bar', x='State_Name', y='Confirmed_Rate', ax=axes[1, 1], color='blue', legend=False)
axes[1, 0].set_title('States with Best Confirmed Rates')
axes[1, 1].set_title('States with Worst Confirmed Rates')
axes[1, 0].set_ylabel('Confirmed Rate (%)')
axes[1, 1].set_ylabel('Confirmed Rate (%)')

# Plot best and worst death rates
best_death_states.plot(kind='bar', x='State_Name', y='Death_Rate', ax=axes[2, 0], color='red', legend=False)
worst_death_states.plot(kind='bar', x='State_Name', y='Death_Rate', ax=axes[2, 1], color='red', legend=False)
axes[2, 0].set_title('States with Best Death Rates')
axes[2, 1].set_title('States with Worst Death Rates')
axes[2, 0].set_ylabel('Death Rate (%)')
axes[2, 1].set_ylabel('Death Rate (%)')

# Show the plots
plt.tight_layout()
plt.show()