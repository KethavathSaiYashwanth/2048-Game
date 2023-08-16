import random
from kivy.app import App
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class BoxLayoutExample(BoxLayout):
    pass


class GridLayoutExample(GridLayout):
    high_score = NumericProperty(0)
    c = 0
    j = 0
    k = []
    h = NumericProperty(10)
    score = NumericProperty(0)
    background_color_numbers = ListProperty(["peachpuff"] * 16)
    title1 = StringProperty("2048")
    title2 = StringProperty("")
    slider_value_text = StringProperty("10")
    not_start_game = BooleanProperty(True)
    game_over_or_not_start_game = BooleanProperty(True)
    my_bool = False
    my_bool_a = False
    my_bool_b = False
    you_win = BooleanProperty(False)
    game_over = BooleanProperty(False)
    text_score = StringProperty("0")
    text_high_score = StringProperty("0")
    text_a = StringProperty("START GAME")
    my_text = ListProperty([""] * 16)
    my_num = ListProperty([0] * 16)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.on_l_click()
        elif keycode[1] == 'right':
            self.on_r_click()
        elif keycode[1] == 'up':
            self.on_u_click()
        elif keycode[1] == 'down':
            self.on_d_click()
        elif keycode[1] == 'enter':
            self.new_game()
        return True

    def win(self):
        for u in range(0, 16):
            if self.my_num[u] == 2048:
                self.you_win = True
                self.title1 = "YOU"
                self.title2 = "WIN"
                break

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.text_high_score = str(self.high_score)

    def update_color(self):
        for t in range(0, 16):
            if self.my_num[t] == 0:
                self.background_color_numbers[t] = "peachpuff"
            if self.my_num[t] == 2:
                self.background_color_numbers[t] = "khaki"
            if self.my_num[t] == 4:
                self.background_color_numbers[t] = "plum"
            if self.my_num[t] == 8:
                self.background_color_numbers[t] = "palevioletred"
            if self.my_num[t] == 16:
                self.background_color_numbers[t] = "darkseagreen"
            if self.my_num[t] == 32:
                self.background_color_numbers[t] = "indianred"
            if self.my_num[t] == 64:
                self.background_color_numbers[t] = "mediumslateblue"
            if self.my_num[t] == 128:
                self.background_color_numbers[t] = "steelblue"
            if self.my_num[t] == 256:
                self.background_color_numbers[t] = "saddlebrown"
            if self.my_num[t] == 512:
                self.background_color_numbers[t] = "silver"
            if self.my_num[t] == 1024:
                self.background_color_numbers[t] = "rosybrown"
            if self.my_num[t] == 2048:
                self.background_color_numbers[t] = "gold"

    def check_game_over(self):
        for p in range(0, 16):
            if not self.my_num[p]:
                self.my_bool = True
                break
        if not self.my_bool:
            for q in [0, 4, 8, 12]:
                if self.my_num[q] == self.my_num[q + 1] or self.my_num[q + 1] == self.my_num[q + 2]:
                    self.my_bool_a = True
                    break
                if self.my_num[q + 2] == self.my_num[q + 3]:
                    self.my_bool_a = True
                    break
            for s in [0, 1, 2, 3]:
                if self.my_num[s] == self.my_num[s + 4] or self.my_num[s + 4] == self.my_num[s + 8]:
                    self.my_bool_b = True
                    break
                if self.my_num[s + 8] == self.my_num[s + 12]:
                    self.my_bool_b = True
                    break
        if not self.my_bool and not self.my_bool_a and not self.my_bool_b:
            self.game_over = True
            self.game_over_or_not_start_game = True
            self.title1 = "GAME"
            self.title2 = "OVER"
            self.text_a = "TRY AGAIN"
        self.my_bool = False
        self.my_bool_a = False
        self.my_bool_b = False

    def on_slider_value(self, widget):
        self.slider_value_text = str(int(widget.value))
        self.h = int(widget.value)

    def new_game(self):
        self.game_over_or_not_start_game = False
        self.not_start_game = False
        self.title1 = "2048"
        self.title2 = ""
        self.you_win = False
        self.update_high_score()
        self.score = 0
        self.update_score()
        self.game_over = False
        self.text_a = "NEW GAME"
        self.my_num = []
        for i in range(0, 16):
            self.my_num.append(0)
        a = random.randint(0, 15)
        while True:
            b = random.randint(0, 15)
            if b != a:
                break
        u = random.randint(1, self.h)
        if u == 1:
            self.my_num[a] = 4
        else:
            self.my_num[a] = 2
        v = random.randint(1, self.h)
        if v == 1:
            self.my_num[b] = 4
        else:
            self.my_num[b] = 2
        self.update_text()
        self.update_color()

    def update_text(self):
        my_num_new = []
        for each in self.my_num:
            if not each:
                my_num_new.append("")
            else:
                my_num_new.append(str(each))
        self.my_text = my_num_new

    def new_number(self):
        while True:
            x = random.randint(0, 15)
            if not self.my_num[x]:
                break
        y = random.randint(1, self.h)
        if y == 1:
            self.my_num[x] = 4
        else:
            self.my_num[x] = 2

    def update_score(self):
        self.text_score = str(self.score)

    def on_r_click(self):
        if not self.not_start_game:
            self.c = 0
            for i in [2, 6, 10, 14]:
                if self.my_num[self.j - 2] and self.my_num[self.j]:
                    if self.my_num[self.j - 2] == self.my_num[self.j - 1]:
                        if self.my_num[self.j] == self.my_num[self.j + 1]:
                            if self.my_num[self.j - 1] == 2 * self.my_num[self.j]:
                                self.my_num[self.j + 1] = 2 * self.my_num[self.j]
                                self.my_num[self.j] = 2 * self.my_num[self.j - 1]
                                self.my_num[self.j - 1] = 0
                                self.my_num[self.j - 2] = 0
                                self.score = self.score + self.my_num[self.j] + self.my_num[self.j + 1]
                                if self.my_num[self.j] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j] == 2048:
                                    self.score = self.score + 64
                                if self.my_num[self.j + 1] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j + 1] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j + 1] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j + 1] == 2048:
                                    self.score = self.score + 64
                                self.c = self.c + 4
                                continue
                self.j = i
                for each in range(0, 4):
                    while True:
                        if self.j < self.c:
                            self.j = self.c + 2
                            break
                        if self.my_num[self.j + 1]:
                            if self.my_num[self.j] == self.my_num[self.j + 1]:
                                if self.my_num[self.j] in self.k:
                                    self.j = self.j - 1
                                    continue
                                self.score = self.score + 2 * self.my_num[self.j]
                                self.my_num[self.j + 1] = self.my_num[self.j] + self.my_num[self.j]
                                self.my_num[self.j] = 0
                                if self.my_num[self.j + 1] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j + 1] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j + 1] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j + 1] == 2048:
                                    self.score = self.score + 64
                                self.k.append(self.my_num[self.j + 1])
                                self.j = self.j - 1
                                continue
                            else:
                                self.j = self.j - 1
                                continue
                        else:
                            self.my_num[self.j + 1] = self.my_num[self.j]
                            self.my_num[self.j] = 0
                            self.j = self.j - 1
                            continue
                self.c = self.c + 4
                self.k = []
            self.c = 0
            self.j = 0
            self.new_number()
            self.update_text()
            self.update_score()
            self.update_high_score()
            self.update_color()
            self.win()
            self.check_game_over()

    def on_l_click(self):
        if not self.not_start_game:
            self.c = 3
            for i in [1, 5, 9, 13]:
                if self.my_num[self.j] and self.my_num[self.j + 2]:
                    if self.my_num[self.j + 1] == self.my_num[self.j + 2]:
                        if self.my_num[self.j - 1] == self.my_num[self.j]:
                            if self.my_num[self.j + 1] == 2 * self.my_num[self.j]:
                                self.my_num[self.j - 1] = 2 * self.my_num[self.j]
                                self.my_num[self.j] = 2 * self.my_num[self.j + 1]
                                self.my_num[self.j + 1] = 0
                                self.my_num[self.j + 2] = 0
                                self.score = self.score + self.my_num[self.j] + self.my_num[self.j - 1]
                                if self.my_num[self.j] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j] == 2048:
                                    self.score = self.score + 64
                                if self.my_num[self.j - 1] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j - 1] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j - 1] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j - 1] == 2048:
                                    self.score = self.score + 64
                                self.c = self.c + 4
                                continue
                self.j = i
                for each in range(0, 4):
                    while True:
                        if self.j > self.c:
                            self.j = self.c - 2
                            break
                        if self.my_num[self.j - 1]:
                            if self.my_num[self.j] == self.my_num[self.j - 1]:
                                if self.my_num[self.j] in self.k:
                                    self.j = self.j + 1
                                    continue
                                self.score = self.score + 2 * self.my_num[self.j]
                                self.my_num[self.j - 1] = self.my_num[self.j] + self.my_num[self.j]
                                self.my_num[self.j] = 0
                                if self.my_num[self.j - 1] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j - 1] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j - 1] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j - 1] == 2048:
                                    self.score = self.score + 64
                                self.k.append(self.my_num[self.j - 1])
                                self.j = self.j + 1
                                continue
                            else:
                                self.j = self.j + 1
                                continue
                        else:
                            self.my_num[self.j - 1] = self.my_num[self.j]
                            self.my_num[self.j] = 0
                            self.j = self.j + 1
                            continue
                self.c = self.c + 4
                self.k = []
            self.c = 0
            self.j = 0
            self.new_number()
            self.update_text()
            self.update_score()
            self.update_high_score()
            self.update_color()
            self.win()
            self.check_game_over()

    def on_d_click(self):
        if not self.not_start_game:
            self.c = 0
            for i in [8, 9, 10, 11]:
                if self.my_num[self.j - 8] and self.my_num[self.j]:
                    if self.my_num[self.j - 8] == self.my_num[self.j - 4]:
                        if self.my_num[self.j] == self.my_num[self.j + 4]:
                            if self.my_num[self.j - 4] == 2 * self.my_num[self.j]:
                                self.my_num[self.j + 4] = 2 * self.my_num[self.j]
                                self.my_num[self.j] = 2 * self.my_num[self.j - 4]
                                self.my_num[self.j - 4] = 0
                                self.my_num[self.j - 8] = 0
                                self.score = self.score + self.my_num[self.j] + self.my_num[self.j + 4]
                                if self.my_num[self.j] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j] == 2048:
                                    self.score = self.score + 64
                                if self.my_num[self.j + 4] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j + 4] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j + 4] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j + 4] == 2048:
                                    self.score = self.score + 64
                                self.c = self.c + 1
                                continue
                self.j = i
                for each in range(0, 4):
                    while True:
                        if self.j < self.c:
                            self.j = self.c + 8
                            break
                        if self.my_num[self.j + 4]:
                            if self.my_num[self.j] == self.my_num[self.j + 4]:
                                if self.my_num[self.j] in self.k:
                                    self.j = self.j - 4
                                    continue
                                self.score = self.score + 2 * self.my_num[self.j]
                                self.my_num[self.j + 4] = self.my_num[self.j] + self.my_num[self.j]
                                self.my_num[self.j] = 0
                                if self.my_num[self.j + 4] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j + 4] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j + 4] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j + 4] == 2048:
                                    self.score = self.score + 64
                                self.k.append(self.my_num[self.j + 4])
                                self.j = self.j - 4
                                continue
                            else:
                                self.j = self.j - 4
                                continue
                        else:
                            self.my_num[self.j + 4] = self.my_num[self.j]
                            self.my_num[self.j] = 0
                            self.j = self.j - 4
                            continue
                self.c = self.c + 1
                self.k = []
            self.c = 0
            self.j = 0
            self.new_number()
            self.update_text()
            self.update_score()
            self.update_high_score()
            self.update_color()
            self.win()
            self.check_game_over()

    def on_u_click(self):
        if not self.not_start_game:
            self.c = 12
            for i in [4, 5, 6, 7]:
                if self.my_num[self.j] and self.my_num[self.j + 8]:
                    if self.my_num[self.j + 4] == self.my_num[self.j + 8]:
                        if self.my_num[self.j - 4] == self.my_num[self.j]:
                            if self.my_num[self.j + 4] == 2 * self.my_num[self.j]:
                                self.my_num[self.j - 4] = 2 * self.my_num[self.j]
                                self.my_num[self.j] = 2 * self.my_num[self.j + 4]
                                self.my_num[self.j + 4] = 0
                                self.my_num[self.j + 8] = 0
                                self.score = self.score + self.my_num[self.j] + self.my_num[self.j - 4]
                                if self.my_num[self.j] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j] == 2048:
                                    self.score = self.score + 64
                                if self.my_num[self.j - 4] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j - 4] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j - 4] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j - 4] == 2048:
                                    self.score = self.score + 64
                                self.c = self.c + 1
                                continue
                self.j = i
                for each in range(0, 4):
                    while True:
                        if self.j > self.c:
                            self.j = self.c - 8
                            break
                        if self.my_num[self.j - 4]:
                            if self.my_num[self.j] == self.my_num[self.j - 4]:
                                if self.my_num[self.j] in self.k:
                                    self.j = self.j + 4
                                    continue
                                self.score = self.score + 2 * self.my_num[self.j]
                                self.my_num[self.j - 4] = self.my_num[self.j] + self.my_num[self.j]
                                self.my_num[self.j] = 0
                                if self.my_num[self.j - 4] == 64:
                                    self.score = self.score + 4
                                if self.my_num[self.j - 4] == 256:
                                    self.score = self.score + 8
                                if self.my_num[self.j - 4] == 1024:
                                    self.score = self.score + 16
                                if self.my_num[self.j - 4] == 2048:
                                    self.score = self.score + 64
                                self.k.append(self.my_num[self.j - 4])
                                self.j = self.j + 4
                                continue
                            else:
                                self.j = self.j + 4
                                continue
                        else:
                            self.my_num[self.j - 4] = self.my_num[self.j]
                            self.my_num[self.j] = 0
                            self.j = self.j + 4
                            continue
                self.c = self.c + 1
                self.k = []
            self.c = 0
            self.j = 0
            self.new_number()
            self.update_text()
            self.update_score()
            self.update_high_score()
            self.update_color()
            self.win()
            self.check_game_over()


class WidgetsExample(GridLayout):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
