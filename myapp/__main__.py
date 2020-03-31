import sys

from .cli import cli

cli(sys.argv[1:], prog_name='myapp', auto_envvar_prefix='MYAPP')
