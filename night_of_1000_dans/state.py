from engine.game.state import GameState

class NOTDGameState(GameState):
    def __init__(self):
        super().__init__()
        self.player_name = "Michael"

    @property
    def qa_mode(self):
        return self.player_name.lower() == "qa"

game_state = NOTDGameState()
