void GenerateCPUChoice(Card *cpu_choice, Random *r)

{
  uint64_t rand;
  long i;
  ulong j;
  uint8_t tmp;

  *(undefined4 *)cpu_choice = 0x3020100;
  *(undefined4 *)(cpu_choice + 4) = 0x7060504;
  *(undefined4 *)(cpu_choice + 8) = 0xb0a0908;
  *(undefined4 *)(cpu_choice + 0xc) = 0xf0e0d0c;
  *(undefined4 *)(cpu_choice + 0x10) = 0x13121110;
  *(undefined4 *)(cpu_choice + 0x14) = 0x17161514;
  *(undefined4 *)(cpu_choice + 0x18) = 0x1b1a1918;
  *(undefined4 *)(cpu_choice + 0x1c) = 0x1f1e1d1c;
  *(undefined4 *)(cpu_choice + 0x20) = 0x23222120;
  *(undefined4 *)(cpu_choice + 0x24) = 0x27262524;
  *(undefined4 *)(cpu_choice + 0x28) = 0x2b2a2928;
  *(undefined4 *)(cpu_choice + 0x2c) = 0x2f2e2d2c;
  *(undefined4 *)(cpu_choice + 0x30) = 0x33323130;

  i = 51;
  do {
    rand = Random::GetRandom(r);
    j = (rand & 0xffffffff) % (ulong)((int)i + 1);
    tmp = cpu_choice[i].card;
    cpu_choice[i].card = cpu_choice[j].card;
    cpu_choice[j].card = tmp;
    i = i + -1;
  } while (i != 0);
  return;
}
