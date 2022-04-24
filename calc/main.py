from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.mess1 = "Mayushi is more intelligent than you."
        self.mess2 = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            elif current == self.mess1:
                self.solution.text = button_text
            elif current == self.mess2:
                self.solution.text = button_text
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            for i in self.operators:
                if i in self.solution.text:
                    split0 = self.solution.text.split(i)
                    s = []
                    for j in split0:
                        try:
                            while j[0] == "0":
                                j = j[1:]
                        except IndexError:
                            j="0"
                        s.append(j)
                    k = i.join(s)
                    self.solution.text = k
            try:
                self.ans = str(eval(self.solution.text))
                self.solution.text = self.ans
            except ZeroDivisionError:
                self.solution.font_size = 40
                self.solution.text = self.mess1
            except SyntaxError:
                for i in self.operators:
                    if i in self.solution.text:
                        split0 = self.solution.text.split(i)
                        if split0[-1] == "":
                            self.solution.font_size = 40
                            if i == "/":
                                self.mess2 = "By what I should divide?"
                                self.solution.text = self.mess2
                            elif i == "*":
                                self.mess2 = "With what I should multiply?"
                                self.solution.text = self.mess2
                            elif i == "+":
                                self.mess2 = "What should I add?"
                                self.solution.text = self.mess2
                            elif i == "-":
                                self.mess2 = "What should I subtract?"
                                self.solution.text = self.mess2
                    else:
                        pass


if __name__ == '__main__':
    app = MainApp()
    app.run()
