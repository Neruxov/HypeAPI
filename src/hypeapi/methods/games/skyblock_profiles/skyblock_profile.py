from .skyblock_profile_member import *

class SkyBlockProfile:
    def __init__(self, data):
        self.data = data

    def getProfileID(self):
        return self.data['profile_id']

    def getCuteName(self):
        return self.data['cute_name']

    def getProfileMembers(self):
        if self.data['members'] is None:
            return None

        members = []

        for i in self.data['members']:
            members.append(SkyBlockMember(self.data['members'][i], i))

        return members

    def getMembers(self):
        return self.data['members']
