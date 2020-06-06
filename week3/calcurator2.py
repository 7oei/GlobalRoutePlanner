def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMult(line, index):
  token = {'type': 'MULT'}
  return token, index + 1

def readDivision(line, index):
  token = {'type': 'DIVISION'}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMult(line, index)
    elif line[index] == '/':
      (token, index) = readDivision(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


# 掛け算割り算
def evaluateMulDiv(tokens):
  tokens_removedMulDiv = []
  if not tokens[0]['type'] == 'MINUS': # 式が負の数で始まる場合を考慮
      tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  tmp_num = tokens[index]['number'] # 演算子の前の値を保持しておくための変数

  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':

      if tokens[index - 1]['type'] == 'MULT':
        tmp_num *= tokens[index]['number']

      elif tokens[index - 1]['type'] == 'DIVISION':
        tmp_num /= tokens[index]['number']

      elif tokens[index-1]['type'] == 'PLUS' or tokens[index-1]['type'] == 'MINUS':
        # 最初の数字の場合は保持している数字が自分自身なのでappendしない
        if not index==1: tokens_removedMulDiv.append({'type': 'NUMBER', 'number': tmp_num})
        tokens_removedMulDiv.append({'type': tokens[index-1]['type']}) # '+'または'-'はそのままappend
        tmp_num = tokens[index]['number'] # この時点で保持してる数字は乗算も除算もしないのでappend

      else:
        print('Invalid syntax')
        exit(1)

    index += 1
  tokens_removedMulDiv.append({'type': 'NUMBER', 'number': tmp_num})
  return tokens_removedMulDiv


# 足し算引き算
def evaluatePlusMinus(tokens_removedMulDiv):
    answer = 0
    index = 1
    while index < len(tokens_removedMulDiv):
      if tokens_removedMulDiv[index]['type'] == 'NUMBER':
        if tokens_removedMulDiv[index - 1]['type'] == 'PLUS':
          answer += tokens_removedMulDiv[index]['number']
        elif tokens_removedMulDiv[index - 1]['type'] == 'MINUS':
          answer -= tokens_removedMulDiv[index]['number']
        else:
          print('Invalid syntax')
          exit(1)
      index += 1
    return answer


# 全体の計算
# 先に乗算除算、その後加算引き算
def calcurate(tokens):
    tokens_removedMulDiv = evaluateMulDiv(tokens)
    return evaluatePlusMinus(tokens_removedMulDiv)


def test(line):
  tokens = tokenize(line)
  actualAnswer = calcurate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("2.5*3")
  test("2*3/2")
  test("2+2*3.1-4")
  test("2*3.141592653589793238")
  test("-10+2.718281828459*5/2+1")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  ans = calcurate(tokens)
  print("answer = %f\n" % ans)
