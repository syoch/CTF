
#!/bin/bash

ENCRYPTED_FILE="flag.encrypted"
DECRYPTED_FILE="flag.decrypted.txt"

PASSWORD="ThisIsTheEncryptKey"
CIPHER_ALGORITHM="aes-256-cbc"
HASH_ALGORITHM="sha256"

# openssl's output
KEY="ADAFD798C69FFAEF2B2BBB44364F0952B988CDD37BB66BB2CB19B5827A8A2465"

IV="49005600430061006e004f0062006600"

printf "\x1b[1;33mUsing key below:\x1b[0m\n"
printf "\x1b[1;33mKey:\x1b[0m $KEY\n"
printf "\x1b[1;33mIV:\x1b[0m $IV\n"

printf "\x1b[33mDecrypting..\x1b[0m\n"
openssl enc -d -${CIPHER_ALGORITHM} \
    -in "${ENCRYPTED_FILE}" \
    -out "${DECRYPTED_FILE}" \
    -K "$KEY" \
    -iv  "$IV"

printf "\x1b[1;33mDecrypted file:\x1b[0m\n"
xxd $DECRYPTED_FILE