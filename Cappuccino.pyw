import tkinter.messagebox
import tkinter.filedialog
import os
import customtkinter as ck
import tkinter

boot = ck.CTk()
boot.geometry("400x500")
boot.title("Cappuccino(v1.1.0)")
boot.resizable(False, False)
boot.iconbitmap('C:\\Program Files (x86)\\Cappuccino\\icon.ico')

def create_func():
    vn = variable_name_txt.get()
    tt = title_txt.get()
    ft = font_txt.get()
    x = x_scale_txt.get()
    y = y_scale_txt.get()
    lc = location_txt.get()
    print(lc)
    tk_file_path = f'{lc}\{tt}'

    file_content = f'''
import customtkinter as ck

{vn} = ck.CTk()
{vn}.geometry("{x}x{y}")
{vn}.title("{tt}")
app_font = "{ft}"
app_font_size = 20
pad_x = 10
pad_y = 10
label = ck.CTkLabel({vn}, text="Hello world!", font=(app_font, app_font_size))
label.pack(padx=pad_x, pady=pad_y)
    
{vn}.mainloop()

'''
    if x == 'X value' or y == 'Y value':
        tkinter.messagebox.showerror(title='Error', message='X scale and y scale should be integer.')
    elif tt == '' or tt.isspace():
        tkinter.messagebox.showerror(title='Error', message='Title is required for file generation.')
    elif vn == '' or vn.isspace() or vn.isnumeric():
        tkinter.messagebox.showerror(title='Error', message='variable name should be a string.')
    elif lc == '' or lc.isspace():
        tkinter.messagebox.showerror(title='Error', message='Location is inappropriate.')
    elif os.path.exists(location_txt.get() + f'{title_txt.get()}.py') or os.path.exists(
            location_txt.get() + f'{title_txt.get()}.pyw'):
        tkinter.messagebox.showerror(title='Error',
                                     message='This file already exists. Please rename your file name')
    else:
        print(type(r.get()))
        if r.get() == '1':
            with open(f'{tk_file_path}.py', 'w') as file:
                file.write(file_content)
            file.close()
            tkinter.messagebox.showinfo(title='Info', message=f"File '{tt}' has been created successfully.")
        elif r.get() == '2':
            with open(f'{tk_file_path}.pyw', 'w') as file:
                file.write(file_content)
            file.close()
            tkinter.messagebox.showinfo(title='Info', message=f"File '{tt}' has been created successfully.")
        else:
            tkinter.messagebox.showerror(title='Error',
                                         message='Please select extension for this file.')


def browse_func():
    file_path = tkinter.filedialog.askdirectory()
    location_txt.delete(0, tkinter.END)
    location_txt.insert(0, file_path)


app_font = "Square721 BT Roman"
app_font_size = 18
border_color = "white"
x_axis = 20
y_axis = 20
entry_width = 350
# ------------------------------------------------------------------------------
top_frame = ck.CTkFrame(boot)

# -------------------------------------------------------------------------------
title_txt = ck.CTkEntry(top_frame,
                        width=entry_width,
                        font=(app_font, app_font_size),
                        corner_radius=2,
                        placeholder_text="Title",
                        border_color=border_color,
                        border_width=1)

variable_name_txt = ck.CTkEntry(top_frame,
                                width=entry_width,
                                font=(app_font, app_font_size),
                                corner_radius=2,
                                placeholder_text="Variable name",
                                border_color=border_color,
                                border_width=1)

# ----------------------------------------------------------------------------
scale_lbl = ck.CTkLabel(top_frame,
                        text="Scale",
                        font=(app_font, app_font_size))

scale_values = ['100', '200', '300', '400', '500', '600', '700']
x_scale_txt = ck.CTkComboBox(top_frame,
                             width=130,
                             font=(app_font, app_font_size),
                             corner_radius=2,
                             values=scale_values,
                             dropdown_font=(app_font, app_font_size),
                             state='readonly',
                             border_width=1)

x_scale_txt.set('X value')
separator_lbl = ck.CTkLabel(top_frame,
                            text=':',
                            font=(app_font, app_font_size, 'bold'))

y_scale_txt = ck.CTkComboBox(top_frame,
                             width=130,
                             font=(app_font, app_font_size),
                             corner_radius=2,
                             values=scale_values,
                             dropdown_font=(app_font, app_font_size),
                             state='readonly',
                             border_width=1)

y_scale_txt.set('Y value')
# ---------------------------------------------------------------------------
title_txt.pack(padx=20, pady=10)
variable_name_txt.pack(padx=20)
scale_lbl.pack(side='left', padx=20, pady=20)
x_scale_txt.pack(side='left')
separator_lbl.pack(side='left', padx=10)
y_scale_txt.pack(side='left')

top_frame.pack(expand=True, fill='both', padx=5, pady=5)

# ---------------------------------------------------------------------------
bottom_frame = ck.CTkFrame(boot)
# ---------------------------------------------------------------------------
r = ck.StringVar()

console_radio = ck.CTkRadioButton(bottom_frame,
                                  text="Console",
                                  variable=r,
                                  value=1,
                                  fg_color="white",
                                  hover_color="grey",
                                  font=(app_font, app_font_size))

no_console_radio = ck.CTkRadioButton(bottom_frame,
                                     text="no Console",
                                     variable=r,
                                     value=2,
                                     fg_color="white",
                                     hover_color="grey",
                                     font=(app_font, app_font_size))

# ------------------------------------------------------------------------------

fonts = ['Arial', 'SF Pro', 'Tahoma', 'Consoles', 'Courier New', 'JetBrains Mono', 'Square721 BT Roman']
font_txt = ck.CTkComboBox(bottom_frame,
                          width=350,
                          values=fonts,
                          corner_radius=2,
                          font=(app_font, app_font_size),
                          dropdown_font=(app_font, app_font_size),
                          state='readonly',
                          border_width=1)
font_txt.set("Select font")
# ---------------------------------------------------------------------------

location_txt = ck.CTkEntry(bottom_frame,
                           width=350,
                           font=(app_font, app_font_size),
                           text_color='grey',
                           corner_radius=2)

location_txt.insert(0, 'C:\\Users\\Arnold\\')

browse_btn = ck.CTkButton(bottom_frame,
                          text='Browse',
                          text_color="black",
                          font=(app_font, app_font_size - 3),
                          corner_radius=2,
                          command=browse_func,
                          fg_color="white")

# -----------------------------------------------------------------------

create_btn = ck.CTkButton(boot,
                          text='CREATE',
                          text_color="black",
                          height=10,
                          font=(app_font, app_font_size),
                          corner_radius=2,
                          command=create_func,
                          fg_color="white")
# -----------------------------------------------------------------------

console_radio.pack(anchor='w', padx=20, pady=10)
no_console_radio.pack(anchor='w', padx=20)
font_txt.pack(pady=25)
location_txt.pack()
browse_btn.pack(anchor='w',padx=20, pady=10)
bottom_frame.pack(expand=True, fill='both', padx=5, pady=5)

create_btn.pack(anchor='e', pady=20, padx=20)

boot.mainloop()
