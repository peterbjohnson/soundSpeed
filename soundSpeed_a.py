# Reads and plots sounds from a sound card
# Customise the sample duration, frequency, and interval
##
# Example application:
# python soundSpeed_a.py --duration .1 --fs 44100 --interval 300 --device 1
##
# In the above example, a 0.1 s sample, at 44.1 kHz, is plotted every 300 ms, using device 1
##
# To select a device, run `listDevices.py` to see which devices are available

import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import argparse


def record_and_plot(duration, fs, interval_ms, device_id):
    # Query available audio devices
    devices = sd.query_devices()

    # Check if the specified device_id is valid
    if device_id >= len(devices) or device_id < 0:
        print(
            f"Invalid device ID {device_id}. Please choose a valid device ID.")
        return

    # Select the specified device
    selected_device = devices[device_id]
    print(f"Selected device: {selected_device['name']}")

    fig, ax = plt.subplots()
    ax.set_title('Recorded Audio')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Amplitude')

    # Number of channels (fix to 2 channels)
    num_channels = 2

    plt.ion()  # Turn on interactive mode
    plt.show()

    try:
        while True:
            # Record audio with blocking=False to disable automatic gain control
            myrecording = sd.rec(int(duration * fs), samplerate=fs,
                                 channels=num_channels, device=device_id, blocking=True)
            sd.wait()

            # Extract the data from the recording
            data = myrecording.T  # Transpose to have channels as the first dimension

            # Normalize the audio data to the range [-1, 1]
            data_normalized = data / np.max(np.abs(data))

            # Create a time axis for the plot
            time_axis = np.arange(0, len(data_normalized[0])) / fs

            # Plot each channel
            ax.clear()  # Clear previous plot
            for channel_data in data_normalized:
                ax.plot(time_axis, channel_data)

            ax.relim()
            ax.autoscale(axis='both', tight=True)
            plt.pause(interval_ms / 1000.0)

    except KeyboardInterrupt:
        print("Ctrl-C pressed. Exiting gracefully.")
    finally:
        plt.ioff()  # Turn off interactive mode
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Record and plot audio in real-time.')
    parser.add_argument('--duration', type=float, default=5,
                        help='Duration of each recording in seconds.')
    parser.add_argument('--fs', type=int, default=44100,
                        help='Sampling frequency.')
    parser.add_argument('--interval', type=int, default=100,
                        help='Interval between plots in milliseconds.')
    parser.add_argument('--device', type=int, default=2,
                        help='Device ID of the external sound card.')

    args = parser.parse_args()

    record_and_plot(args.duration, args.fs, args.interval, args.device)
