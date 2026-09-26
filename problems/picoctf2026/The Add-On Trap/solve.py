from cryptography.fernet import Fernet

# KEY = "picoCTF{you're on the right tra}"
KEY = "cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0="

# Fernet encrypted
URL = "gAAAAABmfRjwFKUB-X3GBBqaN1tZYcPg5oLJVJ5XQHFogEgcRSxSis1e4qwicAKohmjqaD-QG8DIN5ie3uijCVAe3xiYmoEHlxATWUP3DC97R00Cgkw4f3HZKsP5xHewOqVPH8ap9FbE"


fernet = Fernet(KEY)
msg = fernet.decrypt(URL)
print(msg)
