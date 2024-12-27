from operator import itemgetter

class StudentGroup:
    """Студенческая группа"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    """Учебный курс"""
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class GroupCourse:
    """Связь между группами и курсами (многие ко многим)"""
    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id
# Студенческие группы
groups = [
    StudentGroup(1, 'Group 101'),
    StudentGroup(2, 'Group 202'),
    StudentGroup(3, 'Group 303'),
    StudentGroup(4, 'Group 404'),
]

# Учебные курсы
courses = [
    Course(1, 'Math', 3),
    Course(2, 'Physics', 4),
    Course(3, 'Programming', 5),
    Course(4, 'History', 2),
]

# Связь между группами и курсами (многие ко многим)
group_courses = [
    GroupCourse(1, 1),
    GroupCourse(1, 2),
    GroupCourse(2, 2),
    GroupCourse(2, 3),
    GroupCourse(3, 1),
    GroupCourse(3, 3),
    GroupCourse(4, 4),
    GroupCourse(4,1),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим (предположим, что группа привязана к одному куратору)
    one_to_many = [(c.name, c.credits, g.name)
                   for g in groups
                   for c in courses
                   if g.id == 1 and c.id == 2]  #

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, gc.course_id, gc.group_id)
                         for c in courses
                         for gc in group_courses
                         if c.id == gc.course_id]

    many_to_many = [(g.name, course_name, c.credits)
                    for course_name, course_id, group_id in many_to_many_temp
                    for g in groups if g.id == group_id
                    for c in courses if c.id == course_id]

    print('Задание 1')
    # «Студенческая группа» и «Учебный курс» связаны соотношением один-ко-многим (по куратору). Выведите список всех курсов, у которых название начинается с буквы «P», и названия их групп.
    res_1 = [(course, credits, group) for course, credits, group in one_to_many if course[0] == 'P']
    print(res_1)

    print('\nЗадание 2')
    # «Студенческая группа» и «Учебный курс» связаны соотношением один-ко-многим. Выведите список групп с минимальным количеством кредитов у курсов в каждой группе, отсортированный по минимальному количеству кредитов.
    res_2_unsorted = []
    # Перебираем все группы
    for g in groups:
        # Список курсов группы
        g_courses = list(filter(lambda i: i[2] == g.name, many_to_many))
        # Если группа не пустая
        if len(g_courses) > 0:
            # Список кредитов курсов группы
            g_credits = [credits for _, _, credits in g_courses]
            # Минимальное количество кредитов
            g_min = min(g_credits)
            res_2_unsorted.append((g.name, g_min))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    print('\nЗадание 3')
    # «Студенческая группа» и «Учебный курс» связаны соотношением многие-ко-многим. Выведите список всех связанных групп и курсов, отсортированный по группам, сортировка по курсам произвольная.
    res_3 = sorted(many_to_many, key=itemgetter(0))
    print(res_3)


if __name__ == '__main__':
    main()
