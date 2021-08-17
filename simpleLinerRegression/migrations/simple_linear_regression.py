#Dataset template

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from .models import SalaryRecord

def model(obj):
    
    obj = SalaryRecord.objects.all()
    x = [[i.experience] for i in obj]
    y = [[i.salary] for i in obj]
    
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 1/3,random_state = 0)

    #fitting linear regression model
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(x_train,y_train)
    return regressor