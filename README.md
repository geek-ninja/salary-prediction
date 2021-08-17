# salary-prediction
<h2>Prediction of Salary of employees using simple regression model and storing the data in django database with a frontend input page</h2>

<p>code snippet</p>

```python
from django.shortcuts import render
import joblib
import pandas as pd
from .utils import get_plot
from django.core.files.storage import FileSystemStorage
import os
from .models import SalaryRecord
from .simple_linear_regression import model
import pandas as pd

def home_view(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        uploaded_file.name = 'Salary_Data.csv'
        if (os.path.isfile('model/Salary_Data.csv')):
            os.remove('model/Salary_Data.csv')
            print('done')
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        url = fs.url(name)
        context['url'] = url

    return render(request,"ml/slr.html",context)

def result_view(request):
    
    # if os.path.isfile('model/Salary_Data.csv'):
    #     dataset = pd.read_csv('model/Salary_Data.csv')
    #     df = pd.DataFrame(dataset)
    #     x = dataset.iloc[:,:-1].values
    #     y = dataset.iloc[:,1].values
        
    obj = SalaryRecord.objects.all()
    
    x = [[i.experience] for i in obj]
    y = [[i.salary] for i in obj]
    print(x)
    reg = model(obj)
    lis = []
    lis.append(request.GET['exp'])
    salary = reg.predict([lis])
    chart = get_plot(x,y,reg.predict(x))      
    # else:
    #     chart = False
    #     salary = ['Dataset is not uploaded']
    
    return render(request,"ml/slr_result.html",{'salary':salary[0][0],'chart':chart})



```

<h3>screen shot</h3>

![](1.png)

![](2.png)
