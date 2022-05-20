from kivy.config import Config

Config.set('graphics', 'multisamples', '0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

kv = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import Clock kivy.clock.Clock

ScreenManager:
    MainScreen:
    ShowData:    

<DataSwitch>

    Button:
        text: 'Data 1'
        on_press: root.show_data1()
        on_press: app.root.current = 'ShowData'
    Button:
        text: 'Data 2'
        on_press: root.show_data2()
        on_press: app.root.current = 'ShowData'

<Row>:
    TextInput:
        id: text_input
        size_hint_y: None
        height: 30

<Rows>:   
    orientation: 'vertical'

<MainScreen>:
    name: 'MainScreen'
    DataSwitch:

<ShowData>:
    name: 'ShowData'
    on_pre_enter:
        Clock.schedule_once(self.ids.rows.fill_with_data, 0.1)
    Rows:
        id: rows
    Button:
        text: 'Go back'
        size_hint_y: None
        height: 20
        on_press: app.root.current = 'MainScreen'

"""


class Row(BoxLayout):

    def __init__(self, text, **kwargs):
        super(Row, self).__init__(**kwargs)
        self.ids.text_input.text = text


class Rows(BoxLayout):
    data = []

    def fill_with_data(self, dt):
        for item in self.data:
            row = Row(text=str(item))
            self.add_widget(row)


class MainScreen(Screen):
    pass


class DataSwitch(BoxLayout):
    data1 = ['1', '2', '3', '4']
    data2 = ['5', '6', '7', '8']

    def show_data1(self):
        App.get_running_app().root.get_screen('ShowData').ids.rows.data = self.data1

    def show_data2(self):
        App.get_running_app().root.get_screen('ShowData').ids.rows.data = self.data2


class ShowData(Screen):
    def on_pre_leave(self):
        self.ids.rows.clear_widgets()


sm = Builder.load_string(kv)


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()