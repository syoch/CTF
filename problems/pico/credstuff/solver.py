with open("leak/passwords.txt", "r") as f:
    passwords = f.read().splitlines()
with open("leak/usernames.txt", "r") as f:
    usernames = f.read().splitlines()

i = usernames.index("cultiris")
cultiris_pw = passwords[i]

s = "".join(
    chr(ord("a") + (26 + ord(c) - ord("a") - 13) % 26)
    if c.islower()
    else chr(ord("A") + (26 + ord(c) - ord("A") - 13) % 26)
    if c.isupper()
    else c
    for c in cultiris_pw
)
print(s)
