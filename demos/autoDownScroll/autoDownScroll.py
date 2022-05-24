from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
<MessageView>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<Message>:
    canvas:
        Color:
            rgba: 0, 1, 0, 0.3
        Rectangle:
            pos: self.pos
            size: self.size
''')

class Message(Widget):
    pass

class MessageView(ScrollView):
    pass

class TestApp(App):
    def msg_in(self, btn):
        msg = Message()
        msg.size_hint = [None, None]
        self.msg_layout.add_widget(msg)
        self.sv1_main.scroll_to(msg)

    def build(self):
        self.scr = Screen()
        self.sv1_main = MessageView(pos_hint={"top": 0.87, "center_x": 0.5},
                                    size_hint=(0.97, 0.65))
        self.msg_layout = GridLayout(cols=1,
                                     size_hint_y=None)
        self.msg_layout.bind(minimum_height=self.msg_layout.setter('height'))
        self.bt1_main = Button(size_hint=(0.1, 0.078),
                               pos_hint={"top": 0.097, "center_x": 0.927},
                               on_press=self.msg_in)
        self.scr.add_widget(self.sv1_main)
        self.sv1_main.add_widget(self.msg_layout)
        self.scr.add_widget(self.bt1_main)
        return self.scr

TestApp().run()