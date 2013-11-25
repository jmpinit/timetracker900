import time
import datetime

import gtk
from gtk import Window, Button, Widget

if __name__ == "__main__":
    def same_cb(widget, event):
        gtk.main_quit()

    def project_cb(widget, event):
        gtk.main_quit()

    def study_cb(widget, event):
        gtk.main_quit()

    def life_cb(widget, event):
        gtk.main_quit()

    def other_cb(widget, event):
        gtk.main_quit()

    window = Window(gtk.WINDOW_TOPLEVEL)
    window.connect("destroy", gtk.main_quit)

    box = gtk.VBox(False, 0)

    stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    btn_same = Button("SAME")
    btn_same.connect_object("button_press_event", same_cb, window)
    box.pack_start(btn_same, True, True, 0)

    btn_project = Button("project")
    btn_project.connect_object("button_press_event", project_cb, window)
    box.pack_start(btn_project, True, True, 0)

    btn_study = Button("study")
    btn_study.connect_object("button_press_event", study_cb, window)
    box.pack_start(btn_study, True, True, 0)

    btn_life = Button("life")
    btn_life.connect_object("button_press_event", life_cb, window)
    box.pack_start(btn_life, True, True, 0)

    btn_other = Button("other")
    btn_other.connect_object("button_press_event", other_cb, window)
    box.pack_start(btn_other, True, True, 0)

    window.add(box)
    window.show_all()

    gtk.main()

