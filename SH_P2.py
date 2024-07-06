import os
import numpy as np
from scipy.io import wavfile

dtmf_frekanslar = {
    '697_1209': '1', '697_1336': '2', '697_1477': '3',
    '770_1209': '4', '770_1336': '5', '770_1477': '6',
    '852_1209': '7', '852_1336': '8', '852_1477': '9',
    '941_1209': '*', '941_1336': '0', '941_1477': '#'
}
ses_dizin = 'E:\SayisalHaberlesme_Proje\DTMF Files\dtmf_egitim_dosyalari'
dosyalar = os.listdir(ses_dizin)

for dosya in dosyalar:
    # Dosya yolu oluştur
    dosya_yolu = os.path.join(ses_dizin, dosya)
    
    if not dosya.endswith('.wav'):
        print(f"{dosya} WAV formatında değil, geçiliyor...")
        continue
    
    # Ses dosyasını yükle
    fs, ses_verisi = wavfile.read(dosya_yolu)
    
    # FFT 
    ses_fft = np.fft.fft(ses_verisi)
    frekanslar = np.fft.fftfreq(len(ses_fft), 1/fs)
    
    dugme_numarasi = None
    for frekans in dtmf_frekanslar.keys():
        f1, f2 = map(int, frekans.split('_'))
        band1 = np.abs(frekanslar - f1).argmin()  # Alt bant indeksi
        band2 = np.abs(frekanslar - f2).argmin()  # Üst bant indeksi
        # Her bantta en güçlü pikseli bul
        ton1 = np.abs(ses_fft[band1:band2]).argmax() + band1  
        ton2 = np.abs(ses_fft[band2:]).argmax() + band2 
        # DTMF tonu
        if ses_fft[ton1] > 1000 and ses_fft[ton2] > 1000:  
            dugme_numarasi = dtmf_frekanslar[frekans]
            break
    button_telefon = dosya.split('.')[0]  
    button, telefon = button_telefon.split('_')  
    
    if button == '10':
        button = '*'
    elif button == '11':
        button = '0'
    elif button == '12':
        button = '#'
    
    print(f"Ses Dosyası: {dosya}, Buton: {button}, Telefon: {telefon}")