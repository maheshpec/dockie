import os

os.environ['TOKENIZERS_PARALLELISM'] = "false"

import argparse
import logging
import sys
import textwrap
import transformers

from ..transformers_patch import PIPELINE_DEFAULTS

try:
    from . import scan
except ModuleNotFoundError as e:
    _module_not_found_error = e

if _module_not_found_error is not None:
    raise ModuleNotFoundError(
        textwrap.dedent(
            f"""\
            At least one dependency not found: {str(_module_not_found_error)!r}
            It is possible that dockie was installed without the CLI dependencies. Run:

              pip install 'dockie[cli]'

            to install impira with the CLI dependencies."""
        )
    )
