#!/usr/env/bin bash

flag=$1

curl 'https://play.picoctf.org/api/submissions/' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: ja,en-US;q=0.7,en;q=0.3' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFToken: t6oBrjLMql4tDKWcj8jsArO2Tp4bc7il' \
  -H 'Origin: https://play.picoctf.org' \
  -H 'DNT: 1' \
  -H 'Sec-GPC: 1' \
  -H 'Alt-Used: play.picoctf.org' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://play.picoctf.org/practice/challenge/506?originalEvent=gym&page=1&solved=1' \
  -H 'Cookie: cf_clearance=oDSGL3I2kQOqAuAiXG2y0NuZ0fh7D96axjmebbjTejg-1764072544-1.2.1.1-j8DggLSJjCKDq2PBW6hJCQU6Fc9Khk5HYwIB6Ak.pAivpNwx7zCiTbnKxcIWCZOhjAwaK_72La5v3Ed.MiE6hGcGkWTQCpQirGTSbwCvMFMgr52rB1f1BLOEWxzevfgJs.LYf3vvRDvfQRgh0jL6DdkTVw4APLGGDkChG0FNxgiiBOKFcM8fPtPnxeHbvsE1xZi1d1PIQ0HRaF.G.xE9ErA8f0qNAR4QlDLCGfko7cgBhadRUHHcnZmfJXhsDAzV; csrftoken=t6oBrjLMql4tDKWcj8jsArO2Tp4bc7il; sessionid=icxanf06c9s9t1wsc27z1z1orl47412v' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Priority: u=0' \
  --data-raw "{\"challenge\":506,\"flag\":\"$flag\"}"
echo