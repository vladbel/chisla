class DataProviderBase:
    result = []
    def get_data(self):
        return result


class DataProviderSimple ( DataProviderBase ):

    def __init__( self ):
        self.result = [1, 2, 3]