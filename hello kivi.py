#!/user/bin/python
#  -*-coding: utf-8-*-
# from kivy.app import App
# from kivy.uix.button import Button
# class TestApp(App):
#     def build(self):
#         return Button(text="hello,kivy")
# TestApp().run()


# from kivy.app import App
# from kivy.uix.button import Button
# class TestApp(App):
#     def build(self):
#         return Button(text='hello kivy',background_color=(0,1,1,1),font_size=150)
# if __name__=="__main__":
#     TestApp().run()



from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
class TestApp(App):
    def build(self):
        s = Scatter()
        l = Label(text="hell0 kivy",font_siza=150)
        s.add_widget(l)
        return s
if __name__=="__main__":
    TestApp().run()