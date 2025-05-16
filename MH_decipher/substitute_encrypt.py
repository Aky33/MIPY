from .alphabet import alphabet

def substitute_encrypt(plaintext, key):
    mapping = {}
    for i in range(len(alphabet)):
        mapping[alphabet[i]] = key[i]

    encrypted_text = ''
    for c in plaintext:
        if c in mapping:
            encrypted_text += mapping[c]
        else:
            encrypted_text += c

    return encrypted_text