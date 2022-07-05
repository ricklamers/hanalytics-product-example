import pandas as pd
import numpy as np


def random_dates(start, end, n=10):

    start_u = start.value//10**9
    end_u = end.value//10**9

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


def compute_event_df(events_df):
    buy_counts = events_df[['product', 'action']][events_df['action'] == 'buy'].value_counts().to_frame()
    buy_counts.index = buy_counts.index.droplevel(1)

    view_counts = events_df[['product', 'action']][events_df['action'] == 'view'].value_counts().to_frame()
    view_counts.index = view_counts.index.droplevel(1)

    df = pd.concat([buy_counts, view_counts], axis=1)
    df.columns = ['total_buys', 'total_views']
    
    return df