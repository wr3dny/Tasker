games_in_progress = []
games_finished = []
figures_in_painting = []
figures_finished = []
models_in_making = []
models_finished = []
good_primary_choice = ['T', 'G', 'F', 'M']
good_secondary_choice = ['A', 'L', 'R', 'F']


def hello_screen():
    print('Hello !')
    choice = input('What to do ? \n (T)ask \n (G)ames \n (F)igures \n (M)odels \n ->')
    choice = choice.capitalize()
    while choice not in good_primary_choice:
        choice = input('What to do ? \n (T)ask \n (G)ames \n (F)igures \n (M)odels \n ->')
        choice = choice.capitalize()
    else:
        return choice


def tasker():
    task_to_be_done = []
    task_done = []
    task_removed = []
    print('Welcome to tasks')
    t_choice = input('What to do ? \n (L)ist \n (R)emove \n (F)inish \n (A)dd')
    t_choice = t_choice.capitalize()
    while t_choice not in good_secondary_choice:
        t_choice = input('What to do ? \n (L)ist \n (R)emove \n (F)inish \n (A)dd')
    else:
        if t_choice == 'L':
            print(task_to_be_done)
        elif t_choice == 'R':
            print(task_to_be_done)
        elif t_choice == 'F':
            print(task_to_be_done)
        elif t_choice == 'A':
            task_to_be_done.append(input('Describe new task '))
            print(task_to_be_done)




# def distributor(ch):
#         if ch == 'T':
#             return = T
#         elif ch == 'G':
#             return
#         elif choice == 'F':
#             pass
#         elif choice == 'M':
#             pass


def status_check():
    pass


def main():
    first_choice = hello_screen()
    tasker()




if __name__ == '__main__':
    main()