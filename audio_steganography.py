from pydub import AudioSegment
import tempfile

def hide_message_audio(audio_file, message_bytes):
    audio = AudioSegment.from_file(audio_file)
    samples = audio.get_array_of_samples()

    binary = ''.join(format(b, '08b') for b in message_bytes) + '1111111111111110'
    if len(binary) > len(samples):
        raise ValueError("Message too long for this audio file!")

    modified_samples = samples[:]
    for i in range(len(binary)):
        modified_samples[i] = (samples[i] & ~1) | int(binary[i])

    stego_audio = audio._spawn(modified_samples)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    stego_audio.export(temp_file.name, format="wav")
    return temp_file.name

def extract_message_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)
    samples = audio.get_array_of_samples()
    bits = ''.join(str(sample & 1) for sample in samples)
    end = bits.find('1111111111111110')
    if end == -1:
        return b"No hidden message found"
    bits = bits[:end]
    message_bytes = bytearray()
    for i in range(0, len(bits), 8):
        message_bytes.append(int(bits[i:i+8], 2))
    return bytes(message_bytes)
