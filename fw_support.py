import pystray
import fw
import database
from win32con import *
from win32gui import LoadCursor, GetCursorInfo, SetCursor
import collocation
from dialogs import *
import rapidtranslate
from PIL import Image
from pystray import MenuItem as item

def main(*args):
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , to_tray)
    global _top1, mainWindow
    _top1 = root
    db = database.Database()
    mainWindow = fw.ToplevelWin(root, db)
    mainWindow.root.attributes('-topmost', 1)
    mainWindow.Label1.configure(text=f"{mainWindow.db.get_word()}")
    mainWindow.root.attributes('-topmost', 0)
    root.mainloop()

def next_word(*args):
    mainWindow.Label1.configure(text=f"{mainWindow.db.get_word()}")
    mainWindow.Label2.configure(text=f"")
    mainWindow.HtmlText.set_html("<html></html>")

def translate(*args):
    original_text = mainWindow.Label1.cget("text")
    current_cursor_handle = GetCursorInfo()[1]
    wait_cursor_handle = LoadCursor(0, IDC_WAIT)
    SetCursor(wait_cursor_handle)
    rapid_key = mainWindow.db.get_parameter('rapid_key')
    translated_text = rapidtranslate.rapid_translate(original_text,rapid_key)
    mainWindow.HtmlText.set_html(collocation.get_callocation(original_text))
    SetCursor(current_cursor_handle)
    mainWindow.Label2.configure(text=f"{translated_text}")

def delete_word(*args):
    dialog = YesNoDialog(mainWindow,mainWindow.db.delete_word, mainWindow.Label1.cget("text"))
    dialog.show()
    if dialog.deleted:
        next_word()

def add_word(*args):
    dialog = EditDialog(mainWindow)
    dialog.show()
    if dialog.processed:
        mainWindow.db.add_word(dialog.new_word)
        mainWindow.Label1.configure(text=f"{dialog.new_word}")
        mainWindow.Label2.configure(text=f"")
        mainWindow.HtmlText.set_html("<html></html>")

def update_word(*args):
    dialog = EditDialog(mainWindow, mainWindow.Label1.cget("text"))
    dialog.show()
    if dialog.processed:
        mainWindow.db.update_word(dialog.word, dialog.new_word)
        mainWindow.Label1.configure(text=f"{dialog.new_word}")
        mainWindow.Label2.configure(text=f"")
        mainWindow.HtmlText.set_html("<html></html>")

def set_rapid_key(*args):
    dialog = EditDialog(mainWindow, f"{mainWindow.db.get_parameter('rapid_key')}")
    dialog.show(True)
    if dialog.processed:
        mainWindow.db.set_parameter('rapid_key',f"{dialog.new_word.replace(' ','')}")


def quit_application(icon, item):
    icon.stop()
    mainWindow.root.destroy()

def show_application(icon, item):
    icon.stop()
    mainWindow.root.attributes('-topmost', 1)
    mainWindow.root.deiconify()
    mainWindow.root.attributes('-topmost', 0)
    mainWindow.ButtonNext.focus_set()

def to_tray(*args):
    mainWindow.root.withdraw()
    image = Image.open(f"fw.ico")
    menu = (item('Foreign Words', show_application, default=True), item('Close', quit_application))
    icon = pystray.Icon("Foreign Words",image,"Foreign Words",menu)
    icon.run()

if __name__ == '__main__':
    fw.start_up()