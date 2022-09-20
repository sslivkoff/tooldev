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
            {
                'name': ('--modules', '-m'),
                'help': 'display modules and hide other sections',
                'action': 'store_true',
            },
            {
                'name': ('--functions', '-f'),
                'help': 'display functions and hide other sections',
                'action': 'store_true',
            },
            {
                'name': ('--classes', '-c'),
                'help': 'display functions and hide other sections',
                'action': 'store_true',
            },
            {
                'name': ('--dunder', '-d'),
                'help': 'display dunder and hide other sections',
                'action': 'store_true',
            },
            {
                'name': ('--other', '-o'),
                'help': 'display other section and hide other sections',
                'action': 'store_true',
            },
        ],
        'examples': [
            '',
            'numpy',
            'numpy.linalg',
            'numpy.linalg -f -c',
        ],
    }


def lsp_command(
    package_or_module: str,
    modules: bool,
    functions: bool,
    classes: bool,
    dunder: bool,
    other: bool,
) -> None:

    if package_or_module is None:
        package_name = directory_utils.get_module_of_working_directory()
    else:
        package_name = package_or_module

    package = importlib.import_module(package_name)

    if modules or functions or classes or dunder or other:
        raw_sections = [
            ['title', True],
            ['internal_modules', modules],
            ['external_modules', modules],
            ['functions', functions],
            ['dunder', dunder],
            ['other', other],
        ]
        sections = [name for name, value in raw_sections if value]
    else:
        sections = None
    namespace_utils.print_module_summary(package, sections=sections)
