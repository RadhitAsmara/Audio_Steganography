import wave
from bitarray import bitarray


def bytes_to_bits(byte_array):
    bits = bitarray(endian='big')
    bits.frombytes(byte_array)
    return bits


def hide_data(audio_file, secret_data, output_file):
    audio = wave.open(audio_file, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    audio.close()
    secret_data_bytes = secret_data.encode()
    secret_bits = bytes_to_bits(secret_data_bytes)
    if len(secret_bits) > len(frame_bytes):
        raise ValueError(
            "Audio file size is not enough to hide confidential data.")
    for i in range(len(secret_bits)):
        frame_bytes[i] = (frame_bytes[i] & 0xFE) | secret_bits[i]
    output_audio = wave.open(output_file, 'wb')
    output_audio.setparams(audio.getparams())
    output_audio.writeframes(frame_bytes)
    output_audio.close()
    print("Data hidden successfully in the audio file.")


audio_file = "original.wav"
secret_data = "This is a secret message!"
output_file = "modified.wav"
hide_data(audio_file, secret_data, output_file)
