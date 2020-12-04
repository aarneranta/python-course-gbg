def killer(suspects, dead_people):
    for suspect, seen in suspects.items():
        if all(dead_person in seen for dead_person in dead_people):
            return suspect
