import matplotlib.pyplot as plt
import pandas as pd
import constants as c
from tqdm import tqdm
tqdm.pandas()


if __name__ == "__main__":
    """ Read input datafile """
    df = pd.read_csv(c.data_path, usecols=['authorID', 'timestamp', 'msg'])

    """ Throw out nulldata """
    df = df[df['msg'].notnull()]

    """ Convert to timestamp & rename column """
    df['timestamp'] = df['timestamp'].progress_apply(lambda x: pd.to_datetime(x, unit="ms").strftime('%y-%m'))
    df.rename(columns={'timestamp':'date'})

    """ Convert ids to names """
    df['authorID'] = df['authorID'].progress_apply(lambda row: c.authors[row])
    
    df = df[['authorID', 'date', 'msg']]
    dates = df["date"].unique()[::-1]
    df = df.groupby(by=['date', 'authorID']).count()

    d1 = dates[0]
    agge = []
    personal_data = {}
    for name in c.authors.values():
        personal_data[name] = []
        for date in dates:
            try:
                msgs = df.loc[date].loc[name]['msg']
                personal_data[name].append(msgs)
            except KeyError:
                personal_data[name].append(0)
    
        plt.plot(dates, personal_data[name], label=name)

    plt.title("Activity over time")
    plt.ylabel("Messages")
    plt.xlabel("YY-MM")
    x_ticks = plt.xticks(rotation=45)

    for t in x_ticks[1][::2]:
        t.set_visible(False)

    plt.grid('on')
    plt.legend()
    plt.show()
