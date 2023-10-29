import numpy as np

def cluster_events_by_type(data, types):

    clustered_data = {}

    for type in set(types):
        idx = np.where(types == type)
        clustered_data[type] = data[idx]

    return clustered_data