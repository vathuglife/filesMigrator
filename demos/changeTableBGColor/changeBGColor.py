from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

Builder.load_string("""
<-MDDataTable>:
    background_color: 1, 1, 1, 1  # added for this example
    MDCard:
        id: container
        orientation: "vertical"
        elevation: root.elevation
        padding: "24dp", "24dp", "8dp", "8dp"
        # canvas added for this change
        canvas:
            Color:
                rgba: root.background_color
            Rectangle:
                size: self.size
                pos: self.pos
""")

class Example(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            background_color=(102/255,51/255,153/255,1),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("[color=#52251B]Column 2[/color]", dp(30)),
                ("Column 3", dp(30)),
                ("[size=24][color=#C042B8]Column 4[/color][/size]", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (
                    f"{i + 1}",
                    "[color=#297B50]1[/color]",
                    "[color=#C552A1]2[/color]",
                    "[color=#6C9331]3[/color]",
                    "4",
                    "5",
                )
                for i in range(50)
            ],
        )
        layout.add_widget(data_tables)
        return layout


Example().run()