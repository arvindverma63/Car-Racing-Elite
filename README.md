# Car-Racing-Elite

Car Racing Elite
Car Racing Elite is a 2D car racing game built with Pygame, where players control a car to avoid oncoming enemy vehicles while earning points. The game features a sleek interface, dynamic road scrolling, car shadows, exhaust trail effects, and a speedometer-like HUD. It includes start, gameplay, and game-over states with intuitive controls and gradient-styled buttons.
Features

Gameplay: Navigate a player car left or right to avoid collisions with enemy cars.
Scoring: Earn points for each enemy car that passes off-screen.
Visuals:
Procedurally drawn car sprites with headlights, spoilers, and windows.
Dynamic road with lane lines and scrolling effect.
Shadow and exhaust trail particle effects for realism.
Gradient buttons and a speedometer-inspired HUD.


States:
Start screen with "Start" and "Quit" buttons.
Gameplay with player movement and enemy spawning.
Game-over screen with score display and "Restart" or "Quit" options.


Controls:
Left Arrow (←): Move car left.
Right Arrow (→): Move car right.
Mouse: Click "Start," "Restart," or "Quit" buttons.



Requirements

Python: 3.13.1 (tested), or any Python 3.8+ version.
Pygame: 2.6.1 (tested), installable via pip.
Operating System: Windows, macOS, or Linux.
Optional: Orbitron font (Orbitron.ttf) for enhanced UI (place in project directory).

Installation

Clone or Download the Project:

Copy all project files to a directory (e.g., D:\Python Tkinter\Car-War\).


Set Up a Virtual Environment (recommended):
python -m venv .venv
.\venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux


Install Pygame:
pip install pygame==2.6.1


Verify Project Files:Ensure the following files are in the project directory:

main.py
constants.py
player.py
enemy.py
road.py
ui.py
trail_particle.py


Optional: Custom Font:

Download Orbitron.ttf and place it in the project directory.
Update main.py to use the font:title_font = pygame.font.Font("Orbitron.ttf", 70)
ui_font = pygame.font.Font("Orbitron.ttf", 35)





Usage

Run the Game:
python main.py


Game Flow:

Start Screen: Click "Start" to begin or "Quit" to exit.
Gameplay: Use ← and → keys to move the player car, avoiding enemy cars. Score increases as enemies pass.
Game Over: Colliding with an enemy ends the game. Click "Restart" to play again or "Quit" to exit.


Exit: Click "Quit" or close the window to exit the game.


File Structure

main.py: Core game loop, state management, and initialization (Pygame, fonts, display).
constants.py: Game constants (dimensions, colors, speeds, states).
player.py: Player car class with movement, drawing, and trail effects; includes create_car function.
enemy.py: Enemy car class with random spawning and movement.
road.py: Road class for scrolling background with lane lines.
ui.py: UI functions for text, gradient buttons, and HUD rendering.
trail_particle.py: Trail particle class for exhaust effects.

Troubleshooting

Error: pygame.error: font not initialized:
Ensure pygame.init() is called before font operations. Verify main.py has font initialization after pygame.init().


Error: NameError: name 'PLAYER_SPEED' is not defined:
Check that PLAYER_SPEED is imported in main.py from constants.py.


Quit Button Not Working:
Confirm main.py uses self.quit_game() for the "Quit" button action, not globals().update.


Syntax Errors:
Check for non-printable characters (e.g., U+00A0). Use a text editor like VS Code with “Render Control Characters” enabled.


Missing Modules:
Install Pygame: pip install pygame.
Ensure all project files are in the same directory.



Future Improvements

Add sound effects for collisions, button clicks, and background music.
Implement a high-score system with persistent storage.
Support custom car images instead of procedural sprites.
Add difficulty levels (e.g., increasing enemy speed over time).
Include a pause menu or settings screen.

License
This project is licensed under the MIT License. Feel free to modify and distribute it.

Built with ❤️ using Pygame. Contributions welcome!
