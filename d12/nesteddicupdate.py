course={
    'php':{'name':'seema','marks':30},
     'java':{'name':'armi','marks':35},
      'python':{'name':'mansi','marks':25}
}

course.update({'flutter':{'name':'herry'}})
# course['php']['marks']=37
print(course)
print()

del course['python']['marks']
print(course)

