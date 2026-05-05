import pandas as pd
import joblib
import os

# =========================
# BASE PATH
# =========================
BASE_DIR = os.path.dirname(__file__)  # pages/

# =========================
# LOAD MODELS
# =========================
encoder = joblib.load(os.path.join(BASE_DIR, "encoders.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))
reg_model = joblib.load(os.path.join(BASE_DIR, "xgb_regressor_model.pkl"))
clf_model = joblib.load(os.path.join(BASE_DIR, "xgb_classifier_model.pkl"))

# =========================
# PREDICTION FUNCTION
# =========================
def predict(user_input_dict):

    df = pd.DataFrame([user_input_dict])

    # Ensure all required columns exist
    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df.reindex(columns=features)

    # =========================
    # CATEGORICAL ENCODING FIX
    # (encoder is a DICT of LabelEncoders)
    # =========================
    cat_cols = df.select_dtypes(include="object").columns

    for col in cat_cols:
        if col in encoder:
            try:
                df[col] = encoder[col].transform(df[col].astype(str))
            except:
                df[col] = 0

    # =========================
    # SCALE DATA
    # =========================
    df_scaled = scaler.transform(df)

    # =========================
    # PREDICTIONS
    # =========================
    viability = reg_model.predict(df_scaled)[0]
    prob = clf_model.predict_proba(df_scaled)[0][1]
    tox = int(prob >= 0.5)

    return viability, prob, tox