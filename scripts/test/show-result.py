import os
import sys
from nile.nre import NileRuntimeEnvironment

sys.path.append(os.path.dirname(__file__))


def run(nre: NileRuntimeEnvironment):
    print("Show Player score")

    player = nre.get_or_deploy_account("PKEYPLAYER")
    print(f"Player account address: {player.address}")

    res = nre.call("tournament", "player_score", [player.address])
    print(f"Player score: {res}")

    res = nre.call("tournament", "ship_count", [] )
    print(f"Tournament.ship_count: {res}")
    
    res = nre.call("tournament", "max_dust", [] )
    print(f"Tournament.max_dust: {res}")
    
    res = nre.call("tournament", "turn_count", [] )
    print(f"Tournament.turn_count: {res}")
    
    res = nre.call("tournament", "grid_size", [] )
    print(f"Tournament.grid_size: {res}")
    
    res = nre.call("tournament", "tournament_winner", [] )
    print(f"Tournament.tournament_winner: {res}")

    res = nre.call("tournament", "played_battle_count", [] )
    print(f"Tournament.played_battle_count: {res}")
