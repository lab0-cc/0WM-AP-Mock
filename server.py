#!/usr/bin/env python3

"""This module implements a simple mock AP server"""

from http.server import HTTPServer, SimpleHTTPRequestHandler, test
from sys import argv
from time import sleep

class Handler(SimpleHTTPRequestHandler):
    """This class injects headers in HTTP responses"""
    def end_headers(self):
        sleep(1)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    test(Handler, HTTPServer, port=int(argv[1]) if len(argv) > 1 else 8000)
