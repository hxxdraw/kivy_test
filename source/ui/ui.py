from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from source.ui import custom
from kivymd.uix.button import *
from kivymd.uix.boxlayout import *
import source.client.client_prototype as cl
from kivymd.uix.card import *
from kivymd.uix.label import *
from kivymd.uix.screen import MDScreen

KV = """
<DialogBoxContent>
    size_hint_y: None
    height: "50dp"
    spacing: "12dp"
    orientation: "vertical"
    
    MDTextField:
        password: True
        hint_text: "password"

MDFlatButton:
    text: "Connect"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    on_release: app.login_dialog(self.text)

"""


class DialogBoxContent(MDBoxLayout):
    pass


class Application(MDApp):
    access_dialog = None

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        pass

    def login_dialog(self, desktop_name):
        if not self.access_dialog:
            self.access_dialog = MDDialog(
                title=custom.AccessDialog.title.format(desktop_name),
                type="custom",
                content_cls=DialogBoxContent(),
                buttons=[
                    MDFlatButton(
                        **custom.AccessDialog.CANCEL_BUTTON, on_release=lambda e: self.access_dialog.dismiss(force=True)
                    ),
                    MDFlatButton(
                        **custom.AccessDialog.OK_BUTTON
                    )
                ]
            )
        self.access_dialog.open()


class Tab(MDFloatLayout, MDTabsBase):
    pass


if __name__ == "__main__":
    Application().run()

