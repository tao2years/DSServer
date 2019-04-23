import pandas as pd
filename = "intent.csv"

def csv2Json(filename):
    df = pd.read_csv(filename)
    print(df)
    df.to_json("intent.json", orient='index')

csv2Json(filename)