import tkinter
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Calculator" )


# define font
myFont = font.Font(family='Helvetica', size=18, weight='bold')



# to make size fixed
root.resizable(0, 0)
# to set size of gui
root.geometry("305x455")



# set background
# C = Canvas(root, bg="blue", height=250, width=300)
# filename = PhotoImage(file = "E:\sh.png")
# background_label = Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)




def button_click(item):
    global expression

    expression = expression + str(item)

    input_text.set(expression)




def btn_clear():
    global expression

    expression = ""

    input_text.set("")



def btn_equal():
    global expression

    result = str(eval(expression))  # 'eval' function evalutes the string expression directly

    input_text.set(result)

    expression = ""


expression = ""

# 'StringVar()' is used to get the instance of input field

input_text = StringVar()


# set the screen of displaying text
input_field = Entry(root , font=('arial', 16, 'bold' ) ,textvariable = input_text  ,  foreground="white", bd = 32 , insertwidth = 4 , bg="green" , justify = "center" )

# set placeholder
input_field.insert(0, "Start Calculating..." )



input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

btns_frame = Frame(root, width=312, height=272.5, bg="#eee")

btns_frame.pack()

#  relief=RAISED ,borderwidth=4 , effect of button

#Define buttons
button_1 = Button(btns_frame ,  relief=RAISED , borderwidth=4, text="1" , fg="black", font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command =lambda :button_click(1)).grid(row= 3, column=0)
button_2 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="2" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(2)).grid(row= 3, column=1)
button_3 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="3" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(3)).grid(row=3 , column=2)
button_4 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="4" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(4)).grid(row=2 , column=0)
button_5 = Button(btns_frame ,  relief=RAISED ,borderwidth=4, text="5" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(5)).grid(row=2 , column=1)
button_6 = Button(btns_frame ,  relief=RAISED ,borderwidth=4, text="6" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(6)).grid(row= 2, column=2)
button_7 = Button(btns_frame ,  relief=RAISED ,borderwidth=4, text="7" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(7)).grid(row=1 , column=0)
button_8 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="8" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(8)).grid(row=1 , column=1)
button_9 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="9" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(9)).grid(row= 1, column=2)
button_0 = Button(btns_frame , relief=RAISED ,borderwidth=4, text="0" ,fg="black",font=('arial', 12, 'bold' ) , padx =25 , pady=17 , command = lambda :button_click(0)).grid(row=4 , column=0)

button_add = Button( btns_frame, relief=RAISED ,borderwidth=4,text="+" ,fg="black", padx =25 , pady=17 , font=('arial', 12, 'bold' ) , bg="orange", command = lambda:button_click("+")).grid (row = 2 , column = 3)
button_equal = Button(btns_frame , relief=RAISED ,borderwidth=4, text="=" ,fg="black", padx =61 , pady=17 , font=('arial', 12, 'bold' ) , bg="green" , command = lambda: btn_equal()).grid(row=5 , column =0 , columnspan=2 )
button_clear = Button(btns_frame , relief=RAISED ,borderwidth=4, text="C" ,fg="black", padx =24 , pady=17 , font=('arial', 12, 'bold' ) , bg="green" ,command =lambda: btn_clear()).grid(row =1 ,column = 3 )
button_min = Button(btns_frame , relief=RAISED ,borderwidth=4, text="-" ,fg="black", padx =27 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command =lambda: button_click("-")).grid(row=3 , column =3 )
button_dot = Button(btns_frame , relief=RAISED ,borderwidth=4, text="." ,fg="black", padx =27 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command = lambda:button_click(".")).grid(row=4 , column = 1)
button_divide = Button(btns_frame , relief=RAISED ,borderwidth=4, text="/" ,fg="black", padx =28 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command = lambda:button_click("/")).grid(row=4 , column =2 )
button_mult = Button(btns_frame ,  relief=RAISED ,borderwidth=4,text="*" ,fg="black", padx =26 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command = lambda:button_click("*")).grid(row= 4, column = 3)
button_l_bracket = Button(btns_frame , relief=RAISED ,borderwidth=4, text="(" ,fg="black", padx =27 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command =lambda: button_click("(")).grid(row= 5, column =2 )
button_r_barcket = Button(btns_frame , relief=RAISED ,borderwidth=4, text=")" ,fg="black", padx =27 , pady=17 , font=('arial', 12, 'bold' ) ,bg="orange", command =lambda: button_click(")")).grid(row=5 , column =3 )






root.mainloop()