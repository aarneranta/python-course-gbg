# Write a Python script to concatenate following dictionaries to create a new one.
# merge_dicts:
#
# d1={1:10, 2:20}
# d2={3:30, 4:40}
# dicts = (d1, d2, d3)
#
# Expected Result : merge_dicts(dicts) => {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def merge_dicts(dicts):
    out = {}
    for d in dicts:
        out |= d
    return out

# Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x). Go to the editor
#
# Expected Result : power_dict(5) => {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def power_dict(n):
    d={}
    for i in range(1,n+1):
        d[i] = i**2
    return d

# *** Bonus: Ej från övningen! ***

# Write a Python script that takes a dict with students as input and returns a
# list sorted by them by their average grade as output.
# Input is assumed to look like this:
# students = {"Sara" : {"TIN214": 5, "TMA970": 3, "TDA416": "U"},
#            "Pelle" : {"TMA970": 4, "TDA416": 5},
#            "Måns" : {"TIN214": "U"},
#            "Anna-Karin" : {"TIN214": 5, "TMA970": 4, "PPU073": 5}}


def avg_grade(courses): # Hjälpfunktion som kallas från sort_students()!
    avg = 0
    for coursename in courses:
        if courses[coursename] != "U": # Vi räknar "U" som värt noll poäng.
            avg += courses[coursename]/len(courses)
    return avg

def sorted_students(students):
    out = {}
    for name in students:
        out[name] = avg_grade(students.get(name)) # Till exempel: out = {"Sara": 2.6666666666666665}
    return sorted(out, key = out.get, reverse = True) # Vi vill sortera efter medelbetyg, samt från bäst betyg till sämst.
