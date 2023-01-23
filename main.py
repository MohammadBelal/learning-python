#!/usr/bin/env python3
# pylint: disable=missing-module-docstring

__author__ = "Muhammad Bilal"
__version__ = "0.1.0"

import boto3

s3 =  boto3.resource('s3')

def main():
    """ Main entry point of the app """
    print("hello world")

main()
