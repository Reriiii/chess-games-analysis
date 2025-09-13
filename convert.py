# pip install python-chess
import chess.pgn
import pandas as pd
import time
import logging
import random

# ---------------------------
# Config
# ---------------------------
DATE = "2025-01"
PATH = f"F://dataset/chess-game/{DATE}/lichess_db_standard_rated_{DATE}.pgn"
OUTPUT_CSV = f"dataset/{DATE}.csv"
LOG_FILE = f"logs/log_{DATE}.txt"

LOG_INTERVAL = 1000
LIMIT = 1_000_000  # số lượng game cần sample
SEED = 42
# ---------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, "a", encoding="utf-8"),
    ],
)

random.seed(SEED)
reservoir = []
total_seen = 0
start_time = time.time()

with open(PATH, "r", encoding="utf-8", errors="ignore") as f:
    while True:
        game_headers = chess.pgn.read_headers(f)
        if game_headers is None:
            break

        white_elo = game_headers.get("WhiteElo")
        black_elo = game_headers.get("BlackElo")

        if white_elo is None or black_elo is None:
            continue  
        
        avg_elo = (int(white_elo) + int(black_elo)) // 2

        row = {
            "Event": game_headers.get("Event"),
            "Date": game_headers.get("Date"),
            "White_Name": game_headers.get("White"),
            "Black_Name": game_headers.get("Black"),
            "WhiteElo": game_headers.get("WhiteElo"),
            "BlackElo": game_headers.get("BlackElo"),
            "WhiteRatingDiff": game_headers.get("WhiteRatingDiff"),
            "BlackRatingDiff": game_headers.get("BlackRatingDiff"),
            "Result": game_headers.get("Result"),
            "Opening": game_headers.get("Opening"),
            "TimeControl": game_headers.get("TimeControl"),
        }

        total_seen += 1
        if len(reservoir) < LIMIT:
            reservoir.append(row)
        else:
            j = random.randint(1, total_seen)
            if j <= LIMIT:
                reservoir[j - 1] = row

        if total_seen % LOG_INTERVAL == 0:
            elapsed = time.time() - start_time
            logging.info(
                f"{total_seen:,} games scanned | "
                f"Reservoir filled: {len(reservoir):,} | "
                f"Elapsed: {elapsed/60:.2f} min"
            )

# xuất ra csv
df = pd.DataFrame(reservoir)
df.to_csv(OUTPUT_CSV, index=False)

elapsed = time.time() - start_time
logging.info(
    f"[DONE] {len(reservoir):,} random games saved to {OUTPUT_CSV} "
    f"after scanning {total_seen:,} games in {elapsed/60:.2f} minutes."
)
