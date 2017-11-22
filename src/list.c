#include <stdlib.h>

typedef struct stringlistnode {
  char *node;
  struct stringlistnode *next;
} stringlist;

void stringlist_append(stringlist *pos, stringlist *new) {
  new->next = pos->next;
  pos->next = new;
}

stringlist stringlist_new(int itemSize, char *items[]) {
  stringlist *total;
  for(int i = 0; i < itemSize; i++) {
    stringlist *new;
    new = malloc(sizeof(stringlist));
    new->node = items[i];
  }
}
