task_to_be_done = []
task_done = []
games_in_progress = []
games_finished = []
figures_in_painting = []
figures_finished = []
models_in_making = []
models_finished = []
good_primary_choice = ['T', 'G', 'F', 'M']
good_secondary_choice = ['A', 'L', 'R', 'F']


def actions():
    print('Hello !')
    choice = input('What to do ? \n (T)ask \n (G)ames \n (F)igures \n (M)odels \n ->')
    choice = choice.capitalize()
    while choice not in good_primary_choice:
        choice = input('What to do ? \n (T)ask \n (G)ames \n (F)igures \n (M)odels \n ->')
        choice = choice.capitalize()
    else:
        if choice == 'T':
            choice_of_t = input(' (A)dd \n (L)ist \n --> ')
            choice_of_t = choice_of_t.capitalize()
            while choice_of_t not in good_secondary_choice:
                choice_of_t = input(' (A)dd \n (L)ist \n --> ')
                choice_of_t = choice_of_t.capitalize()
            else:
                pass

        elif choice == 'G':
            pass
        elif choice == 'F':
            pass
        elif choice == 'M':
            pass


def status_check():
    pass


def main():
    actions()


if __name__ == '__main__':
    main()