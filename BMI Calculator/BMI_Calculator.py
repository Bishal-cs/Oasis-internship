#------------------------------------------------------ BMI Calculator ----------------------------------------------------------
from tkinter import *
from tkinter import ttk
# colors code -----------------------------------

c1 = '#778899'   #lightslategray		
c2 = '#0F0F0F'   #Black
c3 = '#A2B5CD'   #lightsteelblue3		

layout = Tk()
layout.title('BMI Calculator')
layout.geometry('295x230')
layout.resizable(height=False, width=False)
layout.configure(bg=c3)

# Functions -----------------------------------
def calculate_bmi():
    weight = float(e_weight.get())
    height = float(e_height.get()) ** 2
    result = weight / height

    if result < 18.4:
        L_result_text['text'] = "Your BMI is Underweight"       
    elif result >= 18.4 and result < 24.9:
        L_result_text['text'] = "Your BMI is Normal"    
    elif L_result >= 25 and result < 29.9:
        L_result_text['text'] = "Your BMI is  Overweight"    
    else:
        return "Obesity"
    L_result["text"] = '{:{}f}'.format(result, 2)

# Frame Work--------------------------------------

top_frame = Frame(layout, width= 295, height=50, bg=c3, pady=0, padx=0)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(layout, width= 295, height=50, bg=c3, pady=0, padx=0)
bottom_frame.grid(row=1, column=0)

app_label = Label(top_frame, text="BMI Calculator", width=23, height=1, padx=0, anchor = "center", font=("Ivy 16 bold"), bg=c3, fg=c2)
app_label.place(x=0, y=2)

app_line =Label(top_frame, text="", width=400, height=1, padx=0, anchor = "center", font=("Arial 1"), bg=c1, fg=c2)
app_line.place(x=0, y=35)

l_weight = Label(bottom_frame, text = "Enter Your Weight", height = 1, padx = 0, anchor = "center", font = ("Ivy 10 bold"), bg = c3, fg = c2)
l_weight.grid(row = 0, column = 0, columnspan = 1, pady = 10, padx = 3)
e_weight = Entry(bottom_frame, width = 5, justify = "center", font = ("Ivy 10 bold"), relief = "solid")
e_weight.grid(row = 0, column = 1, columnspan = 1, pady = 10, padx = 3)

l_height = Label(bottom_frame, text = "Enter Your Height", height = 1, padx = 0, anchor = "center", font = ("Ivy 10 bold"), bg = c3, fg = c2)
l_height.grid(row = 1, column = 0, columnspan = 1, pady = 10, padx = 3)
e_height = Entry(bottom_frame, width = 5, justify = "center", font = ("Ivy 10 bold"), relief = "solid")
e_height.grid(row = 1, column = 1, columnspan = 1, pady = 10, padx = 3)

L_result = Label(bottom_frame, width= 6, height = 2, text= "---", padx = 6, pady= 12, anchor = "center", font = ("Ivy 10 bold"), bg = c1, fg = c2)
L_result.place(x = 200, y = 13)

L_result_text = Label(bottom_frame, width= 37, height = 1, text= "", padx = 6, pady= 12, anchor = "center", font = ("Ivy 10 bold"), bg = c1, fg = c2)
L_result_text.place(x = 0, y = 85)

b_Calculate = Button(bottom_frame, text = "Calculate", font = ("Ivy 10 bold"), width = 34, height = 1, bg=c1, fg=c2, anchor="center", command = calculate_bmi) 
b_Calculate.grid(row = 4, column = 0, columnspan = 30, pady = 60, padx = 5)

layout.mainloop()