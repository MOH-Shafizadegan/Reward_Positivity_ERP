import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np

def plot_spectrum(data, fs):

    # Compute the spectrum
    S = np.fft.rfft(data) # The spectrum array
    P = 20 * np.log10(np.abs(S)) # The power array
    f = np.linspace(0, fs/2, len(P)) # The frequency array

    # Plot the spectrum
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
