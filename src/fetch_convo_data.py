import os
import fbchat
import time
import pandas as pd
from login import *

__TIMEBUFFER__ = 0.5
data_path = "~/repos/sommartorpet/data/conv_data.csv" # Match ur path


def write_output(messages, df=None):

    # Expand datatype
    exp_msg = [[] for _ in range(len(messages))]
    for msg, new_msg in zip(messages,exp_msg):
        new_msg.append(msg.uid)
        new_msg.append(msg.author)
        new_msg.append(msg.timestamp)
        new_msg.append(msg.text)


    new_df = pd.DataFrame(exp_msg, columns=["msgID","authorID","timestamp","msg"])

    if df is None:
        new_df.to_csv(data_path, index=False)
    else:
        df = pd.concat(df, new_df, axis=1)
        df.to_csv(data_path, index=False)

def fetch_data(timestamp=None):
    client = fbchat.Client(get_user(), get_passwd(), session_cookies=get_cookies())
    print(f"Logged in: {client.isLoggedIn()}")

    msg_lst = []
    fetches = 1
    if timestamp is None:
        messages = client.fetchThreadMessages(thread_id=get_thread(), limit=100)
        for msg in messages:
            msg_lst.append(msg)
        print(f"Fetch #{fetches:0<3}, msg-count: {len(msg_lst):10}")
        timestamp = messages[-1].timestamp
    
    time.sleep(__TIMEBUFFER__)
    first_time = True
    attempt = 1

    stop = False
    while not stop: # error
        try:
            messages = client.fetchThreadMessages(thread_id=get_thread(), limit=100, before=timestamp)    
            if len(messages) == 0: # Exit
                stop = True
                break
            timestamp = messages[-1].timestamp 
        except fbchat.FBchatException as e:
            if first_time:
                write_output(msg_lst)
                first_time = False
            print(f"Retrying fetch #{fetches:0<3}, attempt #:{attempt:2}")
            attempt += 1
            time.sleep(__TIMEBUFFER__ * 4)
            continue

        first_time = True
        for msg in messages:
            msg_lst.append(msg) 
        fetches += 1
        attempt = 1
        print(f"Fetch #{fetches:0<3}, msg-count: {len(msg_lst):10}")
        time.sleep(__TIMEBUFFER__)
        
    return msg_lst
         


if __name__ == "__main__":

    if os.path.exists(data_path):
        print("Old file exists")
        # Read csvfile
        df = pd.read_csv(data_path)
        time_stamp = df["timestamp"].iloc[-1]
        msg_lst = fetch_data(int(time_stamp))
        write_output(msg_lst, df)

    else:
        msg_lst = fetch_data()
        write_output(msg_lst)
