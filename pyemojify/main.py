#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from codecs import open
import json
from os import path
import re

import click

from pyemojify import __version__


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
@click.option('-t', '--text', help="The input text")
def cli(text):
    file_path = path.join(path.abspath(path.dirname(__file__)), 'emoji.json')
    with open(file_path, encoding='utf-8') as f:
        emoji_table = json.load(f)
    if not text:
        text = click.get_text_stream('stdin').read().strip()
    emoji_keys = re.findall(r':\w+:', text)
    for emoji_key in emoji_keys:
        raw_emoji = emoji_table.get(emoji_key, emoji_key)
        text = text.replace(emoji_key, raw_emoji)
    click.echo(text)
