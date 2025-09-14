import pandas as pd
from pathlib import Path

data = {
    "Year": [],
    "QuestionNumber": [],
    "QuestionType": [],  # MCQ / Structured
    "Topic": [],
    "QuestionText": []
}

df = pd.DataFrame(data)
path = Path(__file__).resolve().parents[1] / "data" / "past_papers.csv"
df.to_csv(path, index=False)
print("✅ Empty dataset created at:", path)
