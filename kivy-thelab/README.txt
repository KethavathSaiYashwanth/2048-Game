Packages:
    I installed kivy package and then imported App, Layouts like BoxLayout, GridLayout and imported
    properties like StringProperty, NumericProperty, BooleanProperty, listProperty, ColorProperty.
    Also imported window from kivy.
    Imported random.

Program Structure:
    I created a class GridLayoutExample, which is a type of GridLayout and is the main layout.
    I also created another class WidgetsExample of type GridLayout and BoxLayoutExample of type BoxLayout
    and used them inside the kv file many times.
    Inside the main class, that is GridLayoutExample, i introduced many objects and also used the StringProperty,
    NumericProperty, BooleanProperty, listProperty, ColorProperty as without these any changes in main.py will not be
    seen in kv file.
    I developed __init__ function and given access to the keyboard arrows.
    I wrote all the functions needed and also the functions for new_game, on_l_click, on_r_click, on_u_click,
    on_d_click buttons  which are 'enter', 'left', 'right', 'up', 'down' respectively on the keyboard.
    I also attached some font files and used them in the kv file.
    I wrote each navigation button by using for loops and changing row by row or column column.

Instructions:
    1.Game does not start until we click "START GAME" and when clicked, it turns into "NEW GAME".
    Without clicking "START GAME", the direction buttons and also the keyboard arrows will remain disabled.
    2.Two numbers, each is either 2 or 4, will be appeared randomly on the 4x4 grid. We can use either buttons on window
    or the keyboard arrows to play.
    3.After each navigation button is clicked, we get either 2 or 4 on a random empty tile of the grid.
    4.Each distinct number will have its own unique background color on grid.
    5.Score increases as every pairing takes place and gets added to the score. High score will show the maximum of
    scores of the previous games played.
    6.Score gets a bonus for every pairing resulting in 64, 256, 1024, 2048 as 4, 8, 16, 64 respectively.
    7.Our goal is to achieve 2048, if we do so, the Label 2048 turns into "YOU WIN". Otherwise, you end up in a grid
    totally filled up with no chance of further pairing, the Label 2048 turns into "GAME OVER" and the new game button
    turns into "TRY AGAIN", also the buttons and the grid will be changed in appearance and cannot be changed until
    "TRY AGAIN" is clicked.

Extra Feature:
    I added a difficulty level Slider ranging from 0 to 100, which is on default, on 10.
    This difficulty level is based on the probability of getting on one tile of the grid.
    The less the probability of getting 4, the more the difficulty level is the logic used.
    The reason is "Achieving 1024 with all 2s is equivalent to achieving 2048 with all 4s" and hence more probability
    of 4 will make the game easier.
