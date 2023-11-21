import sounddevice as sd


def list_audio_devices():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"{i}: {device['name']}")


if __name__ == "__main__":
    list_audio_devices()
