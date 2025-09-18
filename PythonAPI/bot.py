from command import Command
from buttons import Buttons
import pandas as pd
import joblib

class Bot:
    def __init__(self):
        self.model = joblib.load("model.pkl")
        self.scaler = joblib.load("scaler.pkl")

        self.feature_columns = [
            'Player1_ID', 'health', 'x_coord', 'y_coord',
            'is_jumping', 'is_crouching', 'is_player_in_move', 'move_id',
            'Player2_ID', 'Player2 health', 'Player2 x_coord', 'Player2 y_coord',
            'Player2 is_jumping', 'Player2 is_crouching', 'Player2 is_player_in_move', 'Player2 move_id',
            'x_diff', 'y_diff', 'is_facing_right'
        ]

    def fight(self, current_game_state, player):
        p1 = current_game_state.player1
        p2 = current_game_state.player2

        #spatial features 
        x_diff = p1.x_coord-p2.x_coord
        y_diff = p1.y_coord - p2.y_coord
        is_facing_right = int(x_diff < 0)

        #input fetaure vetcors
        features = pd.DataFrame([[ 
            p1.player_id, p1.health, p1.x_coord, p1.y_coord,
            int(p1.is_jumping),int(p1.is_crouching), int(p1.is_player_in_move), p1.move_id,
            p2.player_id, p2.health, p2.x_coord, p2.y_coord,
            int(p2.is_jumping),int(p2.is_crouching), int(p2.is_player_in_move), p2.move_id,
            x_diff, y_diff,is_facing_right
        ]], columns=self.feature_columns)

        #scale features before prediction
        scaled_features = self.scaler.transform(features)
        prediction = self.model.predict(scaled_features)[0]

        buttons = Buttons()
        (buttons.up, buttons.down, buttons.right, buttons.left,
         buttons.Y, buttons.B, buttons.A,
         buttons.R, buttons.L, buttons.X) = map(bool, prediction)

        my_command = Command()
        if player == "1":
            my_command.player_buttons=buttons
        else:
            my_command.player2_buttons = buttons

        return my_command
