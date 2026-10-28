import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("310x400")
root.title("calculator")
root.configure(fg_color="#070707")

font = "Consolas", 25, "bold"
font_button = "Consolas", 20, "bold"
bg_color = "#202020"
hover_color = "#202020"
text_color = "#FF6F00"
text_color_2 = "#FFFFFF"

def add_number(number):
    display.configure(state="normal")
    display.insert("end", number)
    
def add_to_disp(value):
    display.configure(state="normal")
    display.insert("end", value)
    display.configure("readonly")
    
def clear_disp():
    display.configure(state = "normal")
    display.delete(0, "end")
    display.configure("readonly")
    
def clear_disp_1():
    display.configure(state = "normal")
    display.delete(0, 1)
    display.configure("readonly")
    
def calc():
    result = eval(display.get())
    display.configure(state="normal")
    display.delete(0, "end")
    display.insert(0, str(result))
    display.configure(state="readonly")

display = ctk.CTkEntry(root, font = font, justify="right", state="readonly", width=270, height=50)
display.place(y = 30, x = 20)

button = ctk.CTkButton(root, text = "C", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: clear_disp())
button.place(y = 140, x = 25)

button = ctk.CTkButton(root, text = "÷", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: add_to_disp("/"))
button.place(y = 140, x = 220)

button = ctk.CTkButton(root, text = "×", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: add_to_disp("*"))
button.place(y = 190, x = 220)

button = ctk.CTkButton(root, text = "-", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: add_to_disp("-"))
button.place(y = 240, x = 220)

button = ctk.CTkButton(root, text = "+", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: add_to_disp("+"))
button.place(y = 290, x = 220)

button = ctk.CTkButton(root, text = "=", fg_color=text_color, hover_color=text_color, text_color=text_color_2, font = font_button, width=60, height=40, corner_radius=13, command=calc)
button.place(y = 340, x = 220)

button = ctk.CTkButton(root, text = ",", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_to_disp(","))
button.place(y = 340, x = 155)

button = ctk.CTkButton(root, text = "%", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: add_to_disp("%"))
button.place(y = 140, x = 155)

button = ctk.CTkButton(root, text = "⌫", font = font_button, fg_color=bg_color, hover_color=bg_color, text_color=text_color, width=60, height=40, corner_radius=13, command=lambda: clear_disp_1())
button.place(y = 140, x = 90)

button = ctk.CTkButton(root, text = "7", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("7"))
button.place(y = 190, x = 25)

button = ctk.CTkButton(root, text = "8", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("8"))
button.place(y = 190, x = 90)

button = ctk.CTkButton(root, text = "9", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("9"))
button.place(y = 190, x = 155)

button = ctk.CTkButton(root, text = "4", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("4"))
button.place(y = 240, x = 25)

button = ctk.CTkButton(root, text = "5", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("5"))
button.place(y = 240, x = 90)

button = ctk.CTkButton(root, text = "6", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("6"))
button.place(y = 240, x = 155)

button = ctk.CTkButton(root, text = "1", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("1"))
button.place(y = 290, x = 25)

button = ctk.CTkButton(root, text = "2", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("2"))
button.place(y = 290, x = 90)

button = ctk.CTkButton(root, text = "3", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=60, height=40, corner_radius=13, command=lambda: add_number("3"))
button.place(y = 290, x = 155)

button = ctk.CTkButton(root, text = "0", font = font_button, fg_color = bg_color, hover_color=hover_color, text_color=text_color_2, width=125, height=40, corner_radius=13, command=lambda: add_number("0"))
button.place(y = 340, x = 25)

root.mainloop()