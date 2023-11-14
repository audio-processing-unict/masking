from scipy.io import wavfile
from lib import generate_sine_wave, generate_white_noise

def main() -> None:
    wavfile.write("tone.wav", 44100, generate_sine_wave(400.0, duration=5.0, amplitude=0.5))
    wavfile.write("noise.wav", 44100, generate_white_noise(duration=5.0, amplitude=0.5))

if __name__ == "__main__":
    main()
