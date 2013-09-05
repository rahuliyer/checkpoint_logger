#!/usr/bin/python

import unittest
import os
import os.path as path

from checkpoint import Checkpoint

class TestCheckpoint(unittest.TestCase):
	TEST_DIR = "/tmp/checkpoint_test"
	TEST_KEY = "test_key"
	TEST_KEY2 = "test_key2"

	def setUp(self):
		os.mkdir(TestCheckpoint.TEST_DIR)

	def tearDown(self):
		os.system("rm -rf " + TestCheckpoint.TEST_DIR)

	def testCreation(self):
		x = Checkpoint(TestCheckpoint.TEST_DIR)
		
		self.assertTrue(path.exists(TestCheckpoint.TEST_DIR + "/.checkpoint"))

	def testCheckLogCreation(self):
		x = Checkpoint(TestCheckpoint.TEST_DIR)
		
		x.createCheckpointLog(TestCheckpoint.TEST_KEY)
		self.assertTrue(TestCheckpoint.TEST_KEY in x.getCheckpointLogKeys())

		x.releaseCheckpointLog(TestCheckpoint.TEST_KEY)
		self.assertFalse(TestCheckpoint.TEST_KEY in x.getCheckpointLogKeys())

	def testCheckpointWrite(self):
		x = Checkpoint(TestCheckpoint.TEST_DIR)
		x.createCheckpointLog(TestCheckpoint.TEST_KEY)

		x.writeCheckpoint(TestCheckpoint.TEST_KEY, "a", 1)
		x.writeCheckpoint(TestCheckpoint.TEST_KEY, "a", 2)
		x.writeCheckpoint(TestCheckpoint.TEST_KEY, "b", 3)

		x.releaseCheckpointLog(TestCheckpoint.TEST_KEY)

		self.assertEqual(sorted(x.getCheckpointKeys()), ["a", "b"])
		self.assertEqual(x.getCheckpoints("b"), [3])
		self.assertEqual(x.getCheckpoints("a"), [1, 2])

	def testCheckpointRestart(self):
		x = Checkpoint(TestCheckpoint.TEST_DIR)
		x.createCheckpointLog(TestCheckpoint.TEST_KEY)
		x.createCheckpointLog(TestCheckpoint.TEST_KEY2)

		x.writeCheckpoint(TestCheckpoint.TEST_KEY, "a", 1)
		x.writeCheckpoint(TestCheckpoint.TEST_KEY, "a", 2)
		x.writeCheckpoint(TestCheckpoint.TEST_KEY2, "b", 3)

		x.releaseCheckpointLog(TestCheckpoint.TEST_KEY)
		x.releaseCheckpointLog(TestCheckpoint.TEST_KEY2)
		
		y = Checkpoint(TestCheckpoint.TEST_DIR)
		self.assertEqual(y.getCheckpoints("b"), [3])
		self.assertEqual(y.getCheckpoints("a"), [1, 2])

if __name__ == "__main__":
	unittest.main()

