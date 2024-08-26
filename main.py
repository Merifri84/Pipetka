from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')


class MyNewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lb = Label(text='Color', pos=(20, 50))
        btn1 = Button(text='', pos=(200, 100), background_color=[1, 0, 0, 1], background_normal='', on_press=self.redBtnPress)
        btn2 = Button(text='', pos=(150, 150), background_color=[0.23, 0.69, 0.44, 1], background_normal='', on_press=self.greenBtnPress)
        btn3 = Button(text='', pos=(100, 250), background_color=[1, 0.64, 0, 1], background_normal='', on_press=self.yellowBtnPress)
        btn4 = Button(text='', pos=(50, 30), on_press=self.grayBtnPress)
        layout.add_widget(self.lb)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

    def redBtnPress(self, instance):
        instance.text = "255, 0, 0"
        self.lb.text = "Red"

    def greenBtnPress(self, instance):
        instance.text = "60, 179, 113"
        self.lb.text = "Green"

    def yellowBtnPress(self, instance):
        instance.text = "255, 165, 0"
        self.lb.text = "Yellow"

    def grayBtnPress(self, instance):
        instance.text = "Random"
        self.lb.text = "Gray"


if __name__ == "__main__":
    MyNewApp().run()
