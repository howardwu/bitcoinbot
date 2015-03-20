import csv


class models():

    """ A collection of models stored in the directory. Models
        are stored locally as tables when called.
    """

    def getModel(self, name):
        """Return the table whose name is NAME stored in this collection."""
        f = open('one.csv')
        csv_f = csv.reader(f)
        return csv_f

    def getPrices(self, name):
        """Return a list of prices from this model."""
        table = getModel(name)
        prices = []
        for row in table:
            prices.append(row[3])
        return prices
