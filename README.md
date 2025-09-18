# Street Fighter AI Game Bot - Spring 2025

## Description

This project implements a Machine Learning-based game bot that plays Street Fighter II Turbo on the SNES emulator using Python. The bot replaces rule-based logic with ML-based decisions and interacts with the game through socket communication via the BizHawk emulator's Python API.

## Team Members

- 23i-0129_Ayesha Khan
- 23i-0054_Moomena Asad
- 23i-0192_Nawaal

## Installation

### Requirements
- Windows 7 or higher (64-bit)
- Python 3.6.3+
- BizHawk Emulator (via provided Google Drive link)
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `joblib`

### Setup Instructions

1. Download the BizHawk emulator:
   [BizHawk Download](https://drive.google.com/file/d/18SN8e_XqJFEPZ0wcWXQ8GnzuZk58cn-2/view?usp=sharing)

2. Extract the emulator and open the appropriate folder:
   - `single-player` to run bot vs CPU
   - `two-players` to run bot vs bot

3. Open `EmuHawk.exe`, go to:
   - `File > Open ROM` and load `Street Fighter II Turbo (U).smc`
   - `Tools > Tool Box`

4. Leave emulator/toolbox open. Then open terminal in the API folder and run:

   ```bash
   python controller.py 1  # For player 1 bot

## Installation

### Requirements
- Windows 7 or higher (64-bit)
- Python 3.6.3+
- BizHawk Emulator (via provided Google Drive link)
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `joblib`

### Setup Instructions

1. Download the BizHawk emulator:
   [BizHawk Download](https://drive.google.com/file/d/18SN8e_XqJFEPZ0wcWXQ8GnzuZk58cn-2/view?usp=sharing)

2. Extract the emulator and open the appropriate folder:
   - `single-player` to run bot vs CPU

3. Open `EmuHawk.exe`, go to:
   - `File > Open ROM` and load `Street Fighter II Turbo (U).smc`
   - `Tools > Tool Box`

4. Leave emulator/toolbox open. Then open terminal in the API folder and run:

   ```bash
   python controller.py 1  # For player 1 bot


### 5. **Code Structure and ML Model**

## Code Structure

- `bot.py`: Main bot logic and ML model prediction.
- `controller.py`: Establishes socket communication and game loop.
- `command.py`: Defines the Command object to send button presses.
- `buttons.py`: Represents button states on the SNES gamepad.
- `player.py`: Stores player attributes (health, position, actions).
- `game_state.py`: Aggregates all current game information for decision-making.

## ML Model Usage

1. Run the game with a human player and log data (e.g., to CSV).
2. Train your ML model externally using this data.
3. Save the model as `model.pkl` using `joblib`.
4. The bot will load this model automatically in `bot.py` and use it to predict moves.
---
## Running the Bot

To run the bot after setting up everything:

        python controller.py 1
## Running the Bot

To run the bot after setting up everything:

        python controller.py 1

## Acknowledgements

- This project is part of the Artificial Intelligence course (Spring 2025) at FAST.
- Emulator and base code provided by course instructors.