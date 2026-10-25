from pathlib import Path
import os
def readfileandfolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i, item in enumerate (items):
        print(f"{i+1} : {item}")


def create():
    try:
        readfileandfolder()
        name = Path(input("enter file name: "))
        p = Path(name)

        if not p.exists() and p.is_file:
            with open (p,'w') as fs:
                data = input("what want to write in this file:-")
                fs.write(data)
            print("file created sucessfully")

        else:
            print("this file alreaady  exists")

    except Exception as err:
        print(f"as error occurd {err}")


def readfile():
    try:
    
        readfileandfolder()
        name = Path(input("enter a file name :-"))
        p = Path(name)
        if name.exists() and p.is_file:
            with open (p,"r") as fs:
               data = fs.read()
               print(data)
               print("data read sucessfully")

        else:
            print("this file is not exists")

    except Exception as err:
        print(f"as error occured{err}")

def updatfile():
    try:
        readfileandfolder()
        name = input("which file you want to update pls enter a name:- ")
        p = Path(name)

        if p.exists()and p.is_file() :
            print("press 1 for rename a file:- ")
            print("press 2 for overwritting a data of your file:- ")
            print("press 3 for appending a some content in a file:- ")

            res = int(input("please tell your number:- "))
            
            if res ==1:
                name2 = input("write a file you want to rename:- ")
                p2 = Path(name2)
                p.rename(p2)
                print("file rename sucessfully")

            elif res == 2:
                with open(p,"w") as fs:
                    data =input("write a data you want to overwrite:- ")
                    fs.write(data)
                    print("data overwrite sucessfully")

            elif res ==3:
                with open(p,"a") as fs:
                    data = input("write a data you want to append:- ")
                    fs.write(data)
                    print("data append sucessfully")

            else:
                print("Invalid choice")

    except Exception as err:
        print(f"as occur some error{err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("writw a name which file you want to delete:- ") 
        p =Path(name)

        if p.exists and p.is_file:
            os.remove(p) 
            print("file deleted suessfully.")

    except Exception as err:
            print(f"as occur some error{err}")     


    
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updatingg a file")
print("press 4 for deleting a file")

check = int(input("please enter a number between 1 to 4 :-"))



if check==1:
    create()

if check == 2:
    readfile()

if check == 3:
    updatfile()

if check == 4:
    deletefile()

