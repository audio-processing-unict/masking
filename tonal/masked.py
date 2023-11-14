from scipy.io import wavfile
from lib import generate_sine_wave

def main() -> None:
    low_tone = generate_sine_wave(1000.0, duration=5.0, amplitude=0.5)
    high_tone = generate_sine_wave(1300.0, duration=5.0, amplitude=0.05)
    signal = low_tone + high_tone
    wavfile.write("masked.wav", 44100, signal)

if __name__ == "__main__":
    main()
