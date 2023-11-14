import numpy
from scipy.io import wavfile
from lib import generate_sine_wave

def main() -> None:
    masker = generate_sine_wave(1000.0, duration=1.0, amplitude=0.5)
    masked = generate_sine_wave(1050.0, duration=1.05, amplitude=0.1)
    missing_samples = len(masked) - len(masker)
    masker = numpy.concatenate((masker, numpy.zeros(missing_samples)))
    signal = masker + masked
    wavfile.write("masked.wav", 44100, signal)

if __name__ == "__main__":
    main()
