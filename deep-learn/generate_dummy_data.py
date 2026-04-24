import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, mean_squared_error

# Set random seed untuk reproducibility
np.random.seed(42)

# ============================================
# SOAL 4: Dataset untuk Confusion Matrix
# ============================================
# Target: TP 42, TN 83, FP 27, FN 27 (total 179)

tp_count = 42
tn_count = 83
fp_count = 27
fn_count = 27
n_samples = tp_count + tn_count + fp_count + fn_count

# Generate features untuk semua samples
age = np.random.randint(18, 80, n_samples)
income = np.random.randint(20000, 200000, n_samples)
credit_score = np.random.randint(300, 850, n_samples)
employment_years = np.random.randint(0, 40, n_samples)
num_accounts = np.random.randint(1, 10, n_samples)
loan_amount = np.random.randint(5000, 500000, n_samples)
debt_to_income = np.random.uniform(0, 0.6, n_samples)
payment_history = np.random.randint(0, 100, n_samples)

# Create actual and predicted labels sesuai dengan target CM
actual_approval = np.concatenate([
    np.ones(tp_count + fn_count, dtype=int),      # 42 TP + 27 FN = 69 actual positive
    np.zeros(tn_count + fp_count, dtype=int)      # 83 TN + 27 FP = 110 actual negative
])

predicted_approval = np.concatenate([
    np.ones(tp_count, dtype=int),                 # 42 TP
    np.zeros(fn_count, dtype=int),                # 27 FN
    np.ones(fp_count, dtype=int),                 # 27 FP
    np.zeros(tn_count, dtype=int)                 # 83 TN
])

# Shuffle indices
shuffle_idx = np.random.permutation(n_samples)
age = age[shuffle_idx]
income = income[shuffle_idx]
credit_score = credit_score[shuffle_idx]
employment_years = employment_years[shuffle_idx]
num_accounts = num_accounts[shuffle_idx]
loan_amount = loan_amount[shuffle_idx]
debt_to_income = debt_to_income[shuffle_idx]
payment_history = payment_history[shuffle_idx]
actual_approval = actual_approval[shuffle_idx]
predicted_approval = predicted_approval[shuffle_idx]

# Create DataFrame
df_confusion = pd.DataFrame({
    'age': age,
    'income': income,
    'credit_score': credit_score,
    'employment_years': employment_years,
    'num_accounts': num_accounts,
    'loan_amount': loan_amount,
    'debt_to_income': np.round(debt_to_income, 2),
    'payment_history': payment_history,
    'actual_approval': actual_approval,
    'predicted_approval': predicted_approval
})

# Save to CSV
df_confusion.to_csv('confusion_matrix_data.csv', index=False)

print("=" * 60)
print("SOAL 4 - Dataset Confusion Matrix (Loan Approval)")
print("=" * 60)
print(f"Total samples: {len(df_confusion)}")
print(f"\nDataset shape: {df_confusion.shape}")
print(f"\nFirst 5 rows:")
print(df_confusion.head())

# Verify confusion matrix values
cm = confusion_matrix(actual_approval, predicted_approval)
tn, fp, fn, tp = cm.ravel()

print(f"\n--- Confusion Matrix ---")
print(f"TP (actual=1, predicted=1): {tp}")
print(f"TN (actual=0, predicted=0): {tn}")
print(f"FP (actual=0, predicted=1): {fp}")
print(f"FN (actual=1, predicted=0): {fn}")

# Hitung metrics
accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0

print(f"\n--- Metrics ---")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")

print(f"\nSaved to: confusion_matrix_data.csv\n")

# ============================================
# SOAL 5: Dataset untuk RMSE
# ============================================
# Hanya 4 dataset: actual dan predicted fare

actual_fare_data = [50, 10, 100, 500]
predicted_fare_data = [45, 25, 100, 400]

# Create DataFrame
df_rmse = pd.DataFrame({
    'actual_fare': actual_fare_data,
    'predicted_fare': predicted_fare_data
})

# Save to CSV
df_rmse.to_csv('rmse_data.csv', index=False)

print("=" * 60)
print("SOAL 5 - Dataset RMSE (Fare Prediction)")
print("=" * 60)
print(f"Total samples: {len(df_rmse)}")
print(f"\nDataset:")
print(df_rmse)

# Hitung RMSE
mse = mean_squared_error(df_rmse['actual_fare'], df_rmse['predicted_fare'])
rmse = np.sqrt(mse)

print(f"\n--- Metrics ---")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"\nSaved to: rmse_data.csv")
print("=" * 60)
