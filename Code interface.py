#Thêm thư viện tkinter
from tkinter import *

#Tạo một cửa sổ mới
window = Tk()

#Thêm tiêu đề cho cửa sổ
window.title('Welcome to VniTeach app')

#Đặt kích thước của cửa sổ
window.geometry('350x200')

#Thêm label có nội dung Hello, font chữ
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

#Xác định vị trí của label
lbl.grid(column=0, row=0)

btn = Button(window, text="Submit", bg="orange", fg="red")

#Thiết lập vị trí của nút nhấn có màu nền và màu chữ
btn.grid(column=1, row=0)

#Tạo một Textbox
txt = Entry(window,width=10)

#Vị trí xuất hiện của Textbox
txt.grid(column=1, row=0)

#Đặt vị trí con trỏ tại Textbox
txt.focus()

#Hàm xử lý khi nút được nhấn
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
top = Tk()
top.geometry("400x250")
Start = Label(top, text = "Start").place(x = 30, y = 50)
End = Label(top, text = "End").place(x = 30, y = 90)

e1 = Entry(top).place(x = 80, y = 50)
e2 = Entry(top).place(x = 80, y = 90)
btn = Button(top, text="Submit", bg="orange", fg="red")

#Thiết lập vị trí của nút nhấn có màu nền và màu chữ
btn.place(x=250, y=65)

#Tạo một Textbox
txt = Entry(window,width=10)

#Vị trí xuất hiện của Textbox
txt.grid(column=1, row=0)

#Đặt vị trí con trỏ tại Textbox
txt.focus()

#Hàm xử lý khi nút được nhấn
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

top.mainloop()
#Để tắt chức năng nhập của Textbox bằng state
#Lặp vô tận để hiển thị cửa sổ
window.mainloop()