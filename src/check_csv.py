import pandas as pd

questions = pd.read_csv("../data/questions.csv")
syllabus  = pd.read_csv("../data/syllabus.csv")

print("Questions sample:\n", questions.head(), "\n")
print("Syllabus sample:\n", syllabus.head())
