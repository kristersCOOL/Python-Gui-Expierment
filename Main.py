import ctypes

# Load the shared library
game_lib = ctypes.CDLL('./Gui.so')

# Call the create_window function
game_lib.run_game()

