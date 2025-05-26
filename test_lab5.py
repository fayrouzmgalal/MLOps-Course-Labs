#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

url = "http://localhost:8000/docs#/"

# Example input matching your model features
test_data = {
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Female",
    "Age": 35,
    "Tenure": 5,
    "Balance": 60000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000.0
}

response = requests.post(url, json=test_data)

print("Status Code:", response.status_code)
print("Response:", response.json())


# In[ ]:




