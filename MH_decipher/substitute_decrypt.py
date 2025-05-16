from .alphabet import alphabet

def substitute_decrypt(ciphertext, key):
    reverse_mapping = {}
    for i in range(len(alphabet)):
        reverse_mapping[key[i]] = alphabet[i]

    decrypted_text = ''
    for c in ciphertext:
        if c in reverse_mapping:
            decrypted_text += reverse_mapping[c]
        else:
            decrypted_text += c

    return decrypted_text