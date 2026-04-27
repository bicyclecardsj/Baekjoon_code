fbi_agents = []

for i in range(1, 6):
    name = input()
    
    if "FBI" in name:
        fbi_agents.append(i)

if fbi_agents:
    print(*(fbi_agents))
else:
    print("HE GOT AWAY!")
