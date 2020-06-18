from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import base64

PUBLIC_KEY = '-----BEGIN PUBLIC KEY-----\n' + \
'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCKFctVrhfF3m2Kes0FBL/JFeO' + \
'cmNg9eJz8k/hQy1kadD+XFUpluRqa//Uxp2s9W2qE0EoUCu59ugcf/p7lGuL99Uo' + \
'SGmQEynkBvZct+/M40L0E0rZ4BVgzLOJmIbXMp0J4PnPcb6VLZvxazGcmSfjauC7' + \
'F3yWYqUbZd/HCBtawwIDAQAB\n' + \
'-----END PUBLIC KEY-----'

def encrypt(msg):
    keyPub = RSA.importKey(PUBLIC_KEY)
    cipher = PKCS1_v1_5.new(keyPub)
    cipher_text = cipher.encrypt(msg.encode())
    return base64.b64encode(cipher_text).decode()
