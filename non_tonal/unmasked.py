from scipy.io import wavfile
from lib import generate_sine_wave, generate_white_noise

def main() -> None:
    tone = generate_sine_wave(400.0, duration=5.0, amplitude=0.5)
    noise = generate_white_noise(duration=5.0, amplitude=0.5)
    signal = tone + noise
    wavfile.write("unmasked.wav", 44100, signal)

if __name__ == "__main__":
    main()
