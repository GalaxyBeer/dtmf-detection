# DTMF Detection

A basic Python script for detecting DTMF tones from WAV files. Pairs corresponding to DTMF tones are defined. Two frequency components are used for each value. Only files with the ".wav" extension in the directory are retrieved, returning the sampling frequency and audio data.

##Logic 

Fourier transformation (FFT) is used to read audio files and recognize DTMF tones. DTMF frequencies are pairs of frequency components corresponding to telephone keys. Using FFT, the frequency components of the audio signal are found and compared with the DTMF frequency pairs. If specific frequency pairs are above a certain power threshold, these pairs are recognized as DTMF tones. The recognition results are shown along with the information taken from the file name.

###Application

![image](https://github.com/GalaxyBeer/dtmf-detection/assets/72799974/5fc2361c-dd8b-4e06-9e91-15435fd67241)

## How to Use

1. Place your DTMF WAV files in the specified directory.
2. Run the `dtmf_detection.py` script to analyze the audio files and detect DTMF tones.

## Requirements

- `numpy`
- `scipy`

## Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.
