class SkyBlockMember:
    def __init__(self, data, uuid):
        self.data = data
        self.uuid = uuid

    def getUUID(self):
        return self.uuid

    def getLastSave(self):
        return self.data['last_save']

    def getInventoryArmor(self):
        pass