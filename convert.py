# pip install python-chess
import chess.pgn, pandas as pd
#get 32_796 per day, 10_932 per elo
current_date = None
rows = []

from_500_to_1000 = 0
from_1000_to_1500 = 0
from_1500 = 0

total = 0

path = "data/lichess_db_standard_rated_2025-08/lichess_db_standard_rated_2025-08.pgn"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    while True:
        
        game_headers = chess.pgn.read_headers(f)
        if game_headers is None:
            break
        
        date = game_headers.get("Date")
        if date != current_date:
            current_date = date
            from_500_to_1000 = 0
            from_1000_to_1500 = 0
            from_1500 = 0
        
        avg_elo = (int(game_headers.get("WhiteElo")) + int(game_headers.get("BlackElo"))) // 2
        
        if game_headers.get("TimeControl") == "600+5":
            if avg_elo <= 1000 and from_500_to_1000 <= 10_932:
                from_500_to_1000 += 1
            elif avg_elo <= 1500 and from_1000_to_1500 <= 10_932:
                from_1000_to_1500 += 1
            elif avg_elo > 1500 and from_1500 <= 10_932:
                from_1500 += 1
            else:
                continue
            
            rows.append({
                "Event": game_headers.get('Event'),
                "Date": game_headers.get("Date"),
                "White_Name": game_headers.get("White"),
                "Black_Name": game_headers.get("Black"),
                "WhiteElo": game_headers.get("WhiteElo"),
                "BlackElo": game_headers.get("BlackElo"),
                "WhiteRatingDiff": game_headers.get("WhiteRatingDiff"),
                "BlackRatingDiff ": game_headers.get("BlackRatingDiff"),
                "Result": game_headers.get("Result"),
                "Opening": game_headers.get("Opening"),
                "TimeControl": game_headers.get("TimeControl"),
            })
            total += 1
            if total >= 1000000:
                break
            print(f"{total}. Append: {avg_elo} Elo, 500 - 1000 Elo: {from_500_to_1000} , 1000 - 1500 Elo: {from_1000_to_1500}, > 1500 Elo: {from_1500}, Date: {date}")

df = pd.DataFrame(rows)
df.to_csv("games.csv", index=False)


