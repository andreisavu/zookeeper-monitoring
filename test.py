#! /usr/bin/env python

import unittest

from check_zookeeper import ZooKeeperServer

ZK_MNTR_OUTPUT = """zk_version\t3.4.0--1, built on 06/19/2010 15:07 GMT
zk_avg_latency\t1
zk_max_latency\t132
zk_min_latency\t0
zk_packets_received\t640
zk_packets_sent\t639
zk_outstanding_requests\t0
zk_server_state\tfollower
zk_znode_count\t4
zk_watch_count\t0
zk_ephemerals_count\t0
zk_approximate_data_size\t27
zk_open_file_descriptor_count\t22
zk_max_file_descriptor_count\t1024
"""

ZK_MNTR_OUTPUT_WITH_BROKEN_LINES = """zk_version\t3.4.0
zk_avg_latency\t23
broken-line

"""

class TestCheckZookeeper(unittest.TestCase):

    def setUp(self):
        self.zk = ZooKeeperServer()
    
    def test_parse_valid_line(self):
        key, value = self.zk._parse_line('something\t5')

        self.assertEqual(key, 'something')
        self.assertEqual(value, 5)

    def test_parse_line_raises_exception_on_invalid_output(self):
        invalid_lines = ['something', '', 'a\tb\tc', '\t1']
        for line in invalid_lines:
            self.assertRaises(ValueError, self.zk._parse_line, line)

    def test_parser_on_valid_output(self):
        data = self.zk._parse(ZK_MNTR_OUTPUT)

        self.assertEqual(len(data), 14)
        self.assertEqual(data['zk_znode_count'], 4)
        
    def test_parse_should_ignore_invalid_lines(self):
        data = self.zk._parse(ZK_MNTR_OUTPUT_WITH_BROKEN_LINES)

        self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()

