import gtk
from gtk import Window, Button, Widget

if __name__ == "__main__":
    window = Window(gtk.WINDOW_TOPLEVEL)
    window.connect("destroy", gtk.main_quit)
    button = Button("Hello World")
    button.connect_object("clicked", Widget.destroy, window)
    window.add(button)
    window.show_all()
    gtk.main()
