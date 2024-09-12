# Nested list have a list inside the list
#/playerScore = [["James",10], ["souza", 20], ["perez", 16]]
#sorted(set(scores)) = basicamente organiza a lista e de pontuação
#e retira as duplicadas


#esses são os ingredientes
def sort_students(names_score):
    scores = []
    for student in names_score:
        scores.append(student[1])

    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]

    names_second_lowest = []
    for student in names_score:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)

    for name in names_second_lowest:
        print(name)




# e essa é a preparação
if __name__ == '__main__':
    names_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_score.append([name, score])

# e para finalizar precisamos USAR os ingredientes
    sort_students(names_score)        