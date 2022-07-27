import os
import sys
from nile.nre import NileRuntimeEnvironment

sys.path.append(os.path.dirname(__file__))

def run(nre: NileRuntimeEnvironment):
    print("Show Player score")

    player = nre.get_or_deploy_account("PKEYPLAYER")
    print(f"Player account address: {player.address}")

    res = nre.call(
        "tournament",
        "player_score",
        [player.address],
    )
    print(f"Player score: {res}")