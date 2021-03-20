import people_also_ask

x = people_also_ask.get_related_questions("UPSC")

for i in x:
    print(i)
    for j in people_also_ask.get_related_questions(i):
        print(j)

