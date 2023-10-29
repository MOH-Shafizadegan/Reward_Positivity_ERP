import numpy as np

def cluster_events_by_type(data, types):

    clustered_data = {}

    for type in set(types):
        idx = np.where(types == type)
        clustered_data[type] = data[idx]

    return clustered_data

def cluster_and_epoch(subject, onsets, fs, epoch_limits, baseline_limits):

    subject['epochs'] = {}

    for type in set(onsets.keys()):
        
        epoch_samples = epoch_limits * fs
        baseline_samples = baseline_limits * fs

        n_epoch = len(onsets[type])
        n_points = epoch_samples[1] - epoch_samples[0] + 1
        n_chan = subject['EEG'].shape[0]

        subject['epochs'][type] = np.zeros((n_chan, n_points, n_epoch))

        for i in range(n_epoch):

            start_index = int(np.round(float(onsets[type][i]) * fs + epoch_samples[0]))           # start index of the epoch
            end_index = int(np.round(float(onsets[type][i]) * fs + epoch_samples[1]))             # end index of the epoch
            baseline_start_index = int(np.round(float(onsets[type][i]) * fs + baseline_samples[0]))    # start index of the baseline within the epoch
            baseline_end_index = int(np.round(float(onsets[type][i]) * fs + baseline_samples[1]))     # end index of the baseline within the epoch
            baseline_mean = np.mean(subject["EEG"][0:n_chan, baseline_start_index:baseline_end_index+1], 1)   # mean value of the baseline for each channel
            subject['epochs'][type][:,:,i] = subject["EEG"][0:n_chan, start_index:end_index+1] - baseline_mean.reshape((67,1))
