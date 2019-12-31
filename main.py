# python　標準入力のサンプルです
input_line = int(input())
for i in range(input_line):
  s = input().rstrip().split(' ')
  print("hello = "+s[0]+" , world = "+s[1])