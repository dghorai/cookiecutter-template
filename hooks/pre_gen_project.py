#!/usr/bin/env python


"""
Code to run before generating the project.

References/Adapted from:
1) https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py
2) https://github.com/cthoyt/cookiecutter-snekpack/blob/main/hooks/pre_gen_project.py

"""

import sys
import re

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_name }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: {module_name} is not a valid Python module name. Please do not use a - and use _ instead.')
    sys.exit(1)
