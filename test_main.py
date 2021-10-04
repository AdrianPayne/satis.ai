import unittest
from main import process_orders

data_input = """R1,4C,1,3A,2,2P,1,100,200,200,100,100
R1,2020-12-08 19:15:31,O1,BLT,LT,VLT
R1,2020-12-08 19:15:32,O2,VLT,VT,BLT,LT,VLT
R1,2020-12-08 19:16:05,O3,VLT,VT,BLT,LT,VLT
R1,2020-12-08 19:17:15,O4,BT,BLT,VLT,BLT,BT,LT,VLT
R1,2020-12-08 19:19:10,O5,BLT,LT,VLT
R1,2020-12-08 19:15:32,O6,VLT,VT,BLT,VLT,BT
R1,2020-12-08 19:16:05,O7,VLT,LT,BLT,LT,VLT
R1,2020-12-08 19:17:15,O8,BT,BLT,VLT,BLT,BLT
R1,2020-12-08 19:18:15,O9,BT,BLT,VLT,BLT,BLT
R1,2020-12-08 19:21:10,O10,BLT,VLT
R1,2020-12-08 19:25:17,O11,VT,VLT
R1,2020-12-08 19:28:17,O12,VT,VLT""".split('\n')
data_input = [row.split(',') for row in data_input]


class TestMain(unittest.TestCase):
    data_test = data_input

    def test_incorrect_input(self):
        with self.assertRaises():
            process_orders([])

    def test_one_order(self):
        local_data = self.data_test[:2]
        output_expected = """R1,O1,ACCEPTED,5
        R1,TOTAL,5
        R1,INVENTORY,94,197,197,99,99
        """
        self.assertEqual(output_expected, process_orders(local_data))

    def test_one_reject(self):
        # TODO
        self.assertEquals(1, 0)

    def test_all_input(self):
        # TODO
        self.assertEquals(1, 0)


if __name__ == '__main__':
    unittest.main()
