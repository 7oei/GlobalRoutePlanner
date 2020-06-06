// ./sort_dic2 dictionary.words.txt

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[]){

  // 入力のエラー処理
  if(argc != 2){
    cerr << "input ./getline input.txt" << endl;
    return 1;
  }

  // open file
  ifstream ifs(argv[1], ios::in);

  // エラー処理
  if(!ifs){
    cerr << "Error: file not opened." << endl;
    return 1;
  }

  string tmp;
  vector<string> dic; // 受け取ったdictionary文字列格納

  while(getline(ifs, tmp)){
    dic.push_back(tmp);
  }

  ofstream outputfile("sample_sorted2.txt"); //出力ファイル

  // 全ての辞書の単語について
  for(int i=1; i<dic.size(); i++){
    string st = dic[i];
    // 大文字は小文字に変換
    for(int j=0; j<st.size(); j++){ 
      if (65 <= st[j] && st[j] <= 90){
        st[j] = st[j] + 32;
      }
    }

    sort(st.begin(), st.end());

    char c=st[0]; //1つ前の文字
    int cnt=1; // 連続で出た数カウント
    string s; // a1b2...みたいなのを保存する文字列

    // ehllo -> ehllo,e1h1l2o1 にする
    for(int j=1; j<st.size(); j++){
      if (c == st[j]) {
        cnt++;
      }
      else {
        s += c + to_string(cnt); // ll -> l2 とかの変換
        cnt = 1;
        c = st[j];
      }
    }
    s += c + to_string(cnt);
    st = s + "," + st + ",";  // h1e1l2o1,hello,
    dic[i] = st;
  }

  sort(dic.begin(), dic.end());

  for(int i=1; i<dic.size(); i++){
    outputfile<<dic[i]; // 書き込み
  }
  outputfile.close();

  ifs.close();
  return 0;
}