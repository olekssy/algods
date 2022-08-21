""" Hypothesis testing primer. """

import numpy as np
import scipy.stats as st
from statsmodels.tsa.stattools import adfuller, kpss

# test size
alpha = 0.025  # size of a test
c_one = st.norm().ppf(1 - alpha)  # critical value
c_two = st.norm().ppf(1 - alpha / 2)  # two-sided critical value
print(f'alpha: {alpha}, c: {c_one:4.4f}, two-sided c: {c_two:4.4f}')

# distributions
n = 10  # size of distribution
a = np.random.normal(0, 1, n)
b = np.random.normal(2, 3, n)
print(f'E[a] = {a.mean():4.2f}, V[a] = {a.var():4.2f}, n = {n}')
print(f'E[b] = {b.mean():4.2f}, V[b] = {b.var():4.2f}, n = {n}')

# One-sided test
# tests if a distribution mu is less than or equal to hypothetical mu_hat
mu_hat = 1.0
h0 = f'Retain H0: distribution mu ({a.mean():4.4f}) ≤ mu_hat ({mu_hat})'
h1 = f'Reject H0: distribution mu ({a.mean():4.4f} > mu_hat ({mu_hat})'
# critical value for regecting H0 if mu > c_hat
c_hat = a.std() * c_one / np.sqrt(n) + mu_hat

if a.mean() > c_hat:
    print(h1)
    print(f'mean: {a.mean():4.4f} > c_hat ({c_hat:4.4f})')
else:
    print(h0)
    print(f'mean: {a.mean():4.4f} < c_hat ({c_hat:4.4f})')
print()

# Alternatively with one-sided t-test
t_stat, p_val = st.ttest_1samp(a, mu_hat, alternative='greater')
print('Alternatively:')
if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
    print(f't_stat: {t_stat:4.4f} > c ({c_one:4.4f})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
    print(f't_stat: {t_stat:4.4f} < c ({c_one:4.4f})')
print()

# One sample t-test
# tests if a distribution mu equals hypothetical mu_hat
h0 = f'Retain H0: mu ({a.mean():4.2f}) = mu_hat {mu_hat}'
h1 = f'Reject H0: mu ({a.mean():4.2f}) ≠ mu_hat {mu_hat}'
t_stat, p_val = st.ttest_1samp(a, mu_hat)

if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
    print(f't_stat: {abs(t_stat):4.4f} > c ({c_two:4.4f})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
    print(f't_stat: {abs(t_stat):4.4f} < c ({c_two:4.4f})')
print()

# Two sample t-test
# tests if the means of two independent samples are significantly different
h0 = f'Retain H0: mu(A) ({a.mean():4.4f}) = mu(B) ({b.mean():4.4f})'
h1 = f'Reject H0: mu(A) ({a.mean():4.4f}) ≠ mu(B) ({b.mean():4.4f})'
t_stat, p_val = st.ttest_ind(a, b)

if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
print()

# Pearson's test
# tests if two independent samples have a linear relationship
corr, p_val = st.pearsonr(a, b)
h0 = f'Retain H0: corr(A,B): {corr:4.2f} = 0.0'
h1 = f'Reject H0: corr(A,B): {corr:4.2f} ≠ 0.0'

if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
print()

# ADF unit root test
# tests if a time series is autoregressive
h0 = 'Retain H0: a unit root is present (series is non-stationary)'
h1 = 'Reject H0: a unit root is not present (series is stationary)'

adf_res = adfuller(np.random.randn(n))
t_stat = adf_res[0]
p_val = adf_res[1]

if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
print()

# KPSS test
# tests if a time series is trend stationary
h0 = 'Retain H0: the time series is trend-stationary'
h1 = 'Reject H0: the time series is not trend-stationary'

kpss_res = kpss(np.linspace(1, 3, n))
t_stat = kpss_res[0]
p_val = kpss_res[1]

if p_val < alpha:
    print(h1)
    print(f'p-value: {p_val:4.4f} < alpha ({alpha})')
else:
    print(h0)
    print(f'p-value: {p_val:4.4f} > alpha ({alpha})')
print()
