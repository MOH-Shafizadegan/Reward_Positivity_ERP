import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
from sklearn.decomposition import FastICA

def plot_spectrum(data, fs):

    # Compute the spectrum
    S = np.fft.rfft(data) # The spectrum array
    P = 20 * np.log10(np.abs(S)) # The power array
    f = np.linspace(0, fs/2, len(P)) # The frequency array

    # Plot the spectrum
    plt.figure
    plt.plot(f, P)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (dB)')
    plt.title('Spectrum')
    plt.show()

def bp_filter(data, f_low, f_high, order, fs):
    
    # Design the filter using butter()
    b, a = signal.butter(order, [f_low, f_high], fs=fs, btype='band')

    # Apply the filter to the data using filtfilt()
    filtered_data = signal.filtfilt(b, a, data)

    return filtered_data

def remove_ICA(data):
    # Run ICA on your data
    data = data.T
    ica = FastICA(n_components=data.shape[1]) # we want *all* the components
    ica.fit(data)

    # Decompose your data into independent components
    components = ica.transform(data) # shape = (n_samples, n_components)

    remove_indices = list(np.where(np.max(components, 0) > 0.75*np.max(abs(components))))

    # "remove" unwanted components by setting them to 0 - simplistic but gets the job done
    components[:, remove_indices] = 0

    #reconstruct signal
    return ica.inverse_transform(components)

