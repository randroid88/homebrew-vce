#!/usr/bin/env python3
import os
import sys
from contextlib import contextmanager

PATH_INDEX = 0
LOCAL_MODULE_PATH = './'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "libexec"))


@contextmanager
def extend_sys_path(path):
    sys.path.insert(PATH_INDEX, path)
    try:
        yield
    finally:
        sys.path.pop(PATH_INDEX)


if __name__ == '__main__':
    command_line_args = sys.argv[1:]
    try:
        with extend_sys_path(LOCAL_MODULE_PATH):
            import vce_lib
    except ModuleNotFoundError:
        import vce_lib

        print('\nModuleNotFoundError')
    except KeyboardInterrupt:
        print('\nProgram interrupted.')
        sys.exit(1)
    else:
        vce_lib.main(command_line_args)
