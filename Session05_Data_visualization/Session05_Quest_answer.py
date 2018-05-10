from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

#Reading Data
bodydims = pd.read_csv("bodydims.csv")
hr = pd.read_csv('HR_comma_sep.csv')
weather = pd.read_csv('월별_기온및강수량_서울.csv')

plt.figure(figsize=(12,7))


plt.style.use("ggplot")

# Scatter Plot
plt.subplot(221)
bii = pd.Series(map(float, bodydims["bii.di"]))
che = pd.Series(map(float, bodydims["che.de"]))
plt.scatter(bii, che, marker = '.', color = 'g')

plt.title("waist measurement - weight")
plt.xlabel("waist")
plt.ylabel("weight")


# Histogram
plt.subplot(222)
age = pd.Series(map(float, bodydims["age"]))
plt.hist(age, bins = 20)
plt.title("Patients' Age Distribution")
plt.xlabel("Age")
plt.axvline(x=age.mean(), color = 'c', linestyle = 'dashed')



# Bar Chart
plt.subplot(223)
departments = list(Counter(hr["sales"]).keys())
num_employee = [Counter(hr["sales"])[departments[i]] for i in range(0, len(departments))]
plt.bar(departments[:6], num_employee[:6], color = 'c')

plt.title("Employee Number per Department")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")



# Simple Plot
plt.subplot(224)

months = list(range(1,13))

monthly_temp_low = list(weather.iloc[0])[1:]
monthly_temp_high = list(weather.iloc[1])[1:]
#iloc[n]은 dataframe의 n번째 행을 return

print(months)
print(monthly_temp_high)

plt.plot(months, monthly_temp_high, marker = 'x', linestyle = 'solid')
plt.plot(months, monthly_temp_low, marker = '.', linestyle = 'dashed')

plt.title("Average Monthly Temperature (Seoul)")
plt.xlabel("Months")
plt.ylabel("Temperature(℃)")
plt.legend(loc = 'best')

plt.show()







