from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle


# ==========================================
# Desktop Window Settings
# ==========================================

Window.clearcolor = (0.055, 0.055, 0.07, 1)


# ==========================================
# Calculator Application
# ==========================================

class CalculatorApp(App):

    def build(self):

        self.title = "Modern Calculator"

        # Main layout
        main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(12)
        )

        # ==================================
        # Display
        # ==================================

        self.display = Label(
            text="0",
            font_size="38sp",
            color=(1, 1, 1, 1),
            halign="right",
            valign="middle",
            size_hint_y=0.25
        )

        self.display.bind(
            size=self.update_text_size
        )

        # Rounded display background
        with self.display.canvas.before:
            Color(0.12, 0.12, 0.15, 1)

            self.display_background = RoundedRectangle(
                pos=self.display.pos,
                size=self.display.size,
                radius=[dp(18)]
            )

        self.display.bind(
            pos=self.update_background,
            size=self.update_background
        )

        main_layout.add_widget(self.display)

        # ==================================
        # Button Grid
        # ==================================

        button_grid = GridLayout(
            cols=4,
            spacing=dp(8),
            size_hint_y=0.75
        )

        # Button information
        buttons = [

            ("C", "clear"),
            ("⌫", "back"),
            ("÷", "/"),
            ("×", "*"),

            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("-", "-"),

            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("+", "+"),

            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("=", "="),

            ("0", "0"),
            (".", "."),
            ("(", "("),
            (")", ")")
        ]

        # ==================================
        # Create Buttons
        # ==================================

        for button_text, button_value in buttons:

            button = Button(
                text=button_text,
                font_size="22sp",
                color=(1, 1, 1, 1),
                background_normal="",
                background_color=self.get_button_color(
                    button_text
                )
            )

            button.bind(
                on_press=lambda instance,
                value=button_value:
                self.button_pressed(value)
            )

            button_grid.add_widget(button)

        main_layout.add_widget(button_grid)

        return main_layout

    # ==========================================
    # Button Colors
    # ==========================================

    def get_button_color(self, text):

        # Equal button
        if text == "=":
            return (0.15, 0.75, 0.35, 1)

        # Operator buttons
        if text in ["+", "-", "×", "÷"]:
            return (1.0, 0.55, 0.05, 1)

        # Clear and backspace
        if text in ["C", "⌫"]:
            return (0.45, 0.45, 0.48, 1)

        # Number buttons
        return (0.17, 0.17, 0.20, 1)

    # ==========================================
    # Button Press
    # ==========================================

    def button_pressed(self, value):

        # Clear
        if value == "clear":

            self.display.text = "0"

        # Backspace
        elif value == "back":

            current_text = self.display.text

            if len(current_text) <= 1:
                self.display.text = "0"

            else:
                self.display.text = current_text[:-1]

        # Calculate
        elif value == "=":

            self.calculate()

        # Numbers / Operators
        else:

            if self.display.text == "0":

                self.display.text = value

            else:

                self.display.text += value

    # ==========================================
    # Calculate Result
    # ==========================================

    def calculate(self):

        try:

            expression = self.display.text

            result = eval(expression)

            # Remove unnecessary .0
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)

            self.display.text = str(result)

        except ZeroDivisionError:

            self.display.text = "Cannot divide by 0"

        except:

            self.display.text = "Error"

    # ==========================================
    # Display Text Size
    # ==========================================

    def update_text_size(self, instance, value):

        instance.text_size = value

    # ==========================================
    # Display Background
    # ==========================================

    def update_background(self, instance, value):

        self.display_background.pos = instance.pos
        self.display_background.size = instance.size


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    CalculatorApp().run()
