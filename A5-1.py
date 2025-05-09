import pyaudio
import wave
import numpy as np


class A51Cipher:
    def __init__(self, key):
        self.R1 = [0] * 19
        self.R2 = [0] * 22
        self.R3 = [0] * 23
        self.key = key
        self.load_key()

    def load_key(self):
        for i in range(64):
            bit = (self.key >> i) & 1
            self.R1[i % 19] ^= bit
            self.R2[i % 22] ^= bit
            self.R3[i % 23] ^= bit

    def majority(self):
        return (self.R1[8] + self.R2[10] + self.R3[10]) >= 2

    def clock(self):
        maj = self.majority()
        if self.R1[8] == maj:
            feedback = self.R1[13] ^ self.R1[16] ^ self.R1[17] ^ self.R1[18]
            self.R1 = [feedback] + self.R1[:-1]
        if self.R2[10] == maj:
            feedback = self.R2[20] ^ self.R2[21]
            self.R2 = [feedback] + self.R2[:-1]
        if self.R3[10] == maj:
            feedback = self.R3[7] ^ self.R3[20] ^ self.R3[21] ^ self.R3[22]
            self.R3 = [feedback] + self.R3[:-1]

    def get_keystream(self, length):
        keystream = []
        for _ in range(length):
            self.clock()
            keystream.append(self.R1[-1] ^ self.R2[-1] ^ self.R3[-1])
        return keystream


def xor_data(data, keystream):
    return bytes([data[i] ^ keystream[i % len(keystream)] for i in range(len(data))])


def record_audio(output_file, duration=5, rate=44100, channels=1, chunk=1024):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=channels,
                        rate=rate, input=True, frames_per_buffer=chunk)

    print("Đang ghi âm...")
    frames = [stream.read(chunk)
              for _ in range(0, int(rate / chunk * duration))]

    print("Ghi âm xong!")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_file, 'wb') as wav:
        wav.setnchannels(channels)
        wav.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wav.setframerate(rate)
        wav.writeframes(b''.join(frames))


def encrypt_audio(input_file, output_file, key):
    with wave.open(input_file, 'rb') as wav:
        params = wav.getparams()
        frames = wav.readframes(wav.getnframes())

    cipher = A51Cipher(key)
    keystream = cipher.get_keystream(len(frames))
    encrypted_data = xor_data(frames, keystream)

    with wave.open(output_file, 'wb') as enc_wav:
        enc_wav.setparams(params)
        enc_wav.writeframes(encrypted_data)


def decrypt_audio(input_file, output_file, key):
    encrypt_audio(input_file, output_file, key)


key = 0b1010101111001101111010100100110110100110010101111100110001010110
record_audio("original.wav", duration=5)
encrypt_audio("original.wav", "encrypted.wav", key)
decrypt_audio("encrypted.wav", "decrypted.wav", key)
