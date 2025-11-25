flag: msg.enc private.rec.der
	openssl pkeyutl -decrypt -in msg.enc -keyform der -inkey private.rec.der -out $@

private.rec.der: private.rec.txt
	openssl asn1parse -genconf $< -out $@
	openssl rsa -in private.rec.der -inform der -text

private.rec.txt:
	python3 generate-keyconf.py $@