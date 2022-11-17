#include<iostream>



using namespace std;


//->[5]->[1]->[3]->[7]->[8]->NULL

// 0x0000693 - 0x0000675
//  int         Node*
//  1           0x0000715

// 0x0000715 - 0x0000727
//  int         Node*
//  3

class Node{
    public:
        int val;
        Node* next;
};

//header
class List{
    public:
        Node* head = nullptr;
        void insert(int val);
};

//source
void List::insert(int val){
            Node* something = new Node;
            something->val = val;
            something->next = head;
            head = something;
        }

int main(){

    List myList;
    myList.insert(1);
    myList.insert(3);
    myList.insert(7);
    //head->[7]->[3]->[1]->NULL
}