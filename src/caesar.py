
def build_cipher(key_value):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890., "
    alphabet_size = len(alphabet)

    cipher = {}

    for i in range(alphabet_size):

        dest = i + key_value
        if dest >= alphabet_size:
            dest = dest - alphabet_size

        cipher[alphabet[i]] = alphabet[dest]

    return cipher


def encode(message, key_value):

    cipher = build_cipher(key_value)

    encoded_message = []

    for letter in message:
        encoded_message.append(cipher[letter])  

    return "".join(encoded_message)


def decode(message, key_value):
    return encode(message, -1 * key_value)


if __name__ == "__main__":
    msg = "Nos vemos despues de clase. Te amo."
    encoded_message = encode(msg, 13)

    print(f"El mensaje cifrado es: {encoded_message}")
