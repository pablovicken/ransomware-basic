from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import sys

# Função para derivar a chave a partir de uma senha
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Tamanho da chave AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Função para criptografar o arquivo
def encrypt_file(file_name: str, password: str):
    # Gerar um salt aleatório para a derivação da chave
    salt = os.urandom(16)

    # Derivar a chave a partir da senha e salt
    key = derive_key(password, salt)

    # Ler o conteúdo do arquivo
    with open(file_name, 'rb') as f:
        file_data = f.read()

    # Gerar um IV aleatório para a criptografia
    iv = os.urandom(16)

    # Inicializar o cipher com a chave e IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Adicionar padding ao arquivo
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    # Criptografar o arquivo
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Salvar o arquivo criptografado com IV + dados criptografados + salt
    with open(file_name, 'wb') as enc_file:
        enc_file.write(salt + iv + encrypted_data)

    # Salvar a senha em um arquivo
    with open(f"{file_name}.key", "w") as key_file:
        key_file.write(password)

    print(f"Arquivo '{file_name}' foi criptografado com sucesso!")
    print(f"A senha de criptografia foi salva em '{file_name}.key'")

# Verificar se o arquivo foi especificado
if len(sys.argv) < 3:
    print("Uso: python encrypt.py <nome_do_arquivo> <senha>")
else:
    file_name = sys.argv[1]  # Nome do arquivo a ser criptografado
    password = sys.argv[2]   # Senha fornecida pelo usuário
    encrypt_file(file_name, password)
