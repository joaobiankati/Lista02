gols_time_a = int(input("Informe a quantidade de gols do time A: "))
gols_time_b = int(input("Informe a quantidade de gols do time B: "))

if gols_time_a > gols_time_b:
    print(f"O time A venceu a partida!")
elif gols_time_b > gols_time_a:
    print(f"O time B venceu a partida!")
else:
    print(f"A partidade ficou empatada!")