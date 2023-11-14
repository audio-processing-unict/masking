from scipy.io import wavfile
from lib import generate_sine_wave, generate_white_noise

def main() -> None:
    wavfile.write("tone_1000.wav", 44100, generate_sine_wave(1000.0, duration=5.0, amplitude=0.5))
    wavfile.write("tone_1300.wav", 44100, generate_sine_wave(1300.0, duration=5.0, amplitude=0.5))

if __name__ == "__main__":
    main()
