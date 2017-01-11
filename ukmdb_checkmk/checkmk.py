#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""UKMDB CLI.

Usage: ukm_ckmk [--help] [--verbose] [--debug ...] <command> [<args>...]

  ukm_ckmk [--debug ...] add_host [--help] <fqdn> [--comment=<comment>] [--set-tags=<tags>] [KEY_VALUE] ...
  ukm_chmk [--debug ...] edit_host [--help] <fqdn> [--comment=<comment>] [--set-tags=<tags> | --add-tags=<tags> | --del-tags=<tags>] [KEY_VALUE] ...
  ukm_chmk [--debug ...] del_host [--help] <fqdn> [--comment=<comment>]

Options:
  -v --verbose             Show more information.
  -d --debug               Show debug information (maybe multiple).

  ukm_cli (-h | --help)
  ukm_cli --version

"""

import logging
from docopt import docopt
from ukmdb_checkmk import __version__
from ukmdb_cli.cmd_base import validate, set_debug_level
from ukmdb_checkmk import ckmk_add_host


def get_mod_version():
    return __version__

ukmdb_log = logging.getLogger("ukmdb")


def main():
    arguments = docopt(__doc__, options_first=True, version=__version__)
    set_debug_level(ukmdb_log, arguments)

    ukmdb_log.debug(u"program 'ukm_ckmk' start")

    if arguments['<command>'] == 'add_host':
        ukmdb_log.debug(u"starting command 'add_host'")
        ckmk_add_host.cmd(validate(docopt(ckmk_add_host.__doc__),
                                   ckmk_add_host.SCHEMA))
# elif arguments['<command>'] == 'mq_info':
#     cmd_mq_info.cmd(validate(docopt(cmd_mq_info.__doc__),
#                              cmd_mq_info.SCHEMA))
