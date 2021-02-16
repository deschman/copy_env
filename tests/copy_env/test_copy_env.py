# -*- coding: utf-8 -*-

# %% Imports
# %%% Py3 Standard
import os
import sys

# %%% 3rd Party
import pytest

# %%% User-Defined
from copy_env.copy_env import copy_env


# %% Variables
pytest_plugins = ['pytest_virtualenv']
package_location = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
source_python_dir = os.path.dirname(sys.executable)


# %% Functions
def test_copy_env(virtualenv) -> None:
    virtualenv.run('cd ' + virtualenv.python)
    virtualenv.run('python {0}.__init__.py -s {1}'.format(
        package_location, source_python_dir))
    try:
        with open(os.path.join(source_python_dir, '_requirements.txt'),
                  'r') as file:
            source_requirements = file.read().split('\n')
        missing_requirements = list(set(source_requirements) -
                                    set(virtualenv.installed_packages()))
        if len(missing_requirements) != 0:
            print(str(missing_requirements)[1:-1] +
                  " may not have installed correctly")
        assert len(missing_requirements) == 0
    except Exception:
        assert False


def test_copy_env_copy_env(virtualenv) -> None:
    copy_env(source_python_dir, os.path.dirname(virtualenv.python))
    try:
        with open(os.path.join(source_python_dir, '_requirements.txt'),
                  'r') as file:
            source_requirements = file.read().split('\n')
        missing_requirements = list(set(source_requirements) -
                                    set(virtualenv.installed_packages()))
        if len(missing_requirements) != 0:
            print(str(missing_requirements)[1:-1] +
                  " may not have installed correctly")
        assert len(missing_requirements) == 0
    except Exception:
        assert False
