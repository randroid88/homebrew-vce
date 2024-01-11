#!/usr/bin/env python3
import os
import sys

if os.path.dirname(os.path.realpath(__file__)) != os.getcwd():
    # If current working directory is not where the file lives, we should load files from libexec
    LIBEXEC_PATH = os.path.join(os.path.dirname(__file__), "..", "libexec")
    sys.path.insert(0, LIBEXEC_PATH)

if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)) )
    print(os.getcwd())
    command_line_args = sys.argv[1:]
    try:
        import vce_lib
    except ModuleNotFoundError:
        print('\nModuleNotFoundError')
        sys.exit(1)
    except KeyboardInterrupt:
        print('\nProgram interrupted.')
        sys.exit(1)
    else:
        vce_lib.main(command_line_args)