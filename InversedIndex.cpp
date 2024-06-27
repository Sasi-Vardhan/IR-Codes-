#include <bits/stdc++.h>
using namespace std;
struct ListNode{
    int DOC;
    struct ListNode* next;
};

typedef struct ListNode node;
unordered_map<string,node*> Seen;

unordered_map<int,int>Found;

string clower(string s){
    string ans = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
            ans += " ";
        }
        else if(s[i] >= 97 && s[i] <= 123){
            ans += s[i];
        }else{
            ans += (s[i] + 32);
        }
    }
    return ans;
}

node* AddTerm(node *first,int val){
    node  *Buffer;
    Buffer=new node;
     Buffer->DOC=val;
    Buffer->next=NULL;
    if(first == NULL) {
        first=Buffer;
        return first;
    }
    else{
        node *temp;
        temp=first;
        while(temp->next){
            temp=temp->next;
        }
        temp->next=Buffer;
    }
    return first;
}

void Saw(string s, int D){
    int prev = 0;
    string ans = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
             if(Seen.find(ans) == Seen.end()){
                Seen[ans] = new node;
            }
            Seen[ans]->next=AddTerm(Seen[ans]->next, D);
            ans = "";
            }
             else{
            ans+=s[i];
        }
        }
        if(Seen.find(ans) == Seen.end()){
                Seen[ans] = new node;
            }
            Seen[ans]->next=AddTerm(Seen[ans]->next, D);
    }
    
void Count(node *first){
    node *temp;
    temp=first;
    while(temp){
        Found[temp->DOC]++;
        temp=temp->next;
    }
}

void Find_Common(int n)
{
    if(n==0){
        cout<<"No Results are found :( "<<endl;
        return ;
    }
    cout<<"The Document is present in :";
    for(auto i=Found.begin();i!=Found.end();i++){
        if(i->second == n) cout<<" DOC "<<i->first<<" and ";
    }
}

void Find_all(int n){
    if(n==0){
        cout<<"No Results are found :( "<<endl;
        return ;
    }
    cout<<"The Document is present in :";
    for(auto i=Found.begin();i!=Found.end();i++){
        if(i->second > 0) cout<<" DOC "<<i->first<<" and ";
    }
}

int main(){
    string D1, D2, D3, D4;
    string query,ans="";
    int flag=0,l=0;
    // READING DOCUMENTS
    D1 = "new home top forecast ";
    D2 = "home sales rise in july ";
    D3 = "increase in home sales july ";
    D4 = "july new home sales ";
    Saw(D1,1);
    Saw(D2,2);
    Saw(D3,3);
    Saw(D4,4);
    node *temp;
    cout<<"Enter Query : ";
    getline(cin,query);
    cout<<"------------------------------------------"<<endl;
    
    for(int i = 0; i < query.size(); i++){
        if(query[i] == ' '){
            if(ans=="and"){
                ans="";
                flag=1;
                continue;
            }
            cout<<ans<<endl;
            if(Seen[ans]){
                Count(Seen[ans]->next);
                l++;
            }
            ans = "";
        }
        else{
            ans+=query[i];
        }
    }
    if(Seen[ans]){
        cout<<ans<<endl;
         Count(Seen[ans]->next);
                l++;
    } 
    
    if(flag==1) Find_Common(l);
    else Find_all(l);
    
    
}s
