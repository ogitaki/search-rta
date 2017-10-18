import codecs
import itertools

import requests
from progressbar import ProgressBar
from pyquery import PyQuery as pq


def main():
    name = "ОГНЯН"#input("Enter name to search for: ").upper().strip()
    year = '2017'#input("Enter year: ")
    bar = ProgressBar(max_value=12)
    i = 0
    for month in range(9, 8, -1):
        bar.update(12 - month)
        if(i == 0):
            print('\n')
        i+=1
        for day in range(32, 0, -1):
            response = requests.get(
                "http://avtoinstruktor.bg/rezultati/sofia/" + str(day) + "/" + str(month) + "/2017")
            people_found = findResults(response, name)
            if len(people_found) > 0:
                print("{}.{}.{}:".format(day, month, year))
                print(formatOutput(people_found))


def findResults(r, name):
    people = []
    tree = pq(r.content)
    name_count = len(name.split())
    if name_count == 2:
        by_name = tree(".visible-sm:contains('" + name + "')").parents('tr')
    elif name_count == 1:
        by_name = tree(".visible-lg:contains('" + name + " ')").parents('tr')
    else:
        by_name = tree(".visible-lg:contains('" + name + "')").parents('tr')
    for i in itertools.count():
        person_info = by_name.eq(i)
        name = person_info('.visible-lg').html()
        grade = person_info('.label').html()
        if name is None:
            break
        exam_type = person_info.parents('table').siblings('.well')('h5').html()
        exam_type = exam_type.split(' ')[-1].title()
        people.append({
            'name': name,
            'grade': grade,
            'exam_type': exam_type
        })

    return people


def formatOutput(people):
    full_result = ""
    for person in people:
        full_result += "{}, {}, {}".format(person['name'], person['exam_type'], person['grade'])
    return full_result

if(__name__ == "__main__"):
    main()
