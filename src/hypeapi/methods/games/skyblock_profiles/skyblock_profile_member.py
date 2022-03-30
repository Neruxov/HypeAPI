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

    def getFirstJoin(self):
        return self.data['first_join']

    def getFirstJoinHub(self):
        return self.data['first_join_hub']

    def getDeaths(self):
        return self.data['stats']['deaths']

    def getKills(self):
        return self.data['stats']['kills']

    def getHighestCritDamage(self):
        return self.data['stats']['highest_critical_damage']

    def getAuctionsBids(self):
        return self.data['stats']['auctions_bids']

    def getAuctionsHighestBid(self):
        return self.data['stats']['auctions_highest_bid']

    def getAuctionsCompleted(self):
        return self.data['stats']['auctions_completed']

    def getAuctionsWon(self):
        return self.data['stats']['auctions_won']

    def getAuctionsGoldSpend(self):
        return self.data['stats']['auctions_gold_spend']

    def getAuctionsCreated(self):
        return self.data['stats']['auctions_created']

    def getAuctionsFees(self):
        return self.data['stats']['auctions_fees']

    def getPurse(self):
        return self.data['coins_purse']

    def getLastDeath(self):
        return self.data['last_death']

    def getFairySouls(self):
        return self.data['fairy_souls']

