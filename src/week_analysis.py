import pandas as pd
import matplotlib.pyplot as plt
import constants as c
from tqdm import tqdm
tqdm.pandas()



if __name__ == '__main__':
    """ Read input data """
    df = pd.read_csv(c.data_path, usecols=['timestamp', 'msg'])

    """ Filter messages """ 
    df = df[df['msg'].notnull()]

    """ Apply datetime transformation + rename """
    df['timestamp'] = df['timestamp'].progress_apply(lambda x: pd.to_datetime(x, unit="ms").day_name())
    df.rename(columns={'timestamp':'weekday'}, inplace=True)

    """ Group by weekdays """
    df = df.groupby('weekday').count()

    """ Extract and order data """
    y = [df.loc[day]['msg'] for day in c.weekdays]
    
    plt.bar(c.weekdays, y)
    plt.title("Activity over weekdays")
    plt.grid('on')
    plt.show()