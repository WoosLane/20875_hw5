import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

myFile = open('city_vehicle_survey.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()


# code for question 2
print('Problem 2 Answers:')
# code below this line
mean_data1 = np.mean(data1)
median_data1 = np.median(data1)
std_dev_data1 = np.std(data1, ddof=1)
print(f'Mean: {mean_data1}')
print(f'Median: {median_data1}')
print(f'Standard Deviation: {std_dev_data1}')

# code for question 3
print('Problem 3 Answers:')
# code below this line
myFile1 = open('vehicle_data_1.txt')
myFile2 = open('vehicle_data_2.txt')
data1 = myFile1.readlines()
data2 = myFile2.readlines()
data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()

t_stat, p_value = t.ttest_ind(data1, data2, equal_var=False)
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

# code for question 5
print('Problem 5 Answers:')
# code below this line
shapiro_data1 = stats.shapiro(data1)
shapiro_data2 = stats.shapiro(data2)

print(f"Shapiro-Wilk Test for Vehicle Data 1: Statistic={shapiro_data1.statistic}, P-value={shapiro_data1.pvalue}")
print(f"Shapiro-Wilk Test for Vehicle Data 2: Statistic={shapiro_data2.statistic}, P-value={shapiro_data2.pvalue}")

if shapiro_data1.pvalue > 0.05:
    print("Vehicle Data 1 appears to be normally distributed (fail to reject H0).")
else:
    print("Vehicle Data 1 does not appear to be normally distributed (reject H0).")

if shapiro_data2.pvalue > 0.05:
    print("Vehicle Data 2 appears to be normally distributed (fail to reject H0).")
else:
    print("Vehicle Data 2 does not appear to be normally distributed (reject H0).")

myFile1 = open('vehicle_data_1.txt')
data1 = myFile1.readlines()

myFile2 = open('vehicle_data_2.txt')
data2 = myFile2.readlines()

data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()












