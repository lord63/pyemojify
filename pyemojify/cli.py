#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from pyemojify import __version__
from pyemojify.emojify import emojify


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
@click.option('-t', '--text', help="The input text")
def cli(text):
    if not text:
        text = click.get_text_stream('stdin').read().strip()
    emoji_text = emojify(text)
    click.echo(emoji_text)
