#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo

# Your test case class goes here


class EchoTest(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
