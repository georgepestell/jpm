import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    # Make sure a TypeError is thrown when a None value is passed into getDataPoint
    def test_getDataPoint_exceptionOnNoneValue(self):
        self.assertRaises(TypeError, getDataPoint, None)

    # Make sure a KeyError is thrown when key information is missing from quote
    def test_getDataPoint_exceptionOnMissingAskPrice(self):

        # Does not contain the top_ask price
        quote = {'top_ask': {'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}

        self.assertRaises(KeyError, getDataPoint, quote)

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Check getDataPoint returns the correct tuple for each quote example
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        # These quotes have a higher price for top_bid than top_ask"
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Check getDataPoint returns the correct tuple for each quote example
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio_priceANotNumber(self):
        price_a = "2.3"
        price_b = 2.3

        self.assertRaises(TypeError, getRatio, price_a, price_b)

    def test_getRatio_priceBNotNumber(self):
        price_a = 2.3
        price_b = "4.6"

        self.assertRaises(TypeError, getRatio, price_a, price_b)

    def test_getRatio_calculateRatio(self):
        price_a = 4.6
        price_b = 2.3

        self.assertEqual(getRatio(price_a, price_b), (price_a / price_b))

    def test_getRatio_calculateRatioPriceAGreaterThanPriceB(self):
        price_a = 2.3
        price_b = 4.6

        self.assertEqual(getRatio(price_a, price_b), (price_a / price_b))

    def test_getRatio_PriceAIsZero(self):
        price_a = 0
        price_b = 4.6

        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_priceBIsZero(self):
        price_a = 2.3
        price_b = 0

        self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
    unittest.main()
