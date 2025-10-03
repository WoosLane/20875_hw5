import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])


# code for Question 1
print('Problem 1 Answers:')
# code below this line
mean_data = np.mean(data)
median_data = np.median(data)
std_dev_data = np.std(data, ddof=1)
print(f"Mean: {mean_data}")
print(f"Median: {median_data}")
print(f"Standard Deviation: {std_dev_data}")

# code for Question 2
print('Problem 2 Answers:')
# code below this line
n = len(data)
df = n - 1
confidence_level = 0.95
alpha = 1 - confidence_level

t_critical = t.ppf(1 - alpha / 2, df)

margin_of_error = t_critical * (std_dev_data / m.sqrt(n))

lower_bound = mean_data - margin_of_error
upper_bound = mean_data + margin_of_error

print(f"95% Confidence Interval for the Mean: ({lower_bound}, {upper_bound})")

# code for Question 3
print('Problem 3 Answers:')
# code below this line
population_mean = 140
t_statistic, p_value = t.ttest_1samp(data, population_mean)
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")
