# =========================================
# IMPORT LIBRARIES
# =========================================

from flask import (
    Flask,
    render_template,
    request
)

import pandas as pd
import numpy as np
import os
import joblib

# =========================================
# CREATE FLASK APP
# =========================================

app = Flask(__name__)

# =========================================
# LOAD AI MODEL
# =========================================

model = joblib.load(
    "risk_model.pkl"
)

scaler = joblib.load(
    "scaler.pkl"
)

# =========================================
# UPLOAD FOLDER
# =========================================

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# =========================================
# HOME PAGE
# =========================================

@app.route("/", methods=["GET", "POST"])

def home():

    table_data = None

    risk_summary = None

    if request.method == "POST":

        # ==================================
        # GET FILE
        # ==================================

        file = request.files["file"]

        if file:

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # ==================================
            # READ DATASET
            # ==================================

            df = pd.read_csv(filepath)

            # ==================================
            # HANDLE MISSING VALUES
            # ==================================

            numeric_columns = df.select_dtypes(
                include=np.number
            ).columns

            for col in numeric_columns:

                df[col] = df[col].fillna(
                    df[col].mean()
                )

            # ==================================
            # PREPARE FEATURES
            # ==================================

            if "Financial_Status" in df.columns:

                X = df.drop(
                    "Financial_Status",
                    axis=1
                )

            else:

                X = df

            # ==================================
            # SCALE DATA
            # ==================================

            X_scaled = scaler.transform(X)

            # ==================================
            # AI PREDICTION
            # ==================================

            predictions = model.predict(
                X_scaled
            )

            # ==================================
            # ADD RESULT COLUMNS
            # ==================================

            df["Mức_Độ_Rủi_Ro"] = predictions

            # ==================================
            # TRUST SCORE
            # ==================================

            df["Điểm_Tin_Cậy"] = np.where(

                df["Mức_Độ_Rủi_Ro"]
                == "Rủi Ro Cao",

                np.random.randint(
                    20,
                    50,
                    len(df)
                ),

                np.random.randint(
                    70,
                    100,
                    len(df)
                )
            )

            # ==================================
            # FINANCIAL HEALTH
            # ==================================

            df["Tình_Trạng_Tài_Chính"] = np.where(

                df["Điểm_Tin_Cậy"] > 75,

                "Ổn Định",

                "Cảnh Báo"
            )

            # ==================================
            # SUMMARY
            # ==================================

            risk_summary = {

                "rows": df.shape[0],

                "columns": df.shape[1],

                "high_risk": (
                    df["Mức_Độ_Rủi_Ro"]
                    == "Rủi Ro Cao"
                ).sum(),

                "stable": (
                    df["Tình_Trạng_Tài_Chính"]
                    == "Ổn Định"
                ).sum()
            }

            # ==================================
            # HTML TABLE
            # ==================================

            table_data = df.head(30).to_html(
                classes="table",
                index=False
            )

    return render_template(

        "index.html",

        table_data=table_data,

        risk_summary=risk_summary
    )

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )