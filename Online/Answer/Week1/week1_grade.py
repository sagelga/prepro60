""" Grade """
def main():
    """ Main function """
    scr = int(input())
    print('%g' % grader(scr))

def grader(scr):
    """ Grade """
    m_than_49 = scr - (scr % 50) - 49
    m_than_49 = max(m_than_49, -1)
    m_than_49 = min(m_than_49, 1)

    scr -= 49
    scr = max(scr, 0)
    scr = min(scr, 50)

    grade = (scr / 10) + 0.2
    grade = (round(grade * 2) / 2) + 0.5

    grade *= m_than_49

    grade = max(grade, 0)
    grade = min(grade, 4)

    return grade

main()
