export INPUT="____ ___ _______"  # some string goes here
export INPUT="here cat network"
o=`echo $INPUT | md5sum | cut -c -32`
echo "flag{$o}"


4
3 cat
7 network