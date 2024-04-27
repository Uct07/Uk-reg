customer = int(input("what is the id of user:"))
pointless=0
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
combinations = []
for i in range (0,len(letters)):
  for j in range(1,10000):
    combinations.append(letters[i] + str(j))
    print()
if customer <= len(combinations):
  assigned = combinations[customer+1]
  print(assigned)
else:
  print("first set complete")
  for a in range(0,len(letters)):
    for b in range(0,len(letters)):
      for c in range(1,10000):
        combinations.append(letters[a] + letters[b] +" "+ str(c))
if customer <= len(combinations):
  assigned = combinations[customer+1]
  print(assigned)
else:
  print("second set complete")
  threeban=["ARS","BUM","GOD","JEW","SEX","SOD","DUW"]
  for a in range(0,len(letters)):
    for b in range(0,len(letters)):
      for c in range(0,len(letters)):
        for d in range(1,10000):
          check = letters[a] + letters[b] + letters[c]
          for e in range(0,len(threeban)):
            if check == threeban[e]:
              pointless = 0
            else:
              combinations.append(letters[a] + letters[b] + letters[c] + str(d))

if customer <= len(combinations):
  assigned = combinations[customer+1]
  print(assigned)
else:
  print(len(combinations))