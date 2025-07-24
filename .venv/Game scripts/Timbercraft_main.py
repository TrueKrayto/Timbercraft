import arcade

class TimbercraftWindow(arcade.Window):
    def __init__(self):
        screen_width, screen_height = arcade.get_display_size()
        super().__init__(screen_width, screen_height, title="Timbercraft", fullscreen=True)

def main():
    window = TimbercraftWindow()
    arcade.run()

if __name__ == "__main__":
    main()