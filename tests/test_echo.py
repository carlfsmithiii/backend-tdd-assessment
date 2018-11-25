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

    def test_upper_option_parser_output(self):
        """ Parsing '-u' or '--upper' should store "upper" in namespace """
        parser = echo.create_parser()
        args = parser.parse_args(['echo.py', '-u'])
        self.assertTrue(args.upper)

    def test_upper_case_output(self):
        """ Running the program with '-u' or '--upper' 
            output UPPER case text 
        """
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", " ", "test"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertIn("TEST", stdout)


if __name__ == '__main__':
    unittest.main()
