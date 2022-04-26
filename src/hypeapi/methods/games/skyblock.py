from ...util.api_requests import *


class SkyBlock:
    def __init__(self, api):
        self.api = api

    def getAuctions(self, page=0):
        return getSkyBlockAuctions(self.api, page)['auctions']

    def getAuction(self, auction_uuid=None, player=None, profile=None):
        return getSkyBlockAuction(self.api, auction_uuid, player, profile)

    def getItems(self):
        return getSkyBlockItems(self.api)['items']
