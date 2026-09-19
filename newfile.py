from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
import math


# ---------- HOME SCREEN ----------
class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.08, 0.12, 0.20, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[0]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="MATHEMATICS APP",
            font_size=32,
            bold=True,
            size_hint_y=0.3
        )
        layout.add_widget(title)

        subtitle = Label(
            text="Smart Mathematics Calculator",
            font_size=18,
            size_hint_y=0.2
        )
        layout.add_widget(subtitle)

        start = Button(
            text="START",
            font_size=24,
            size_hint_y=0.2,
            background_normal="",
            background_color=(0.15, 0.55, 0.85, 1)
        )
        start.bind(on_press=self.open_calculator)
        layout.add_widget(start)

        about = Button(
            text="ABOUT",
            font_size=22,
            size_hint_y=0.2,
            background_normal="",
            background_color=(0.25, 0.35, 0.50, 1)
        )
        about.bind(on_press=self.open_about)
        layout.add_widget(about)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def open_calculator(self, instance):
        self.manager.current = "calculator"

    def open_about(self, instance):
        self.manager.current = "about"


# ---------- CALCULATOR SCREEN ----------
class CalculatorScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.95, 0.95, 0.97, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        main = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=10
        )

        title = Label(
            text="SMART MATHEMATICS CALCULATOR",
            font_size=25,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint_y=0.12
        )
        main.add_widget(title)

        self.num1 = TextInput(
            hint_text="Enter first number",
            input_filter="float",
            multiline=False,
            font_size=20,
            size_hint_y=0.13
        )
        main.add_widget(self.num1)

        self.num2 = TextInput(
            hint_text="Enter second number",
            input_filter="float",
            multiline=False,
            font_size=20,
            size_hint_y=0.13
        )
        main.add_widget(self.num2)

        # ---------- RESULT ----------
        self.result = Label(
            text="Result will appear here",
            font_size=22,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint_y=0.15
        )
        main.add_widget(self.result)

        # ---------- ROW 1 ----------
        row1 = BoxLayout(
            spacing=8,
            size_hint_y=0.13
        )

        add_btn = Button(
            text="+",
            font_size=25,
            background_normal="",
            background_color=(0.15, 0.55, 0.85, 1)
        )
        add_btn.bind(on_press=self.addition)
        row1.add_widget(add_btn)

        sub_btn = Button(
            text="-",
            font_size=25,
            background_normal="",
            background_color=(0.85, 0.45, 0.20, 1)
        )
        sub_btn.bind(on_press=self.subtraction)
        row1.add_widget(sub_btn)

        mul_btn = Button(
            text="×",
            font_size=25,
            background_normal="",
            background_color=(0.25, 0.65, 0.35, 1)
        )
        mul_btn.bind(on_press=self.multiplication)
        row1.add_widget(mul_btn)

        div_btn = Button(
            text="÷",
            font_size=25,
            background_normal="",
            background_color=(0.65, 0.35, 0.75, 1)
        )
        div_btn.bind(on_press=self.division)
        row1.add_widget(div_btn)

        main.add_widget(row1)

        # ---------- ROW 2 ----------
        row2 = BoxLayout(
            spacing=8,
            size_hint_y=0.13
        )

        percent_btn = Button(
            text="%",
            font_size=23,
            background_normal="",
            background_color=(0.20, 0.55, 0.65, 1)
        )
        percent_btn.bind(on_press=self.percentage)
        row2.add_widget(percent_btn)

        square_btn = Button(
            text="x²",
            font_size=23,
            background_normal="",
            background_color=(0.75, 0.50, 0.20, 1)
        )
        square_btn.bind(on_press=self.square)
        row2.add_widget(square_btn)

        sqrt_btn = Button(
            text="√x",
            font_size=23,
            background_normal="",
            background_color=(0.40, 0.50, 0.75, 1)
        )
        sqrt_btn.bind(on_press=self.square_root)
        row2.add_widget(sqrt_btn)

        main.add_widget(row2)

        # ---------- BACK ----------
        back_btn = Button(
            text="BACK",
            font_size=20,
            size_hint_y=0.11,
            background_normal="",
            background_color=(0.30, 0.30, 0.35, 1)
        )
        back_btn.bind(on_press=self.go_back)
        main.add_widget(back_btn)

        self.add_widget(main)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    # ---------- GET NUMBERS ----------
    def get_numbers(self):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)
            return a, b

        except:
            self.result.text = "Please enter valid numbers."
            return None, None

    # ---------- ADDITION ----------
    def addition(self, instance):
        a, b = self.get_numbers()

        if a is not None:
            self.result.text = "Result: " + str(a + b)

    # ---------- SUBTRACTION ----------
    def subtraction(self, instance):
        a, b = self.get_numbers()

        if a is not None:
            self.result.text = "Result: " + str(a - b)

    # ---------- MULTIPLICATION ----------
    def multiplication(self, instance):
        a, b = self.get_numbers()

        if a is not None:
            self.result.text = "Result: " + str(a * b)

    # ---------- DIVISION ----------
    def division(self, instance):
        a, b = self.get_numbers()

        if a is not None:

            if b == 0:
                self.result.text = "Cannot divide by zero."

            else:
                self.result.text = "Result: " + str(a / b)

    # ---------- PERCENTAGE ----------
    def percentage(self, instance):
        a, b = self.get_numbers()

        if a is not None:
            self.result.text = "Result: " + str((a * b) / 100)

    # ---------- SQUARE ----------
    def square(self, instance):

        try:

            if self.num1.text.strip():
                number = float(self.num1.text)
                self.result.text = "Square: " + str(number * number)

            elif self.num2.text.strip():
                number = float(self.num2.text)
                self.result.text = "Square: " + str(number * number)

            else:
                self.result.text = "Please enter a number."

        except:
            self.result.text = "Please enter a valid number."

    # ---------- SQUARE ROOT ----------
    def square_root(self, instance):

        try:

            if self.num1.text.strip():
                number = float(self.num1.text)

            elif self.num2.text.strip():
                number = float(self.num2.text)

            else:
                self.result.text = "Please enter a number."
                return

            if number < 0:
                self.result.text = "No real root"

            else:
                self.result.text = "Square Root: " + str(
                    math.sqrt(number)
                )

        except:
            self.result.text = "Please enter a valid number."

    # ---------- BACK ----------
    def go_back(self, instance):
        self.manager.current = "home"


