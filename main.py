def read_input_file():
    preferences_survey = open('input.txt')
    results = preferences_survey.readlines()
    employees_beers = results[0]
    answers = results[1]
    print('\nNumber of employees and beer sorts:\n', employees_beers)
    print('Answers about preferred beer:\n', answers)
    employees = int(employees_beers.split(' ')[0])
    beers = int(employees_beers.split(' ')[1])
    preferences = answers.split(' ')
    return employees, beers, preferences


def employees_fav_beers():
    employees, beers, preferences = read_input_file()
    employees_preferences = []

    for i in range(employees):
        fav_beers = []
        for k in range(beers):
            if preferences[i][k] == 'Y':
                fav_beers.append(k+1)
        employees_preferences.append(fav_beers)

    return employees_preferences


def minimum_beers_required(preferences):
    preferences.sort(key=len)
    other_preferences = preferences
    beers_required = 0

    while other_preferences:
        preferences = other_preferences
        print('\n', other_preferences)
        beer_preferences_number = dict()

        for beer in preferences[0]:
            beer_likes = 0
            for i in preferences:
                if beer in i:
                    beer_likes += 1
            beer_preferences_number[beer] = beer_likes
        print('{Sort: likes} ==>', beer_preferences_number)

        type_of_beer = max(beer_preferences_number, key=beer_preferences_number.get)

        other_preferences = []
        for i in preferences:
            if type_of_beer not in i:
                other_preferences.append(i)
        beers_required += 1

    print('\n------------------------------------\nMinimum number of beers required: ', beers_required)


if __name__ == '__main__':
    info = employees_fav_beers()
    minimum_beers_required(info)
