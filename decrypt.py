from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes  # Importando o módulo 'hashes'
import os
import base64
import sys

# Função para derivar a chave a partir de uma senha e salt
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # Usando SHA256 para derivar a chave
        length=32,  # Tamanho da chave AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Função para descriptografar o arquivo
def decrypt_file(file_name: str, password: str):
    # Ler o conteúdo criptografado
    with open(file_name, 'rb') as f:
        file_data = f.read()

    # Extrair o salt (primeiros 16 bytes) e o IV (próximos 16 bytes)
    salt = file_data[:16]
    iv = file_data[16:32]
    encrypted_data = file_data[32:]

    # Derivar a chave a partir da senha e salt
    key = derive_key(password, salt)

    # Inicializar o cipher com a chave e IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografar os dados
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remover o padding
    unpadder = padding.PKCS7(128).unpadder()
    original_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Substituir o arquivo criptografado pelo arquivo original
    with open(file_name, 'wb') as dec_file:
        dec_file.write(original_data)

    print(f"Arquivo '{file_name}' foi restaurado com sucesso!")

# Verificar se o arquivo foi especificado
if len(sys.argv) < 3:
    print("Uso: python decrypt.py <nome_do_arquivo> <senha>")
else:
    file_name = sys.argv[1]  # Nome do arquivo criptografado
    password = sys.argv[2]   # Senha fornecida pelo usuário
    decrypt_file(file_name, password)
