from .skyblock_profiles.skyblock_profile import *
from ...util.api_requests import *


class SkyBlock:
    def __init__(self, player):
        self.player = player
        self.profiles = self.getProfiles()

    def getProfiles(self):
        player_profiles = getSkyBlockProfiles(self.player.api, uuid=self.player.uuid)['profiles']

        if player_profiles is None:
            return None

        profiles = []

        for i in player_profiles:
            profiles.append(SkyBlockProfile(i))

        return profiles
