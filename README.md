# Ransomware Simulado com Criptografia AES 🔐
Este projeto implementa um ransomware simulado que criptografa arquivos usando o algoritmo de criptografia simétrica AES e uma senha fornecida pelo usuário. O arquivo criptografado só pode ser restaurado com a senha correta. O projeto contém dois scripts principais: encrypt.py para criptografar arquivos e decrypt.py para descriptografá-los.

Aviso: Este projeto tem fins educacionais. Não o utilize em ambientes de produção ou em arquivos importantes. O objetivo é entender o funcionamento básico da criptografia e como um ransomware pode ser simulado para fins de aprendizado.

## Funcionalidades 📑
- Criptografia de Arquivos: O script encrypt.py criptografa um arquivo de texto usando uma senha fornecida pelo usuário.
- Descriptografia de Arquivos: O script decrypt.py restaura o arquivo criptografado quando a senha correta é fornecida.
- Geração de Arquivo de Senha: A senha fornecida é salva em um arquivo .key que pode ser usado para restaurar o arquivo posteriormente.

## Dependências 🛡
Este projeto utiliza a biblioteca cryptography para a implementação de criptografia AES com PBKDF2 para derivar a chave de criptografia a partir da senha fornecida.

## Instalação das dependências ✅
Para instalar as dependências do projeto, basta executar o seguinte comando:
```
pip install cryptography
```

## Como Usar 🔎
- Criptografando um arquivo
O script encrypt.py criptografa um arquivo usando uma senha fornecida. A senha é usada para gerar uma chave de criptografia, e o arquivo resultante é criptografado com o algoritmo AES.

- Para criptografar um arquivo, execute o seguinte comando:
```
python encrypt.py <nome_do_arquivo> <senha>
```
- Exemplo:
```
python encrypt.py teste.txt minha_senha_segura
```
Isso criptografará o arquivo teste.txt e salvará o arquivo criptografado no mesmo diretório, substituindo o arquivo original. A senha será salva em um arquivo .key para ser usada posteriormente na descriptografia.

2. Descriptografando um arquivo
Para descriptografar o arquivo, você deve fornecer a mesma senha utilizada durante a criptografia. O script decrypt.py vai restaurar o arquivo original a partir da versão criptografada.

Para descriptografar, execute o seguinte comando:
```
python decrypt.py <nome_do_arquivo> <senha>
```
Exemplo:
```
python decrypt.py teste.txt minha_senha_segura
```
Se a senha estiver correta, o arquivo será restaurado com sucesso. Caso contrário, o arquivo não será restaurado.

## Arquivos Gerados 🗂
Arquivo Criptografado: O arquivo criptografado substitui o arquivo original, contendo os dados criptografados, um salt (para a derivação da chave) e um vetor de inicialização (IV).
Arquivo de Senha: A senha usada para criptografar o arquivo é salva em um arquivo com o nome do arquivo original seguido de .key. Exemplo: teste.txt.key.
Estrutura de Arquivos
A estrutura de arquivos do projeto é a seguinte:
```
/desafio_ransomware
│
├── encrypt.py              # Script para criptografar arquivos
├── decrypt.py              # Script para descriptografar arquivos
├── teste.txt               # Arquivo de exemplo para criptografar
└── teste.txt.key           # Arquivo de senha gerado após a criptografia
```

## Detalhes Técnicos 🔗
Criptografia: O algoritmo de criptografia utilizado é o AES no modo CBC (Cipher Block Chaining). A chave de criptografia é derivada da senha do usuário usando o algoritmo PBKDF2.
Padding: O padding PKCS7 é usado para garantir que os dados criptografados tenham um tamanho múltiplo do bloco de criptografia de 128 bits.
Salt: Um salt aleatório é gerado para a derivação da chave, garantindo que a mesma senha resultará em chaves diferentes em execuções diferentes.
IV: Um vetor de inicialização (IV) aleatório é gerado para cada arquivo criptografado, aumentando a segurança da criptografia.

## Exemplo de Uso 📜
Criptografando o arquivo:
```
python encrypt.py arquivo.txt minha_senha
```
Saída esperada:
```
Arquivo 'arquivo.txt' foi criptografado com sucesso!
A senha de criptografia foi salva em 'arquivo.txt.key'
```
Descriptografando o arquivo:
```
python decrypt.py arquivo.txt minha_senha
```
Saída esperada:
```
Arquivo 'arquivo.txt' foi restaurado com sucesso!
```

### Considerações Finais 📳
Este projeto tem como objetivo educacional simular a criptografia e a restauração de arquivos com o uso de senhas, semelhante a um ransomware. O código pode ser aprimorado para incorporar mais recursos, como a troca de senhas, envio de notificações ou outras funcionalidades de segurança.

Licença
Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
