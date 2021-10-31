import joblib
import numpy as np
from .helper import l1, disease

# NB = joblib.load(".NB.pkl")
RF = joblib.load("E:/myStuff/django/mlapi/MyAPI/RF.pkl")


def predict(symptoms):
    NB = joblib.load("E:/myStuff/django/mlapi/MyAPI/NB.pkl")
    totalSymptoms = len(l1)
    isSymptoms = np.zeros(totalSymptoms)

    for symptomId in range(totalSymptoms):
        for symptom in symptoms:
            if symptom == l1[symptomId]:
                isSymptoms[symptomId] = 1

    predictedDiseaseId = NB.predict([isSymptoms])[0]

    predictedDisease = disease[predictedDiseaseId]

    return predictedDisease
