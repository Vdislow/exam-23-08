import datetime
from user.models import Student, Mentor, Language, Course

languages = [
    {
        'name': 'Python',
        'months_to_learn': 6
    },
    {
        'name': 'Java Script',
        'months_to_learn': 6
    },
    {
        'name': 'UX-UI',
        'months_to_learn': 2
    },
]

for lan in languages:
    prog = Language.objects.create(name=lan['name'], month_to_learn=lan['months_to_learn'])

students = [
    {
        'name': 'Amanov Aman',
        'email': 'aman@mail.ru',
        'phone_number': '+996700989898',
        'work_study_place': 'School №13',
        'has_own_notebook': True,
        'preferred_os': 'windows'
    },
    {
        'name': 'Apina Alena',
        'email': 'aapina@bk.ru',
        'phone_number': '0550888888',
        'work_study_place': 'TV',
        'has_own_notebook': True,
        'preferred_os': 'mac'
    },
    {
        'name': 'Phil Spencer',
        'email': 'spencer@microsoft.com',
        'phone_number': '0508312312',
        'work_study_place': 'Microsoft Gaming',
        'has_own_notebook': False,
        'preferred_os': 'linux'
    }
]

for stu in students:
    stud = Student.objects.create(name=stu['name'],
                                  email=stu['email'],
                                  phone_number=stu['phone_number'],
                                  work_study_place=stu['work_study_place'],
                                  has_own_notebook=stu['has_own_notebook'],
                                  preferred_os=stu['preferred_os'])

# mentors = [
#     {
#         'name': 'Ilona Maskova',
#         'email': 'imask@gmail.com',
#         'phone_number': '0500545454',
#         'main_work': None,
#         'experience': datetime.date(year=2021, month=10, day=23)
#     },
#     {
#         'name': 'Halil Nurmuhametov',
#         'email': 'halil@gmail.com',
#         'phone_number': '0709989876',
#         'main_work': 'University of Fort Collins',
#         'experience': datetime.date(year=2010, month=9, day=18)
#     }
# ]
#
# for met in mentors:
#     Mentor.objects.create(name=met['name'],
#                           email=met['email'],
#                           phone_number=met['phone_number'],
#                           main_work=met['main_work'],
#                           experience=met['experience'])



