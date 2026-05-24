# =========================================
# IMPORT LIBRARIES
# =========================================

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =========================================
# READ DATASET
# =========================================

print("\n======================================")
print("READING FINANCIAL DATASET")
print("======================================\n")

df = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!\n")

# =========================================
# PREVIEW DATASET
# =========================================

print("======================================")
print("DATASET PREVIEW")
print("======================================\n")

print(df.head())

# =========================================
# DATASET INFORMATION
# =========================================

print("\n======================================")
print("DATASET INFORMATION")
print("======================================\n")

print("Dataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns)

print("\nDataset Data Types:")
print(df.dtypes)

# =========================================
# CHECK MISSING VALUES
# =========================================

print("\n======================================")
print("MISSING VALUES")
print("======================================\n")

print(df.isnull().sum())

# =========================================
# HANDLE MISSING VALUES
# =========================================

print("\nHandling missing values...\n")

numeric_columns = df.select_dtypes(
    include=np.number
).columns

for col in numeric_columns:

    df[col] = df[col].fillna(
        df[col].mean()
    )

print("Missing values handled successfully!")

# =========================================
# STATISTICAL SUMMARY
# =========================================

print("\n======================================")
print("STATISTICAL SUMMARY")
print("======================================\n")

print(df.describe())

# =========================================
# FEATURES & TARGET
# =========================================

print("\n======================================")
print("PREPARING FEATURES")
print("======================================\n")

X = df.drop(
    "Financial_Status",
    axis=1
)

y = df["Financial_Status"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)

# =========================================
# TRAIN TEST SPLIT
# =========================================

print("\n======================================")
print("TRAIN TEST SPLIT")
print("======================================\n")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# =========================================
# FEATURE SCALING
# =========================================

print("\n======================================")
print("FEATURE SCALING")
print("======================================\n")

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("Scaling completed successfully!")

# =========================================
# TRAIN MACHINE LEARNING MODEL
# =========================================

print("\n======================================")
print("TRAINING AI MODEL")
print("======================================\n")

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("AI model trained successfully!")

# =========================================
# MODEL PREDICTION
# =========================================

print("\n======================================")
print("RUNNING PREDICTIONS")
print("======================================\n")

predictions = model.predict(X_test)

print("Predictions completed!")

# =========================================
# MODEL EVALUATION
# =========================================

print("\n======================================")
print("MODEL PERFORMANCE")
print("======================================\n")

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy Score: {accuracy:.2f}")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

# =========================================
# FEATURE IMPORTANCE
# =========================================

print("\n======================================")
print("FEATURE IMPORTANCE")
print("======================================\n")

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print(importance_df)

# =========================================
# SAVE MODEL
# =========================================

print("\n======================================")
print("SAVING AI MODEL")
print("======================================\n")

joblib.dump(
    model,
    "risk_model.pkl"
)

joblib.dump(
    scaler,
    "scaler.pkl"
)

print("risk_model.pkl saved!")
print("scaler.pkl saved!")

# =========================================
# FINISH
# =========================================

print("\n======================================")
print("PROJECT COMPLETED")
print("======================================\n")

print("Financial Risk AI is ready!")
