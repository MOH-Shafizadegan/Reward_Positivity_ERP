import csv
import numpy as np
import mne

def load_subject_data(id, participants_info):
    sub1_events = []
    with open('../sub-001/ses-01/eeg/sub-001_ses-01_task-ReinforcementLearning_events.tsv', 'r') as f:
        # Create a DictReader object with tab as the delimiter
        reader = csv.DictReader(f, delimiter='\t')
        # Iterate over the rows of the reader
        for row in reader:
            # Append each row as a dictionary to the list
            sub1_events.append(row)

    subject = {}
    subject["Group"] = participants_info[id]['Group']
    subject["events"] = {}
    subject["events"]['onset'] = np.array([event["onset"] for event in sub1_events])
    subject["events"]['type'] = np.array([event["trial_type"] for event in sub1_events])

    if id == 0:
        eeg_file = '../sub-001/ses-01/eeg/sub-001_ses-01_task-ReinforcementLearning_eeg.set'
    elif id == 1:
        eeg_file = '../sub-002/ses-01/eeg/sub-002_ses-01_task-ReinforcementLearning_eeg.set'
    else:
        eeg_file = '../sub-002/ses-02/eeg/sub-002_ses-02_task-ReinforcementLearning_eeg.set'

    raw = mne.io.read_raw_eeglab(eeg_file)

    subject["EEG"] = raw.get_data()

    return subject


