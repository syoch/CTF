#include <sys/ucontext.h>

#define setbuf setbuf_
#include <stdio.h>
#undef setbuf

#include <dlfcn.h>
#include <signal.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <sys/fcntl.h>
#include <sys/mman.h>
#include <sys/ptrace.h>
#include <sys/signal.h>

static void sleep_() {
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

static void handler(int sig, siginfo_t *si, void *platform) {
  int kRegEFL = 17;
  void *address = si->si_addr;

  ucontext_t *ucontext = platform;
  mcontext_t *mcontext = &ucontext->uc_mcontext;

  uint64_t pc = mcontext->gregs[16];
  uint8_t *code_buf = (uint8_t *)(pc);

  printf("\x1b[1;31m======\x1b[m Unhandled instruction "
         "\x1b[1;31m======\x1b[m\n");
  printf("Attempting to access %p failed\n", address);
  printf("code: %016llx\n", pc);
  for (int j = 0; j <= 15; j++) {
    for (int i = 0; i < 16; i++) {
      uint8_t value = code_buf[j * 16 + i];
      printf("%02x ", value);
    }
    printf("\n");
  }

  printf("Signal handler finished\n");
  exit(1);
}

int strcmp(const char *s1, const char *s2) {
  char *env = getenv("LIBOV_STRCMP");
  if (env == NULL)
    goto bypass;
  if (env[0] != '1')
    goto bypass;
  if (env[1] != '\0')
    goto bypass;

  printf("strcmp called with: %s, %s\n", s1, s2);
  printf("Return 0 (equal) or non-zero (not equal): ");
  int result;
  scanf("%d", &result);
  return result;

bypass:
  for (int i = 0;; i++) {
    if (s1[i] != s2[i]) {
      return (unsigned char)s1[i] - (unsigned char)s2[i];
    }
    if (s1[i] == '\0') {
      return 0;
    }
  }
}

__attribute__((constructor)) static void init() {
  printf("Lib override loaded\n");

  struct sigaction sa;
  memset(&sa, 0, sizeof(sa));
  sa.sa_sigaction = handler;
  sa.sa_flags = SA_SIGINFO | SA_RESTART;
  if (sigaction(SIGSEGV, &sa, NULL) == -1) {
    printf("Registering SIGSEGV handler failed\n");
    exit(EXIT_FAILURE);
  }

  open("./libov_loaded", O_CREAT | O_WRONLY, 0644);
}