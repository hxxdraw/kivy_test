from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
import source.client.client_prototype as cl
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import *
from kivymd.uix.dialog import *


KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        
        MDToolbar:
            md_bg_color: app.theme_cls.bg_darkest
            title: "Select Desktop"
            right_action_items: [["dots-vertical", lambda e: print(e)]]
            
        ScrollView:
            MDGridLayout:
                id: box
                cols: 1
                adaptive_height: True

<DialogBoxContent>
    size_hint_y: None
    height: "50dp"
    spacing: "12dp"
    orientation: "vertical"
    
    MDTextField:
        password: True
        hint_text: "password"

<Content>
    size_hint: None, None
    adaptive_size: True
    height: "0dp"
    
'''


class Content(MDBoxLayout):
    '''Custom content.'''


class DialogBoxContent(MDBoxLayout):
    pass


class Test(MDApp):
    access_dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        for table in cl.TABLES.items():
            self.panel = MDExpansionPanel(
                    on_open=lambda: print(123),
                    icon=table[1]['platform'],
                    opening_time=0.05,
                    closing_time=0.05,
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=table[0],
                        secondary_text=table[1]['ip'],
                        tertiary_text=table[1]['domain'],
                    )
                )
            self.panel.bind(on_open=self.connect_dialog)
            self.root.ids.box.add_widget(self.panel)

    def connect_dialog(self, desktop_name):
        self.access_dialog = MDDialog(
            title='Desktop: "{}"'.format(desktop_name.panel_cls.text),
            type="custom",
            content_cls=DialogBoxContent(),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda e: self.access_dialog.dismiss(force=True)
                ),
                MDFlatButton(
                    text="CONNECT"
                )
            ]
        )
        self.access_dialog.open()


Test().run()