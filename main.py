import kivy
kivy.require('2.0.0') # Replace with your Kivy version

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleKivyApp(App):
    def build(self):
        # Create a vertical box layout to hold our widgets
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a label
        self.my_label = Label(text='Hello, Kivy on Android!', font_size='24sp')

        # Create a button
        my_button = Button(text='Click Me', font_size='24sp')

        # Bind the button's 'on_press' event to a function
        my_button.bind(on_press=self.on_button_press)

        # Add the widgets to the layout
        layout.add_widget(self.my_label)
        layout.add_widget(my_button)

        return layout

    def on_button_press(self, instance):
        # This function is called when the button is pressed
        self.my_label.text = 'Button was pressed!'

if __name__ == '__main__':
    SimpleKivyApp().run()
