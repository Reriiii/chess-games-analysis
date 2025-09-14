import pandas as pd

# ==============================
# Config
# ==============================
DATE = "2025-04"
CSV_PATH = f"dataset/{DATE}.csv"  
EXPECTED_SHAPE = (1_000_000, 11)

# ==============================
# Checker
# ==============================
def check_csv(path: str):
    try:
        df = pd.read_csv(path)

        # 1. Shape check
        if df.shape != EXPECTED_SHAPE:
            print(f"[FAIL] Shape mismatch: {df.shape}, expected {EXPECTED_SHAPE}")
        else:
            print("[OK] Shape is correct")

        # 2. Duplicate rows
        dup_count = df.duplicated().sum()
        if dup_count > 0:
            print(f"[FAIL] Found {dup_count} duplicate rows")
        else:
            print("[OK] No duplicates")

        # 3. Date column coverage
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            if df["Date"].isna().any():
                print("[FAIL] Invalid date values found")
            else:
                min_date, max_date = df["Date"].min(), df["Date"].max()
                print(f"[INFO] Date range: {min_date} → {max_date}")
                if min_date.day == 1 and max_date.day >= 28:
                    print("[OK] Date covers full month")
                else:
                    print("[WARN] Date may not cover full month")
        else:
            print("[FAIL] Column 'Date' missing")

        # 4. Null values (except WhiteRatingDiff & BlackRatingDiff)
        allow_null = {"WhiteRatingDiff", "BlackRatingDiff"}
        for col in df.columns:
            if col not in allow_null and df[col].isna().any():
                print(f"[FAIL] Nulls found in column: {col}")
        print("[OK] Null value check done")

        # 5. Extra checks
        if "WhiteElo" in df.columns and (df["WhiteElo"] <= 0).any():
            print("[FAIL] WhiteElo has non-positive values")
        if "BlackElo" in df.columns and (df["BlackElo"] <= 0).any():
            print("[FAIL] BlackElo has non-positive values")

        print("=== Check complete ===")

    except Exception as e:
        print(f"[ERROR] Could not check file: {e}")

# Run
check_csv(CSV_PATH)
