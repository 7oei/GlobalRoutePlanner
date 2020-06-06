// ./sort_dic2 dictionary.words.txt

#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <unordered_map>
#include <vector>
using namespace std;

void load_dict(string dictpath, vector<string> &dic) {
  ifstream ifs(dictpath, ios::in);

  // エラー処理
  if (!ifs) {
    cerr << "Error: file not opened." << endl;
    return;
  }

  string tmp;
  while (getline(ifs, tmp)) {
    dic.push_back(tmp);
  }

  ifs.close();
}

// 単語内の文字数をカウントする
void count_chars(string word, unordered_map<char, int> &counts) {
  for (int i = 0; i < word.size(); i++) {
    char c = tolower(word[i]);
    if (counts.find(c) == counts.end())
      counts.emplace(c, 0);
    counts[c]++;
  }
}

// 単語と文字カウントのマップを文字列に変換
// e.g. "class", {{'c', 1}, {'l': 1}, {'a': 1}, {'s': 2}} => c1l1a1s2,class,
string serialize_word(string word, unordered_map<char, int> &char_counts) {
  string s;
  for (auto c : char_counts) {
    s += c.first + to_string(c.second);
  }
  s += "," + word + ",";
  return s;
}

void convert_dict(vector<string> &dic) {
  // 全ての辞書の単語について
  for (int i = 1; i < dic.size(); i++) {
    string word = dic[i];
    unordered_map<char, int> counts = {};
    count_chars(word, counts);
    dic[i] = serialize_word(word, counts);
  }
  sort(dic.begin(), dic.end());
}

void store_dict(vector<string> dic) {
  ofstream outputfile("sample_sorted2.txt"); //出力ファイル
  for (int i = 1; i < dic.size(); i++) {
    outputfile << dic[i]; // 書き込み
  }
  outputfile.close();
}

string parse_args(int argc, char *argv[]) {
  if (argc != 2) {
    cerr << "input ./getline input.txt" << endl;
    return "";
  }
  return argv[1];
}

int main(int argc, char *argv[]) {
  // argvから辞書のファイルパスを読み込む
  string dictpath = parse_args(argc, argv);

  // 辞書の格納先
  vector<string> dic;

  // オリジナルの辞書を読み込む
  load_dict(dictpath, dic);

  // 辞書を変換する
  convert_dict(dic);

  // 辞書を保存する
  store_dict(dic);

  return 0;
}