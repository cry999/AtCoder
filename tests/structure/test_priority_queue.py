from util.structure import priority_queue as pq
import unittest


class TestPriorityQueue(unittest.TestCase):
    def test_dequeue_from_small_one(self):
        q = pq.PriorityQueue()

        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(5)

        for expected in [1, 2, 3, 4, 5]:
            v = q.dequeue()
            self.assertEqual(
                expected, v,
                msg='dequeue is expected {}, but {}'.format(expected, v))

    def test_empty(self):
        q = pq.PriorityQueue()
        self.assertTrue(
            q.empty(),
            msg='initialized q.empty() expected to be True, but not')

        q.enqueue(1)
        self.assertFalse(
            q.empty(),
            msg='after enqueue empty() expected to be False, but not')

        q.dequeue()
        self.assertTrue(
            q.empty(),
            msg='after dequeue all empty() expected to be True, but not')


if __name__ == "__main__":
    unittest.main()
