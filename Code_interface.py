#Thêm thư viện tkinter
from tkinter import *



top = Tk()
top.title('DIRECTOR')
top.geometry("400x250")
Start = Label(top, text = "Start").place(x = 30, y = 50)
End = Label(top, text = "End").place(x = 30, y = 90)

    
e1 = Entry(top).place(x = 80, y = 50)
e2 = Entry(top).place(x = 80, y = 90)
def clicked():
    return selected,e1,e2
        
btn = Button(top, text="Submit", bg="white", fg="red",command=clicked)
selected = 0
rad1 = Radiobutton(top,text='Input place_name', value=1, variable=selected)
rad2 = Radiobutton(top,text='Input coordinates', value=2, variable=selected) 
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)  
#Thiết lập vị trí của nút nhấn có màu nền và màu chữ
btn.place(x=250, y=65)



#Vị trí xuất hiện của Textbox
top.mainloop()

#Lặp vô tận để hiển thị cửa sổ
