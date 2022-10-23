#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
   struct Node *next;
}*first=NULL;



void create(int arr[], int n){
    int i ;
   struct Node * t,*last;
    first = (struct Node *)malloc(sizeof(struct Node));
    first->data = arr[0];
    first->next =NULL;
    last = first;

    for(i=1;i<n;i++){
        t=(struct Node *)malloc(sizeof(struct Node));
        t->data = arr[i];
        t->next=NULL;
        last->next = t;
        last=t;

    }
}

//iterative approach
/*
void display(struct Node *p){
    while(p!=NULL){
        printf("%d, ",p->data);
        p=p->next;
    }
}
*/

//recursive approach
void display(struct Node *p){
    if(p!=NULL){
        printf("%d ,",p->data);
        display(p->next);
    } 
}

//count no.of nodes : recursive
int count(struct Node *p){
    if(p==0) return 0;
    return (count(p->next)+1);
}

//sum of all elements: recursive
int sum(struct Node *p){
    if(p==0) return 0;
    return sum(p->next)+p->data;
}

//linear search with move to head/front improv
struct Node * search(struct Node * p, int key){
    struct Node *q;
    while(p!=NULL){
        if(key == p->data){
            q->next = p->next;
            p->next = first;
            first = p;
            return p;
        }
        q=p;
        p=p->next;
    }
    return NULL;
}

int main(){
    int a[]={3,5,7,9,6};


    create(a,5);
    display(first);
    printf("\n%d\n",sum(first));
    printf("\n%d\n",count(first));

    struct Node *p;
    p=search(first,0);
    if(p==NULL){
        printf("not found");
    }
    else{
        printf("found %d",p->data);
    }

    




}
