#!/usr/bin/env python
# coding: utf-8

# In[8]:


#CALCULATE NPV FOR TWO PROJECTS
#===============================

#Import a plotting library:
import matplotlib.pyplot as plt

# Project Apollo Cash Flows Here
project_apollo = [-1000000, 0, 0, 50000, 50000, 200000, 250000, 250000, 250000, 250000, 375000, 375000, 375000, 375000, 375000, 250000, 250000, 250000, 250000, 100000]

# Project Beta Cash Flows Here
project_beta = [-1000000, 50000, 50000, 50000, 50000, 250000, 500000, 500000, 500000, 500000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]

discount_rate = [0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18]

#CALCULATION FOR NPV:
def calculate_npv(rate, cash_flow):
    npv = 0
    for t in range(len(cash_flow)):
        npv += cash_flow[t]/(1+rate)**t
    return npv

npvs_apollo = list()
npvs_beta = list()
for rate in discount_rate:
  npv_apollo = calculate_npv(rate,project_apollo)
  npvs_apollo.append(npv_apollo)
  npv_beta = calculate_npv(rate,project_beta)
  npvs_beta.append(npv_beta)
  
plt.plot(discount_rate,npvs_apollo, linewidth = 2.0, color = "red", label = "Project Apollo")
plt.plot(discount_rate,npvs_beta, linewidth = 2.0, color = "blue", label = "Project Beta")
plt.axhline(y=0, linewidth = 0.5, color = "black")
plt.title('NPV Profile for Projects Apollo and Beta')
plt.xlabel('Discount Rate')
plt.ylabel('Net Present Value')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




