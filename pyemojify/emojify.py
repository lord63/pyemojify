#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import re

from pyemojify.emoji import emoji_table


def emojify(text):
    emoji_keys = re.findall(r':\S+:', text)
    for emoji_key in emoji_keys:
        raw_emoji = emoji_table.get(emoji_key, emoji_key)
        text = text.replace(emoji_key, raw_emoji)
    return text
