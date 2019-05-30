
# a=20
# b=30
# a, b =b, a
# print("swap value of a and b are",a,b)
#
# #additiona=input("enter first number")print(a) print(b)p=int(a+bprint("p")ut
# a=input("enter first number")
# a=int(a)
# b=input("enter second number")
# b=int(b)
# c=a+b
# print("sum:",c)
#
# #nt(input("entech=input("enteelif ch =='-':    result=a - b* elif ch ==a
# i=1
# while i<=5:
#     print('*' * i)
#     i=i+1

##exception handling
# var_1 = input('enter the value of first number:')
# var_2 = input('enter the value of second number')
#
# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if(var_2 !=0):
#         result = var_1/var_2
#         print('divison result is:',result)
#     else:
#         print('value of second variable cannnot be zero')
# except ValueError:
#     print('can only enter value')

#exception  handling in calculator
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('calculator')

label = tk.Label(root, text ="enter first number",pady=(10))
label.pack()

first_number_entry = tk.Entry(root)
first_number_entry.pack()

label2 = tk.Label(root, text ='enter second number')
label2.pack()

second_number_entry= tk.Entry(root)
second_number_entry.pack()

operation = tk.Label(root, text ="operations")
operation.pack()

def addition():

    first, second = takeValueInput()
    result = first + second
    #print(first+second)
    result_label.config(text= 'operations result is' + str(result))

def subtact():
     first, second = takeValueInput()
     result =first - second
     result_label.config(text = 'operations result is' + str(result))

def multiply():
    first, second = takeValueInput()
    result =first * second
    result_label.config(text = 'operations result is' + str(result))

def divide():
    first, second = takeValueInput()

    if second ==  0:
      messagebox.showerror("Error", "cannot divide the value by o.")
    else:
       result = first / second
       result = round(result, 2)
       result_label.config(text = 'operations result is' + str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first,second
    except ValueError:
        if((len (first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
          messagebox.showerror('error', "please enter a value")
        else:
          messagebox.showerror('error', "enter only integer value")
        quit(0)

addition_button =tk.Button(root,text ="+",command = lambda :addition())
addition_button.pack()

minus_button = tk.Button(root, text="-", command=lambda: subtact())
minus_button.pack()

multiply_button = tk.Button(root, text="*", command=lambda: multiply())
multiply_button.pack()

divison_button = tk.Button(root, text="/", command=lambda: divide())
divison_button.pack()

result_label = tk.Label(root, text ="operations result is:")
result_label.pack()

root.mainloop()











