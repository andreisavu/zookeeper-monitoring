#! /usr/bin/env python
""" Check Zookeeper Cluster

Generic monitoring script that could be used with multiple platforms.
"""

import sys

from optparse import OptionParser

def main():
    opts, args = parse_cli()

    # find the leader
    
    # send the "mntr" command and read output

    # parse output and get only the specified key

    # select formatter and output

def parse_cli():
    parser = OptionParser()

    parser.add_option('-s', '--servers', dest='servers', 
        help='a list of SERVERS', metavar='SERVERS')

    parser.add_option('-k', '--key', dest='key', 
        help='what KEY to analyze', metavar='KEY')

    parser.add_option('-t', '--target', dest='target', 
        help='target platform', metavar='TARGET')

    parser.add_option('-w', '--warning', dest='warning', 
        help='WARNING level', metavar='WARNING')

    parser.add_option('-c', '--critical', dest='critical',
        help='CRITICAL level', metavar='CRITICAL')

    return parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())

