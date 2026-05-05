import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_val_score
from sklearn.metrics import (
    r2_score, mean_squared_error,
    accuracy_score, precision_score,
    recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, auc
)

from xgboost import XGBRegressor, XGBClassifier

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("/workspaces/NanoToX/dataset.csv")

# Targets
y = df[['% Cell viability', 'toxicity class encoded']]

# Features
X = df.drop(columns=['% Cell viability', 'toxicity class encoded', 'toxicity class'])

# Split targets
y_reg = y['% Cell viability']
y_clf = y['toxicity class encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

y_train_reg = y_train['% Cell viability']
y_test_reg = y_test['% Cell viability']

y_train_clf = y_train['toxicity class encoded']
y_test_clf = y_test['toxicity class encoded']

# ===============================
# Regression Model Training
# ===============================

print("Training Regression Model...")

xgb_reg = XGBRegressor(random_state=42)

param_grid_reg = {
    'n_estimators': [500, 1000],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 6, 9],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

grid_search_reg = GridSearchCV(
    estimator=xgb_reg,
    param_grid=param_grid_reg,
    scoring='neg_mean_squared_error',
    cv=5,
    verbose=2,
    n_jobs=-1
)

grid_search_reg.fit(X_train, y_train_reg)

best_reg_model = grid_search_reg.best_estimator_

print("Best Regression Params:", grid_search_reg.best_params_)

# Regression Evaluation
y_pred_reg = best_reg_model.predict(X_test)

print("Regression R2:", r2_score(y_test_reg, y_pred_reg))
print("Regression MSE:", mean_squared_error(y_test_reg, y_pred_reg))

# ===============================
# Classification Model Training
# ===============================

print("Training Classification Model...")

xgb_clf = XGBClassifier(
    use_label_encoder=False,
    eval_metric='mlogloss',
    random_state=42
)

param_grid_clf = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

grid_search_clf = GridSearchCV(
    estimator=xgb_clf,
    param_grid=param_grid_clf,
    scoring='accuracy',
    cv=3,
    verbose=2,
    n_jobs=-1
)

grid_search_clf.fit(X_train, y_train_clf)

best_clf_model = grid_search_clf.best_estimator_

print("Best Classification Params:", grid_search_clf.best_params_)

# Classification Evaluation
y_pred_clf = best_clf_model.predict(X_test)

print("Classification Accuracy:", accuracy_score(y_test_clf, y_pred_clf))
print(classification_report(y_test_clf, y_pred_clf))

# ===============================
# Cross Validation Check
# ===============================

kf = KFold(n_splits=5, shuffle=True, random_state=42)

cv_scores_reg = cross_val_score(
    best_reg_model, X, y_reg, cv=kf, scoring='r2'
)

print("Regression CV Mean R2:", cv_scores_reg.mean())

# ===============================
# Save Models
# ===============================

joblib.dump(best_reg_model, "xgb_regressor_model.pkl")
joblib.dump(best_clf_model, "xgb_classifier_model.pkl")

print("Models saved successfully.")

# ===============================
# Prediction Tool Function
# ===============================

def predict_toxicity(input_csv_path):
    """
    Prediction tool function.

    Parameters
    ----------
    input_csv_path : str
        Path to new dataset CSV

    Returns
    -------
    regression_prediction, classification_prediction
    """

    reg_model = joblib.load("xgb_regressor_model.pkl")
    clf_model = joblib.load("xgb_classifier_model.pkl")

    new_df = pd.read_csv(input_csv_path)

    X_new = new_df.drop(
        columns=['% Cell viability', 'toxicity class encoded', 'toxicity class'],
        errors='ignore'
    )

    reg_pred = reg_model.predict(X_new)
    clf_pred = clf_model.predict(X_new)

    return reg_pred, clf_pred

print("ML training script ready.")