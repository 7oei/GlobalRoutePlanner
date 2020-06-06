// ./sort_dic dictionary.words.txt

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

  // ファイルを開く
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

  ofstream outputfile("sample_sorted.txt"); //出力ファイル

  // 全ての辞書の単語について
  for(int i=1; i<dic.size(); i++){
    string st = dic[i];
    // 大文字は小文字に変換
    for(int j=0; j<dic[i].size(); j++){ 
      if (65 <= dic[i][j] && dic[i][j] <= 90){
        dic[i][j] = dic[i][j] + 32;
      }
    }
    // 並べ替え
    sort(dic[i].begin(), dic[i].end());
    dic[i] = dic[i] + "," + st + ",";
  }

  sort(dic.begin(), dic.end()); // sort

  for(int i=1; i<dic.size(); i++){
    outputfile<<dic[i]; // 書き込む
  }
  outputfile.close();

  ifs.close();
  return 0;
}
