from __future__ import annotations

import importlib
from .. import directory_utils
from .. import namespace_utils


def get_command_spec():
    return {
        'f': lsp_command,
        'help': 'list items inside package namespace',
        'args': [
            {
                'name': 'package_or_module',
                'help': 'package or submodule to list',
                'nargs': '?',
            },
        ],
        'examples': [
            'lsp',
            'lsp numpy',
            'lsp numpy.linalg',
        ],
    }


def lsp_command(package_or_module):
    if package_or_module is None:
        package_name = directory_utils.get_module_of_working_directory()
    else:
        package_name = package_or_module

    package = importlib.import_module(package_name)

    namespace_utils.print_module_summary(package)

