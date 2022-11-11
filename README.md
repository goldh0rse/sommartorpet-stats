# sommartorpet-stats
fbchat analysis project

## Install dependencies
``` 
$ pip install -r requirements.txt
```
or
```
$ conda install --file requirements.txt
```


## Getting started

1. Copy file `examples/login.py` into `src/login.py` and implement methods:
    1. `get_thread` -> Can be found in the messenger URL for a groupchat
    2. `get_user` -> Username / email
    3. `get_passwd` -> Password
    4. `get_cookies` -> Fetch cookies from a signed in session of messenger, and copy them in.
2. Add correct path in `constants.py` for data storage
3. Run `src/fetch_convo_data.py` to fetch conversational data
4. Run other analytic scripts
