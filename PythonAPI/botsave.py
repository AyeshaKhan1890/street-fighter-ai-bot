from command import Command
from buttons import Buttons
import pandas as pd
import joblib

class Bot:
    def __init__(self):
        # Load trained ML model with 10-output prediction
        self.model = joblib.load("trained_bot.pkl")

        # Ensure these match the training input feature columns
        self.feature_columns = [
            'Player1_ID', 'health', 'x_coord', 'y_coord',
            'is_jumping', 'is_crouching', 'is_player_in_move', 'move_id',
            'Player2_ID', 'Player2 health', 'Player2 x_coord', 'Player2 y_coord',
            'Player2 is_jumping', 'Player2 is_crouching', 'Player2 is_player_in_move', 'Player2 move_id'
        ]

    def fight(self, current_game_state, player):
        p1 = current_game_state.player1
        p2 = current_game_state.player2

        # Build the input feature row (current game state)
        features = pd.DataFrame([[
            p1.player_id, p1.health, p1.x_coord, p1.y_coord,
            int(p1.is_jumping), int(p1.is_crouching), int(p1.is_player_in_move), p1.move_id,
            p2.player_id, p2.health, p2.x_coord, p2.y_coord,
            int(p2.is_jumping), int(p2.is_crouching), int(p2.is_player_in_move), p2.move_id
        ]], columns=self.feature_columns)

        # Predict the 10-button output using the trained model
        prediction = self.model.predict(features)[0]

        # Map prediction to Buttons object
        buttons = Buttons()
        (buttons.up, buttons.down, buttons.right, buttons.left,
         buttons.Y, buttons.B, buttons.A,
         buttons.R, buttons.L, buttons.X) = map(bool, prediction)

        # Assign to the correct player
        my_command = Command()
        if player == "1":
            my_command.player_buttons = buttons
        else:
            my_command.player2_buttons = buttons

        return my_command
