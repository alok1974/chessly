import shutil
import os


from .. import constant as c
from .gamer import Game


class Engine:
    def __init__(self, engine_type=c.EngineType.stockfish, engine_params=None):
        self._engine_type = engine_type
        self._engine_params = engine_params
        self._engine = self._get_engine(
            engine_type=engine_type,
            engine_params=engine_params,
        )

    @property
    def engine_exists(self):
        return bool(self._engine)

    def get_best_move(self, moves=None):
        if not self.engine_exists:
            raise RuntimeError('No engine found!')
        moves = moves or []
        self._apply_moves(moves=moves)
        return self._engine.get_best_move()

    def _apply_moves(self, moves):
        moves = list(map(Game.parse_move_spec, moves))
        moves = list(map(lambda x: f'{x[0].address}{x[1].address}', moves))
        self._engine.set_position(moves)

    def _get_engine(self, engine_type, engine_params=None):
        if engine_type == c.EngineType.stockfish:
            return self._get_stockfish(engine_params=engine_params)
        else:
            error_msg = f"Unsupported engine {engine_type}"
            raise RuntimeError(error_msg)

    @staticmethod
    def _get_stockfish(engine_params=None):
        # Check for stockfish executable
        exe = shutil.which(c.APP.STOCKFISH_EXE_NAME)
        if exe is None:
            return
        elif not os.path.exists(exe):
            return

        # Try to loading the engine
        try:
            from stockfish import Stockfish
            return Stockfish(parameters=engine_params)
        except Exception:
            return
