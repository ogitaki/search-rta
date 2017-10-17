import codecs
import itertools

from progressbar import ProgressBar
import requests
from pyquery import PyQuery as pq


def main():
    name = input("Enter name to search for: ").upper().strip()
    bar = ProgressBar(max_value=12)
    for month in range(12, 0,-1):
        bar.update(12 - month)
        for day in range(32, 0,-1):
            r = requests.get(
                "http://avtoinstruktor.bg/rezultati/sofia/" + str(day) + "/" + str(month) + "/2017")
            print(findResults(r, name))


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
                return
            exam_type = person_info.parents('table').siblings('.well')('h5').html()
            exam_type = exam_type.split(' ')[-1].title()
            people.append({
                name,
                grade,
                exam_type
            })

        return people

if(__name__ == "__main__"):
    main()
