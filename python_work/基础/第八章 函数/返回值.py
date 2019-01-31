# -*- coding-utf-8 -*-
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


person = get_formatted_name('jimi', 'hendrix')
print(person)


def build_person(first_name, last_name, age=''):
    person1 = {'first': first_name, 'last': last_name}
    if age:
        person1['age'] = age
    return person1


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
