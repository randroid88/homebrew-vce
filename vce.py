#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    try:
        import vce_lib

        args = sys.argv[1:]
        vce_lib.main(args)
    except KeyboardInterrupt:
        print('\n Program interrupted.')
        sys.exit(1)
