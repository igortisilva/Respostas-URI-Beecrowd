while True:
  try:
    a = int(input())
    w = [int(i) for i in input().split()]
    maior = w[0]
    for x in range(len(w)):
        if(w[x] > maior):
            maior = w[x]
    if(maior < 10):
        print(1)
    if(maior >= 10 and maior < 20):
        print(2)
    if(maior > 20):
        print(3)
  except EOFError:
    break
