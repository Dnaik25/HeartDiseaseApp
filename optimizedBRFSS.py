import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from imblearn.over_sampling import SMOTENC
from imblearn.under_sampling import NeighbourhoodCleaningRule
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.cluster import KMeans
from sklearn import tree
from sklearn.metrics import classification_report, recall_score, precision_score,f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from imblearn.ensemble import EasyEnsembleClassifier
from sklearn.metrics import roc_curve, roc_auc_score, auc
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import learning_curve
from imblearn.pipeline import Pipeline
import xgboost as xgb
import pickle

df = pd.read_csv('BRFSS_reduced_v3.csv')

X = df.drop('Heart_disease', axis=1)
y = df['Heart_disease']


skf = StratifiedKFold(n_splits=5, shuffle=False)

def SMOTENCL_BRFSS(X, y):
    smote_nc = SMOTENC(categorical_features= np.arange(0,13), random_state=42)
    X_resampled, y_resampled = smote_nc.fit_resample(X, y)

    ncr = NeighbourhoodCleaningRule(n_neighbors=5, threshold_cleaning=0.5)
    X_cleaned, y_cleaned = ncr.fit_resample(X_resampled, y_resampled)

    return X_cleaned, y_cleaned

def evaluate_classifier_brfss(clf, X, y):
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)
    f1_scores = []
    precisions = []
    recalls = []

    for train_idx, test_idx in skf.split(X, y):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_test, y_test = X.iloc[test_idx], y.iloc[test_idx]
        X_train_resampled, y_train_resampled = SMOTENCL_BRFSS(X_train, y_train)

        clf.fit(X_train_resampled, y_train_resampled)
        y_pred = clf.predict(X_test)

        fpr, tpr, _ = roc_curve(y_test, y_pred)
        tprs.append(np.interp(mean_fpr, fpr, tpr))

        tprs[-1][0] = 0.0

        aucs.append(auc(fpr, tpr))
        f1_scores.append(f1_score(y_test, y_pred))
        precisions.append(precision_score(y_test, y_pred))
        recalls.append(recall_score(y_test, y_pred))


    metrics = {
        "Average AUROC": np.mean(aucs),
        "Average F1 scores": np.mean(f1_scores),
        "Precision": np.mean(precisions),
        "Recall": np.mean(recalls)
    }

    return metrics, clf


lr_clf_brfss = LogisticRegression(max_iter=1000, random_state=42)

metrics, trained_model = evaluate_classifier_brfss(lr_clf_brfss, X, y)

def save_model(clf, filename):
    with open(filename, 'wb') as file:
        pickle.dump(clf, file)

save_model(trained_model, "HeartDiseaseModel.pkl")