from tkinter import *

root = Tk()

label_1 = Label(root, text="Password *")
label_2 = Label(root, text="Password Again *")

entry_1 = Entry(root, show='*')
entry_2 = Entry(root, show='*')

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

password = StringVar()
password_again = StringVar()

def password_check(password): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(password) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(password) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in password): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in password): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in password): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in password): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 
  
def main():
    if (password_check(password)):
        print("Password is valid")
    else: 
        print("Invalid Password !!")         
if __name__ == '__main__': 
    main()


Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
