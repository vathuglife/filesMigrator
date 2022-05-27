from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
import mysql.connector
from kivy.core.window import Window 
Window.size =(350,600)


class Tab1(MDFloatLayout, MDTabsBase):
    def product_lists(self, *args):
        database = mysql.connector.connect(host="localhost" , user ="root" , password= "dumbre1902", database="localvendor")
        cursor = database.cursor()
        sql_select_Query = "select * from addproduct"
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        layout = AnchorLayout()
        self.product_table = MDDataTable(
            pos_hint={'center_y': 0.41, 'center_x': 0.5},
            size_hint=(0.9, 0.78),
            elevation= 15,
            rows_num = 100,
            column_data=[
                ("Product Name", dp(25)),
                ("MRP", dp(15)),
                ("Quantity", dp(20)),
                ("Product Description", dp(30)),
                ],
                row_data=[
                        (f"{row[0]}", f"{row[1]}", f"{row[2]}", f"{row[3]}") for row in records
                ],
            )

        self.add_widget(self.product_table)
        return layout

    def on_enter(self):
        self.product_lists()

class Tab2(MDFloatLayout, MDTabsBase):
    pass

class DemoApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("testwidgets.kv"))
        return sm



DemoApp().run()