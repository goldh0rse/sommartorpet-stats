import pandas as pd
import matplotlib.pyplot as plt
import constants as c

if __name__ == "__main__":
    df = pd.read_csv(c.data_path)

    mentions = []
    for name in c.names:
        row = df[df['word'] == name]
        word = row.iloc[0]['word']
        count = row.iloc[0]['count'] 
        print(f"{word} {count}")
        