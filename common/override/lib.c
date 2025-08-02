#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static void sleep() {
  FILE *fp = fopen("/root/flag.txt", "r");
  if (fp) {
    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    char *buffer = malloc(size + 1);
    if (buffer) {
      fread(buffer, 1, size, fp);
      buffer[size] = '\0';
      printf("[flag.txt]\n%s\n", buffer);
      free(buffer);
    }
    fclose(fp);
  } else {
    printf("[flag.txt] Could not open /root/flag.txt\n");
  }
}
