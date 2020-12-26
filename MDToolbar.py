## A simple toolBar Can be as folows


kv = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "MDToolbar"
            left_action_items: [["menu", lambda x: app.callback()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()]]
        Widget:

"""