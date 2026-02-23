from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Frame import AppFrame
from C2_English_App.AllClasses.App_Entry_Box import App_Entry_Box
from C2_English_App.AllClasses.Button_Standard import Button_Standard
from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.App_Label_Title import App_Label_Title

menu_page = AppWindow(title="Testowy tytuł", banner_text = "Witaj w świecie Pythona!")

frame = AppFrame(menu_page)
frame.place(x=100, y=200)

textbox = App_Entry_Box(menu_page)
textbox.place(x=300, y=400)

def run_macro():
    print(textbox.get_text())


button = Button_Standard(menu_page, command = run_macro)
button.place(x=400, y=300)


label = App_Label_Standard(frame, text="To jest mój label", width=300)
label.place(x=5, y=5)

label = App_Label_Title(menu_page, text="To jest mój title", width=300)
label.place(x=30, y=300)


menu_page.mainloop()