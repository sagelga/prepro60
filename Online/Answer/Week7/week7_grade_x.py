""" Grade X """
def calc(grade, weight, scnt, gde):
    """ Grade """
    result = ((grade * weight * scnt) - sum(gde)) / weight
    gde.append(result * weight)
    return result

def convert(grade):
    """ Convert grade to char """
    if grade == 4:
        return 'A'
    elif grade == 3.5:
        return 'B+'
    elif grade == 3:
        return 'B'
    elif grade == 2.5:
        return 'C+'
    elif grade == 2:
        return 'C'
    return convert2(grade)

def convert2(grade):
    """ Prevent Pylint Too many return """
    if grade == 1.5:
        return 'D+'
    elif grade == 1:
        return 'D'
    elif grade == 0:
        return 'F'

def main():
    """ Main function """
    num = int(input())

    # Define variable
    temp = {}
    subject = []
    scnt = 1
    sid = []
    grade = []
    gde = [0]

    for _ in range(num):
        temp['id'] = input()
        temp['name'] = input()
        temp['weight'] = float(input())
        subject.append(temp)
        temp = {}

    for _ in range(num):
        sid.append(input())
        grade.append(float(input()))

    for mcnt in range(num):
        for cnt in range(num):
            if subject[cnt]['id'] == sid[mcnt]:
                subject[cnt]['grade'] = calc(grade[mcnt], subject[cnt]['weight'], scnt, gde)
                scnt += 1

    # Sort by ID
    subject = sorted(subject, key=lambda k: k['id'])

    for data in subject:
        print("%s\t" %data['id'], "%s\t" %data['name'], convert(data['grade']), sep='')

main()
