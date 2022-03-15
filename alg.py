import pandas as pd
import numpy as np 
from catboost import CatBoostClassifier

covid_detect_model = CatBoostClassifier().load_model('covid_model_v2')
covid_stages_model = CatBoostClassifier().load_model('covid_stage_model')

def predictor(path):
    predictions = []
    data = np.array(pd.read_csv(path))
    for d in data:
        prediction1 = covid_detect_model.predict(d)
        if prediction1 == 0:
            prediction2 = covid_stages_model.predict(d)
            if prediction2 == 1:
                predictions.append('Тест положительный. Слабое повреждение лёгких')
            elif prediction2 == 2:
                predictions.append('Тест положительный. Среднее повреждение лёгких')
            elif prediction2 == 3:
                predictions.append('Тест положительный. Критическое повреждение лёгких')
        else:
            predictions.append('Тест отрицательный.')
    results = pd.DataFrame({'Patient': [i for i in range(len(predictions))], 'Result': predictions})
    results.to_csv('result.csv')
