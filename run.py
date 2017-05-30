"""run
This module is a simple script to run some dummy python unit tests. 
It is used just for testing/debugging different things in a Jenkins/Travis CI
pipeline. This script (rthar this git repo) is just an enabler for the following:
1. Test if you can connect to this github.ibm from Jenkins dashboard
2. Use github 'certificates' (not the ssh key pair to connect to github.ibm from
  IBM network and clone this repo
3. Test .travis.yml implementation (needs travis yml Jenkins plugin)
4. Automatically publish build status as git-notes (need git-notes Jenkins plugin)
5. Automatically publish build failures by creating a new github.ibm issue. 
The code is compatible with Python 3.5.x.
Author: Ninad Sathaye
:copyright 2017 IBM
"""

# Script to be run by the Jenkins/Travis CI. 
# Used to debug/test CI pipeline


import os
import unittest

class MyTest(unittest.TestCase):    
    def setUp(self):        
        self.val = 10
        print("\nIn setUp, Running tests for run.py")
        print ("..with self.val=",self.val)
   
     
        
    def test_this_should_pass(self):
        print("Running test_this_should_pass...")
        self.assertTrue(self.val == 10)
    
    @unittest.skip("Skipping a known failure .. test_this_should_fail")
    def test_this_should_fail(self):
        print("Running test_this_should_fail...")
        self.assertFalse(self.val == 10)

if __name__ == '__main__':   
   unittest.main()
