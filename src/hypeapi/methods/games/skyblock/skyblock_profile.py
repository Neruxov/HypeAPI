from .skyblock_profile_member import *

class SkyblockProfile:
    def __init__(self, api, data):
        self.api = api
        self.data = data

    def getProfileID(self):
        return self.data['profile_id']

    def getCuteName(self):
        return self.data['cute_name']

    def getSkyblockMembers(self):
        if self.data['members'] == None:
            return None

        members = []

        for i in self.data['members']:
            members.append(SkyblockProfile(self.api, i))

        self.members = members

        return members