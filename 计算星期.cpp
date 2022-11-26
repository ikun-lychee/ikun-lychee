#include<iostream>
using namespace std;

int main(){
  int Y,M,D,f,y,m;
  cin>>Y>>M>>D;
  f=(14-M)/12;
  y=Y-f;
  m=M+12*f-2;
  int w=(D+y+31*m/12+y/4-y/100+y/400)%7;
  if(w==1) cout<<"周一";
  else if(w==2) cout<<"周二";
  else if(w==3) cout<<"周三";
  else if(w==4) cout<<"周四";
  else if(w==5) cout<<"周五";
  else if(w==6) cout<<"周六";
  else cout<<"周日";
  
  return 0;
}
