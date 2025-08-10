# src/hello.py
import pandas as pd

# create a tiny CSV
pd.DataFrame({
    "student": ["Ana","Ben","Cara","Ana","Ben"],
    "score":   [78, 85, 92, 88, 73],
    "week":    [1,1,1,2,2]
}).to_csv("scores.csv", index=False)

# read + compute
df = pd.read_csv("scores.csv")
by_stu = df.groupby("student")["score"].mean().sort_values(ascending=False)
by_week = df.groupby("week")["score"].mean()

print("Average by student:\n", by_stu.to_dict())  # {'Cara': 92.0, 'Ana': 83.0, 'Ben': 79.0}
print("Average by week:\n", by_week.to_dict())    # {1: 85.0, 2: 80.5}