# ---------- ABOUT SCREEN ----------
class AboutScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.08, 0.12, 0.20, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        title = Label(
            text="ABOUT",
            font_size=30,
            bold=True,
            size_hint_y=0.15
        )
        layout.add_widget(title)

        info = Label(
            text=(
                "MATHEMATICS CALCULATOR\n\n"

                "Operations:\n"
                "• Addition\n"
                "• Subtraction\n"
                "• Multiplication\n"
                "• Division\n"
                "• Percentage\n"
                "• Square\n"
                "• Square Root\n\n"

                "Important Features:\n"
                "• Easy to use\n"
                "• Handles negative numbers\n"
                "• Prevents division by zero\n"
                "• Shows no real root for negative numbers\n\n"

                "Developed by students of class VII\n"
                "Supervised by: Sir Afaq Ali Jiskani"
            ),
            font_size=16
        )

        layout.add_widget(info)

        back = Button(
            text="BACK",
            font_size=20,
            size_hint_y=0.12,
            background_normal="",
            background_color=(0.30, 0.30, 0.35, 1)
        )

        back.bind(on_press=self.go_back)

        layout.add_widget(back)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def go_back(self, instance):
        self.manager.current = "home"


# ---------- MAIN APP ----------
class MathematicsApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(
            HomeScreen(name="home")
        )

        sm.add_widget(
            CalculatorScreen(name="calculator")
        )

        sm.add_widget(
            AboutScreen(name="about")
        )

        return sm


# ---------- RUN APP ----------
if __name__ == "__main__":
    MathematicsApp().run()