#Dictionary

birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'} #dictonary

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == ' ':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name) #will pull the date from the dictinary and output with a string and variable
    else:
        print('I dont have the birthday information for' + name)
        print('what is their birthday')
        bday = input()
        birthdays[name] = bday # updates the dictionary with the name and birthday of the new person
        print('Birthday list has been updated')