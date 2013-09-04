#!/usr/bin/python

import unittest
import os
import os.path as path

from checkpoint import Checkpoint

class TestCheckpoint(unittest.TestCase):
	TEST_DIR = "/tmp/checkpoint_test"
	TEST_KEY = "test_key"

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

if __name__ == "__main__":
	unittest.main()

