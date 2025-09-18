import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample
import joblib

df = pd.read_csv("data.csv")
df.dropna(inplace=True)

#only active rounds
df = df[(df['has_round_started'] == True) & (df['is_player_in_move'] == True)]

#labels
button_labels = [
    'player1_buttons up', 'player1_buttons down', 'player1_buttons right', 'player1_buttons left',
    'player1_buttons Y', 'player1_buttons B', 'player1_buttons A',
    'player1_buttons R', 'player1_buttons L', 'player1_buttons X'
]
df = df[df[button_labels].sum(axis=1) > 0]

#spatial features
df['x_diff'] = df['x_coord']- df['Player2 x_coord']
df['y_diff'] = df['y_coord'] -df['Player2 y_coord']
df['is_facing_right'] = (df['x_diff'] < 0).astype(int)

#input features
input_features = [
    'Player1_ID', 'health', 'x_coord', 'y_coord',
    'is_jumping', 'is_crouching', 'is_player_in_move', 'move_id',
    'Player2_ID', 'Player2 health', 'Player2 x_coord', 'Player2 y_coord',
    'Player2 is_jumping', 'Player2 is_crouching', 'Player2 is_player_in_move', 'Player2 move_id',
    'x_diff', 'y_diff', 'is_facing_right'
]

X = df[input_features]
y = df[button_labels]

#conbine for balancing 
df_balanced = pd.concat([X, y], axis=1)
min_samples = 500
for btn in button_labels:
    class_1 = df_balanced[df_balanced[btn] == 1]
    class_0 = df_balanced[df_balanced[btn] == 0]
    
    if len(class_1) == 0:
        continue  #skip if no positive samples for this button

    if len(class_1) < min_samples:
        class_1_up =resample(class_1, replace=True, n_samples=min_samples, random_state=42)
        df_balanced=pd.concat([class_0, class_1_up])

#separate features and labels
X = df_balanced[input_features]
y = df_balanced[button_labels]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, "scaler.pkl")

# Train model
model = MultiOutputClassifier(
    MLPClassifier(hidden_layer_sizes=(128, 64, 32), activation='relu',
                  solver='adam',max_iter=600, alpha=1e-4, random_state=42,verbose=True)
)
model.fit(X_train_scaled, y_train)

# Save
joblib.dump(model, "model.pkl")
print("Model and scaler saved")
