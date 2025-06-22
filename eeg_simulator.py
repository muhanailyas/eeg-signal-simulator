# eeg_simulator.py

import numpy as np
import matplotlib.pyplot as plt
import os

def generate_eeg_signal(duration=10, fs=250):
    """
    Generate a simulated EEG signal with alpha, beta, theta waves and random noise.
    
    Parameters:
    - duration: Duration of the signal in seconds.
    - fs: Sampling frequency (samples per second).
    
    Returns:
    - t: Time array.
    - signal: The generated EEG signal.
    """
    t = np.linspace(0, duration, duration * fs)
    alpha = np.sin(2 * np.pi * 10 * t)       # Alpha wave (8-13 Hz)
    beta = np.sin(2 * np.pi * 20 * t)        # Beta wave (13-30 Hz)
    theta = np.sin(2 * np.pi * 6 * t)        # Theta wave (4-8 Hz)
    noise = 0.5 * np.random.randn(len(t))    # Gaussian noise

    signal = alpha + beta + theta + noise    # Combine all components to form the EEG signal
    return t, signal

def plot_eeg(t, signal):
    """
    Plot the time-domain and frequency-domain representation of the EEG signal.
    
    Parameters:
    - t: Time array.
    - signal: Simulated EEG signal.
    """
    os.makedirs('plots', exist_ok=True)  # Create 'plots' directory if it doesn't exist
    
    # Time-domain plot
    plt.figure(figsize=(10, 3))
    plt.plot(t, signal)
    plt.title('Simulated EEG Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.savefig('plots/time_series.png')  # Save time-domain plot
    plt.close()

    # Frequency-domain plot
    freqs = np.fft.rfftfreq(len(t), 1/250)  # Frequency axis (1/250 is sampling period)
    fft_vals = np.abs(np.fft.rfft(signal))  # Fast Fourier Transform to get frequency components

    plt.figure(figsize=(10, 3))
    plt.plot(freqs, fft_vals)
    plt.title('Frequency Spectrum of EEG Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.savefig('plots/frequency_spectrum.png')  # Save frequency-domain plot
    plt.close()

if __name__ == "__main__":
    t, signal = generate_eeg_signal()  # Generate the EEG signal
    plot_eeg(t, signal)  # Plot the EEG signal
    print("Plots saved to '/plots/' directory.")
