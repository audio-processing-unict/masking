import numpy

def generate_sine_wave(frequency: int, duration=1.0, amplitude=1.0, sample_rate=44100) -> numpy.ndarray:
    num_samples = int(duration * sample_rate)
    sampling_times = numpy.linspace(0.0, duration, num_samples, dtype=numpy.float32)
    samples = amplitude * numpy.sin(frequency * sampling_times * (2.0 * numpy.pi))
    return samples

def generate_white_noise(mean=0.0, std=1.0, duration=1.0, amplitude=1.0, sample_rate=44100) -> numpy.ndarray:
    num_samples = int(duration * sample_rate)
    samples = amplitude * numpy.random.normal(mean, std, size=num_samples)
    return samples