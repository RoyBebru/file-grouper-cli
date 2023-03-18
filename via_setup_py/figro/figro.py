# -*- coding: utf-8 -*-

"""
File Grouper (CLI)
Author: Dmytro Tarasiuk
"""

import os
import sys

from figro.common import init
init() # is called only here one time

import figro.core as core

def main():
    core.parse_options()

    if core.is_any_to_do():
        core.do_everything()
    else:
        core.print_usage()

if __name__ == "__main__":
    main()
