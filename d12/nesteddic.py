course={
    'php':{'name':'seema','marks':30},
     'java':{'name':'armi','marks':35},
      'python':{'name':'mansi','marks':25}
}
print(course['php']['marks'])

for a,b in course.items():
    print(a,b['name'],b['marks'])

    