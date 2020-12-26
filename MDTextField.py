## We want to take inputs from the user,process it and Display the results

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Basic Authentication App'
        font_style: 'H2'
        pos_hint: {'center_x': 0.6, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Enter you password'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True

    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.auth()

    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 1.0, 'center_y': 0.2}
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)
    def auth(self):
        if self.root.in_class.text == 'root':
            label1 = self.root.ids.show
            label1.text = "success"
        else:
            label1 =self.root.ids.show
            label1.text ='fail'

Main().run()