from base64 import b64decode
from sys import argv
from gmpy2 import *


def parse_hex_string(hex_string):
    data_hex = hex_string.replace("\n", "").replace(" ", "").strip().replace(":", "")
    data_bytes = bytes.fromhex(data_hex)

    data = int.from_bytes(data_bytes, "big")
    return data


N_str = """
    00:b8:cb:1c:ca:99:b6:ac:41:87:6c:18:84:57:32:
    a5:cb:fc:87:5d:f3:46:ee:90:02:ce:60:85:08:b5:
    fc:f6:b6:0a:5a:c7:72:2a:2d:64:ef:74:e1:44:3a:
    33:8e:70:a7:3e:63:a3:03:f3:ac:9a:df:19:85:95:
    69:9f:6e:9f:30:c0:09:d2:19:c7:d9:8c:4e:c8:42:
    03:61:08:34:02:9c:79:56:7e:fc:08:f6:6b:4b:c3:
    f5:64:bf:b5:71:54:6a:06:b7:e4:8f:b3:5b:b9:cc:
    ea:9a:2c:d4:43:49:f8:29:24:20:78:df:a6:4d:52:
    59:27:bf:d5:5d:09:9c:02:4f
"""

P_str = """
    e7:00:56:8f:f5:06:bd:58:92:af:92:59:21:25:e0:6c:
    be:9b:d4:5d:fe:af:e9:31:a3:33:c1:34:63:02:3d:4f:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
"""

N = parse_hex_string(N_str)
P_Upper = parse_hex_string(P_str)
P = 10725802403113500160905962445604470167179368109016722523167967176202402354535693652761274441457102900144114459967870806231249767282954569832245125503110781
E = 0x10001


def calc_rsa_params():
    assert N % P == 0
    Q = N // P

    print(f"Q: {Q.bit_length()} bits")

    phi = (P - 1) * (Q - 1)
    print(f"phi: {phi.bit_length()} bits")

    d = invert(E, phi)
    print(f"d: {d.bit_length()} bits")

    e1 = d % (P - 1)
    e2 = d % (Q - 1)
    coeff = invert(Q, P)

    return {
        "modulus": N,
        "publicExponent": E,
        "privateExponent": d,
        "prime1": P,
        "prime2": Q,
        "exponent1": e1,
        "exponent2": e2,
        "coefficient": coeff,
    }


def generate_asn1_conf(params, fout):
    n = params["modulus"]
    e = params["publicExponent"]
    d = params["privateExponent"]
    p = params["prime1"]
    q = params["prime2"]
    e1 = params["exponent1"]
    e2 = params["exponent2"]
    co = params["coefficient"]

    conf = f"""asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:{n}
pubExp=INTEGER:{e}
privExp=INTEGER:{d}
p=INTEGER:{p}
q=INTEGER:{q}
e1=INTEGER:{e1}
e2=INTEGER:{e2}
coeff=INTEGER:{co}
"""

    with open(fout, "w") as f:
        f.write(conf)


params = calc_rsa_params()
generate_asn1_conf(params, argv[1])
