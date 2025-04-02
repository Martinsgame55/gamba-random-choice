import random

ruleta = ["červená", "zelená", "černá", "0-16", "17-32"]
for i in ruleta:
    print(i)
gamba = input("zadejte jakou chcete možnost")
ruleta.append(gamba)


nahodnaHodnota = random.choice(ruleta)
print(nahodnaHodnota)
