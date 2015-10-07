#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <queue>
using namespace std;
struct Rubik{
    size_t face[6];
};
bool operator==(const Rubik & r1, const Rubik &r2){
    for(int i=0;i<6;i++) if(r1.face[i]!=r2.face[i]) return false;
    return true;
}
struct RubikHasher
{
    size_t operator()(const Rubik& k) const{
        size_t x = 0;
        for(int i=0;i<6;i++) x^=k.face[i];
        return x;
    }
};
int face[7][3][3];
struct Tup{
    int f,i,j;
    Tup(){}
    Tup(int _f,int _i,int _j):f(_f),i(_i),j(_j){}
};
Tup rot1[6][8]={
    {Tup(1,0,0),Tup(1,0,1),Tup(1,0,2),Tup(1,1,2),Tup(1,2,2),Tup(1,2,1),Tup(1,2,0),Tup(1,1,0)},
    {Tup(2,0,0),Tup(2,0,1),Tup(2,0,2),Tup(2,1,2),Tup(2,2,2),Tup(2,2,1),Tup(2,2,0),Tup(2,1,0)},
    {Tup(3,0,0),Tup(3,0,1),Tup(3,0,2),Tup(3,1,2),Tup(3,2,2),Tup(3,2,1),Tup(3,2,0),Tup(3,1,0)},
    {Tup(4,0,0),Tup(4,0,1),Tup(4,0,2),Tup(4,1,2),Tup(4,2,2),Tup(4,2,1),Tup(4,2,0),Tup(4,1,0)},
    {Tup(5,0,0),Tup(5,0,1),Tup(5,0,2),Tup(5,1,2),Tup(5,2,2),Tup(5,2,1),Tup(5,2,0),Tup(5,1,0)},
    {Tup(6,0,0),Tup(6,0,1),Tup(6,0,2),Tup(6,1,2),Tup(6,2,2),Tup(6,2,1),Tup(6,2,0),Tup(6,1,0)}
};
Tup rot2[6][12]={
    {Tup(5,0,0),Tup(5,1,0),Tup(5,2,0),Tup(2,0,0),Tup(2,1,0),Tup(2,2,0),Tup(6,0,0),Tup(6,1,0),Tup(6,2,0),Tup(4,2,2),Tup(4,1,2),Tup(4,0,2)},
    {Tup(5,2,0),Tup(5,2,1),Tup(5,2,2),Tup(3,0,0),Tup(3,1,0),Tup(3,2,0),Tup(6,0,2),Tup(6,0,1),Tup(6,0,0),Tup(1,2,2),Tup(1,1,2),Tup(1,0,2)},
    {Tup(5,2,2),Tup(5,1,2),Tup(5,0,2),Tup(4,0,0),Tup(4,1,0),Tup(4,2,0),Tup(6,2,2),Tup(6,1,2),Tup(6,0,2),Tup(2,2,2),Tup(2,1,2),Tup(2,0,2)},
    {Tup(5,0,2),Tup(5,0,1),Tup(5,0,0),Tup(1,0,0),Tup(1,1,0),Tup(1,2,0),Tup(6,2,0),Tup(6,2,1),Tup(6,2,2),Tup(3,2,2),Tup(3,1,2),Tup(3,0,2)},
    {Tup(4,0,2),Tup(4,0,1),Tup(4,0,0),Tup(3,0,2),Tup(3,0,1),Tup(3,0,0),Tup(2,0,2),Tup(2,0,1),Tup(2,0,0),Tup(1,0,2),Tup(1,0,1),Tup(1,0,0)},
    {Tup(2,2,0),Tup(2,2,1),Tup(2,2,2),Tup(3,2,0),Tup(3,2,1),Tup(3,2,2),Tup(4,2,0),Tup(4,2,1),Tup(4,2,2),Tup(1,2,0),Tup(1,2,1),Tup(1,2,2)}
};
void rev(int a[],int s,int t){
    t--;
    while(s<t) swap(a[s],a[t]),s++,t--;
}
void right_rotate(int a[],int n,int k){
    rev(a,0,n-k),rev(a,n-k,n),rev(a,0,n);
}
void left_rotate(int a[],int n,int k){
    rev(a,0,n),rev(a,0,n-k),rev(a,n-k,n);
}
int b1[8],b2[12];
void rotate(int x){
    bool lft = (x<0);
    if(x<0) x=-x;
    x--;
    for(int k=0;k<8;k++){
        Tup &t = rot1[x][k];
        b1[k] = face[t.f][t.i][t.j];
    }
    for(int k=0;k<12;k++){
        Tup &t = rot2[x][k];
        b2[k] = face[t.f][t.i][t.j];
    }
    if(lft){
        left_rotate(b1, 8, 2);
        left_rotate(b2, 12, 3);
    }else{
        right_rotate(b1, 8, 2);
        right_rotate(b2, 12, 3);
    }
    for(int k=0;k<8;k++){
        Tup &t = rot1[x][k];
        face[t.f][t.i][t.j] = b1[k];
    }
    for(int k=0;k<12;k++){
        Tup &t = rot2[x][k];
        face[t.f][t.i][t.j]= b2[k];
    }
}
bool check(){
    for(int i=1;i<=6;i++)
    for(int j=0;j<3;j++)
    for(int k=0;k<3;k++)
    if(face[i][j][k]!=face[i][0][0]) return false;
    return true;
}

unordered_map<Rubik, int,RubikHasher> tbl;
map<char,int> color_id;
vector<char> color;
inline int get_color_id(char c){
    if(color_id.count(c)==0) {
        color_id[c] = (int)color.size();
        color.push_back(c);
    }
    return color_id[c];
}
void decode(const Rubik& rubik){
    size_t x;
    for(int i=0;i<6;i++){
        x = rubik.face[i];
        for(int j=0;j<9;j++){
            face[i+1][j/3][j%3] = x%6;
            x/=6;
        }
    }
}
Rubik encode(){
    Rubik rubik;
    int x;
    for(int f=1;f<=6;f++){
        x = 0;
        for(int i=8;i>=0;i--)
            x = x*6 +face[f][i/3][i%3];
        rubik.face[f-1]=x;
    }
    return rubik;
}
queue<Rubik> Q;
void print_answer(const Rubik &rubik){
    int k = tbl[rubik];
    if(k==0) return;
    decode(rubik);
    rotate(-k);
    Rubik prev = encode();
    print_answer(prev);
    cout<<k<<",";
}
int main()
{
    char c;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            scanf(" %c",&c), face[5][i][j] = get_color_id(c);
    for(int i=0;i<3;i++){
        for(int k=1;k<=4;k++)
            for(int j=0;j<3;j++) scanf(" %c",&c),face[k][i][j]=get_color_id(c);
        }
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
        scanf(" %c",&c),face[6][i][j]=get_color_id(c);
    Rubik start = encode();
    Q.push(start);
    tbl[start] = 0; //which rotate lead to this
    while(!Q.empty()){
        Rubik head = Q.front();
        Q.pop();
        decode(head);
        if(check()){
            cout<<"I solved it"<<endl;
            print_answer(head);
            cout<<endl;
            break;
        }
        Rubik next;
        for(int k=-6;k<=6;k++){
            if(k==0) continue;
            rotate(k);
            next = encode();
            if(tbl.find(next)==tbl.end()){
                tbl[next] = k;
                Q.push(next);
            }
            rotate(-k);
        }
    }
    return 0;
}
/*

BBB
BPP
GGO
GGOPOYPBYRRR
PYPGBYRGOPOY
OOPGBPBRRGGR
BYY
YRO
YRO

*/
