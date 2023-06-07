import wave
from bitarray import bitarray


def bits_to_bytes(bits):
    byte_array = bits.tobytes()
    return byte_array


def extract_data(audio_file):
    audio = wave.open(audio_file, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    extracted_data = bits_to_bytes(bitarray(extracted_bits))
    audio.close()
    return extracted_data


audio_file = 'modified.wav'
extracted_data = extract_data(audio_file)
print("Extracted message (raw bytes):")
print(extracted_data)
