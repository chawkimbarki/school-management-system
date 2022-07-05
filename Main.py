from time import sleep
import os
import pickle






"""=================================================== Clear Function ==================================================="""






# define our clear function
def clear():
  
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')






"""=================================================== Main Classes ==================================================="""






class student:
    def __init__(self, name, prename, score, clas, rank, description):
        self.name = name
        self.prename = prename
        self.score = score
        self.clas = clas
        self.rank = rank
        self.description = description
        
    def __str__(self):
        return (f"Name : {self.name} | prename : {self.prename} | score : {self.score} | class : {self.clas} | rank : [{self.rank}]")  



    
class clas:
    def __init__(self, level, number, orientation, score, number_of_students):
        self.level = level
        self.number = number
        self.orientation = orientation
        self.score = score
        self.number_of_students = number_of_students

    def __str__(self):
        return (f"{self.level} {self.orientation} {self.number}")




class year:
    def __init__(self):
        self.start == self[0:4]
        self.ends == self[7:]
        return (int(self.start))

    """--- this function will create a folder in this form ("20xx" - "20xx + 1") exemple input = ("2020")  ------>  the folder name = output = ("2020 - 2021") ---"""
    def create_new_year(path):
        sleep(1)
        clear()

        while True:
            while True :
                year = input("In Wich Year Are We : ")

                try:
                    if (2000 < int(year) < 2050):
                        break
                except ValueError:
                    sleep(1)
                    clear()
                    print("Error : The year must be written in this form (20XX)  |\nExemple : 2022")
                    sleep(4)
                    clear()

            if year in files_structure(path):
                sleep(0.5)
                clear()
                print("Error : This year already exists")


            else:
                year = (f"{int(year)} - {int(year) + 1}")
                break

        os.mkdir(f"{path}\\{year}")
    
    """--- this function will show a list of the folders contained in "path" """
    def show_years(path):
        sleep(2)
        clear()
        i = 0
        for file in files_structure(path):
            print(file, end="  |  ")
            i += 1
            if i == 5 :
                print("\n")
                i = 0






"""=================================================== Functions  ==================================================="""






"""--- this functions returns a list of files in directory (path) ---"""
def files_structure(path):
    filesinfolder = os.listdir(path)
    return filesinfolder






"""=================================================== Main Functions ==================================================="""






"""--- this function will show the user a text contains a number of options that the user can shoose from to show/manupilate the data ---"""
def choice():

    sleep(4)
    while True:
        clear()
        print("Choose what you want to do by typing the number of the option you want\n\n\n\n"
            "1 . Show Years (From here you can (show / create / delete / modify) informations of any student or class from saved data throughout the past years)\n\n\n"
            "2 . Show statics (dropping out of school rate / the change of the students number/...)\n\n\n"
            "3 . add a new year,class or student\n\n\n")
        choice = int(input("Your Choice : "))
        if (1 <= choice <= 3):
            break
        else:
            print("! Your Choice must be a number of one of the options above !")
            sleep(3)
            

    return choice



def new():
    clear()
    sleep(1)
    print("Add a :")
    print("   1 .  New Year.\n\n\n"
            "   2 .  New Class\n\n\n"
            "   3 .  New Student\n\n\n")
    
    A = True

    try:
        choice = int(input("Your Choice : "))

    except ValueError:
        A = False
        print("! Your Choice must be a number of one of the options above !")
        sleep(3)

    if A and (1 <= choice <= 3):
        return choice

    else :
        print("! Your Choice must be a number of one of the options above !")
        sleep(3)    






"""=================================================== Main Program ==================================================="""






"""--- the main menue function (read the name agin)"""
def main_menu(path):
    print("\n\nWelcome \n\n Here you can (See / Create / delete or modify) students's or classes's informations or you can show statics of the school \n")
    
    your_choice = choice()

    if your_choice == 1:
        year.show_years(path)
    elif your_choice == 2:
        show_statics() ### I need to work on this
    else :
        New()




"""here is the main function that'll be the first to run"""    
def main():
    clear()
    path = ("D:\\0 . Mbarki\\2 . Projects\\0 . Computer Science\\0 . School\Years")
    if files_structure(path) == []:
        print("\n! There is no data in the specifyed directotie !\n\n")
        print("Create a new year")
        sleep(4)
        year.create_new_year(path)
    main_menu(path)




main()






########################################################  Test Area  ######################################################






""" info_class = clas(4, 1, "info", 20, 9)

st = student("chakwi", "mbarki", "20.0", info_class, "1", "good student")
st2 = student("ahmed ", "hajji ", "19.5", info_class, "2", "normal student")

students = [st, st2]

for studentt in students:
    print(studentt) """