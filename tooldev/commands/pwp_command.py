from __future__ import annotations

from .. import directory_utils


def get_command_spec():
    return {
        'f': pwp_command,
        'help': 'print package or module corresponding to working directory',
    }


def pwp_command():
    module = directory_utils.get_module_of_working_directory()
    print(module)
