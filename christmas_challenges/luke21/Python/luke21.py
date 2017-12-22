venner = ["Asgeir"]
fiender = ["Beate"]  # Lists of friends and enemies, to be filled.

relations_array = []
all_persons = []
with open("etterretningsrapport.txt", "r") as infile:
    for line in infile:
        words = line.split()
        relations_array.append(words)  # Filling the text-data into a nested list, for speed.
        for person in (words[1:3]):
            if not person in all_persons:  # Filling the "all_persons" list with people not previously added.
                all_persons.append(person)

found_someone = True
loop_nr = 0
while found_someone == True:
    found_someone = False
    for line in relations_array:
        relation, person1, person2 = line
        if not person2 in venner and not person2 in fiender:
            if person1 in venner:
                if relation == "vennskap":
                    venner.append(person2)
                    found_someone = True
                else:
                    fiender.append(person2)
                    found_someone = True
            elif person1 in fiender:
                if relation == "vennskap":
                    fiender.append(person2)
                    found_someone = True
                else:
                    venner.append(person2)
                    found_someone = True
        if not person1 in venner and not person1 in fiender:
            if person2 in venner:
                if relation == "vennskap":
                    venner.append(person1)
                    found_someone = True
                else:
                    fiender.append(person1)
                    found_someone = True
            elif person2 in fiender:
                if relation == "vennskap":
                    fiender.append(person1)
                    found_someone = True
                else:
                    venner.append(person1)
                    found_someone = True
    print("loop:", loop_nr)
    loop_nr += 1
    print("Friends:", len(venner))
    print("Enemies:", len(fiender))
    print("Neutrals:", len(all_persons) - len(fiender) - len(venner))



# print(venner)
# print(fiender)
print(len(venner))
print(len(fiender))

for friend in venner:
    for enemy in fiender:
        if enemy == friend:
            print(friend, enemy)
