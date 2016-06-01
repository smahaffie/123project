import os
import sys
from multiprocessing import Pool


"""
THIS FILE WRITES THE INSTRUCTIONS FOR SETTING UP MULTIPLE
"""


SPRINGSPATH = "springs.py"
PEMPATH = "~/laptop.pem"
NO_STRICT_KEY = "-o StrictHostKeyChecking no"


IP_DNS_LIST = [
                ('172.31.48.191', 'ec2-52-90-136-20.compute-1.amazonaws.com'), # main
                ('172.31.48.189', 'ec2-54-85-253-140.compute-1.amazonaws.com'),
                ('172.31.48.192', 'ec2-54-89-105-133.compute-1.amazonaws.com'),
                ('172.31.48.190', 'ec2-54-174-186-93.compute-1.amazonaws.com'),
                ('172.31.48.187', 'ec2-54-175-177-251.compute-1.amazonaws.com'),
                ('172.31.48.188', 'ec2-54-175-234-57.compute-1.amazonaws.com'),
            ]

