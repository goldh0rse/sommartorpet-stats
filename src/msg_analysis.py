import pandas as pd
import matplotlib.pyplot as plt
import constants as c

if __name__ == "__main__":
    """ Read data """
    df = pd.read_csv(c.data_path)

    """ Filter out NULL data """
    df = df[df['msg'].notnull()]
    df.info()

    df['authorID'] = df['authorID'].apply(lambda row: c.authors[row])

    """ Group by authorID """
    df = df[['authorID', 'msg']].groupby("authorID").count()
    
    """ Plot data """
    df = df.sort_values('msg')
    y = df.index.to_list()
    x = df['msg'].to_list()

    plt.bar(y,x, align="center", alpha=0.5)
    plt.title("Sommartorpet aktivitet")
    plt.ylabel("Antal meddelanden")
    plt.show()
    