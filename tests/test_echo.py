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
            ["python", "./echo.py", "-u", "test"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals("TEST", stdout.strip())

    def test_lower_option_parser_output(self):
        """ Parsing '-l' or '--lower' should store "lower" in namespace """
        parser = echo.create_parser()
        args = parser.parse_args(['echo.py', '-l'])
        self.assertTrue(args.lower)

    def test_lower_case_output(self):
        """ Running the program with '-l' or '--lower' 
            output lower case text 
        """
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "TEST"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals("test", stdout.strip())

    def test_title_option_parser_output(self):
        """ Parsing '-t' or '--title' should store "title" in namespace """
        parser = echo.create_parser()
        args = parser.parse_args(['echo.py', '-t'])
        self.assertTrue(args.title)

    def test_title_case_output(self):
        """ Running the program with '-t' or '--title' 
            output Title case Text 
        """
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "test", "this"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals("Test This", stdout.strip())


if __name__ == '__main__':
    unittest.main()
