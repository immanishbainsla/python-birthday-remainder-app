# Import OrderedDict
from collections import OrderedDict

# Created a Dictionary variable to store Name and Birthday's
birthdaydict = OrderedDict()

# Variable to control while Loop
exitvar = True

# While Loop starts
while exitvar:

    print('\n------------------------- Birth Day App -------------------------')
    print('\t1. Show Birthday List.')
    print('\t2. Add Birthday to List.')
    print('\t3. Exit.')

    choice = int(input('\n\tEnter the Choice : '))

    if choice == 1:
        if len(birthdaydict.keys()) == 0:
            print('\t->Nothing to show.\n')

        else:
            print('\n\tSelect search method : ')
            print('\t\t1. Name Search. ')
            print('\t\t2. Birth Date Search. ')
            print('\t\t3. Show Full List. ')

            choice1 = int(input('\n\t\tEnter the Choice : '))

            if choice1 == 1:
                name = input('\n\t\tEnter Name to Search in List : ')
                name = name.title()

                if name in birthdaydict.keys():
                    print(f"->\t\t{name}'s Birthday is on {birthdaydict[name]}.")

                else:
                    print('\t\t->No Data Found.\n')

            elif choice1 == 2:
                dt = input('\n\t\tEnter Birth Date to Search in List : ')
                if dt in birthdaydict.values():
                    print(f"\t\t->{name}'s Birthday is on {birthdaydict[name]}.")

                else:
                    print('\t\t->No Data Found.\n')

            elif choice1 == 3:
                i = 1
                for k, v in birthdaydict.items():
                    print(f"\t\t->{i}. {k}'s Birthday is on {v}.")

            else:
                print('\n\n\t->Choose a Valid Option.\n')

    elif choice == 2:
        name = input('\tEnter Name : ')
        name = name.title()
        bdate = input('\tEnter Birthdate : ')
        birthdaydict[name] = bdate
        print('\n\tBirthday Added.\n')

    elif choice == 3:
        exitvar = False

    else:
        print('\n\t->Choose a Valid Option.\n')




