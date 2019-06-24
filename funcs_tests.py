import unittest
from funcs import *

letters = 'WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
letters2 = 'EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'
letters3 = 'LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP'
rows = get_rows(letters)
columns = get_columns(letters)
rows2 = get_rows(letters2)
columns2 = get_columns(letters2)
rows3 = get_rows(letters3)
columns3 = get_columns(letters3)

class TestCases(unittest.TestCase):

    def test_get_rows1(self):
        self.assertListEqual(get_rows(letters), ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN',
                                                 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])
    def test_get_columns1(self):
        self.assertListEqual(get_columns(letters), ['WCALPOLYXU', 'ABPDOEGCVU', 'QMXENDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN',
                                                    'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])
    def test_check_forward1(self):
        self.assertTupleEqual(check_forward(rows, 'POND'), (0, 'FORWARD'))

    def test_check_forward2(self):
        self.assertTupleEqual(check_forward(rows, 'WEE'), (7, 'FORWARD'))

    def test_check_forward3(self):
        self.assertFalse(check_forward(rows, 'ABCD'))

    def test_check_forward4(self):
        self.assertTupleEqual(check_forward(rows2, 'ZEBRA'), (0, 'FORWARD'))

    def test_check_forward5(self):
        self.assertTupleEqual(check_forward(rows3, 'CHORRO'), (3, 'FORWARD'))

    def test_check_forward6(self):
        self.assertFalse(check_forward(rows3, 'PEACH'))

    def test_check_backward1(self):
        self.assertTupleEqual(check_backward(rows, 'VIM'), (5, 'BACKWARD'))

    def test_check_backward2(self):
        self.assertTupleEqual(check_backward(rows, 'YOS'), (4, 'BACKWARD'))

    def test_check_backward3(self):
        self.assertFalse(check_backward(rows, 'ZZZZ'))

    def test_check_backward4(self):
        self.assertTupleEqual(check_backward(rows2, 'BEAR'), (3, 'BACKWARD'))

    def test_check_backward5(self):
        self.assertTupleEqual(check_backward(rows3, 'HIGH'), (0, 'BACKWARD'))

    def test_check_backward6(self):
        self.assertFalse(check_backward(rows3, 'CHORRO'))

    def test_check_upward1(self):
        self.assertTupleEqual(check_upward(columns, 'COMPILE'), (3, 'UP'))

    def test_check_upward2(self):
        self.assertTupleEqual(check_upward(columns, 'YMXW'), (4, 'UP'))

    def test_check_upward3(self):
        self.assertFalse(check_upward(columns, 'GAIN'))

    def test_check_upward4(self):
        self.assertTupleEqual(check_upward(columns2, 'CHICKEN'), (1, 'UP'))

    def test_check_upward5(self):
        self.assertTupleEqual(check_upward(columns3, 'MARSH'), (3, 'UP'))

    def test_check_upward6(self):
        self.assertFalse(check_upward(columns3, 'HIGHLAND'))

    def test_check_downward1(self):
        self.assertTupleEqual(check_downward(columns, 'CALPOLY'), (1, 'DOWN'))

    def test_check_downward2(self):
        self.assertTupleEqual(check_downward(columns, 'LIP'), (1, 'DOWN'))

    def test_check_downward3(self):
        self.assertFalse(check_downward(columns, 'HFHDJ'))

    def test_check_downward4(self):
        self.assertTupleEqual(check_downward(columns2, 'RABBIT'), (1, 'DOWN'))

    def test_check_downward5(self):
        self.assertTupleEqual(check_downward(columns3, 'HIGUERA'), (0, 'DOWN'))

    def test_check_downward6(self):
        self.assertFalse(check_downward(columns2, 'KOALA'))

    def test_check_diagonal(self):
        self.assertTupleEqual(check_diagonal(rows, 'CPE'), (1,0,'DIAGONAL'))

    def test_check_diagonal2(self):
        self.assertFalse(check_diagonal(rows, 'SLO'))

    #ask how to test for multiple puzzles, not just one
    #does the asking of letters have to be in funcs or word_solver?

if __name__ == '__main__':
   unittest.main()
