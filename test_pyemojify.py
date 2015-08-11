#!/usr/bin/env python
# -*- coding: utf-8 -*-

from click.testing import CliRunner

from pyemojify.cli import cli


def test_pyemojify():
    runner = CliRunner()
    result_one = runner.invoke(
        cli, ['-t', ':smile: :+1: :100: :smile: :clock12:'])
    result_two = runner.invoke(
        cli,
        ['-t', 'Life is short :smile: , use :sparkles: Python :sparkles:'])
    assert result_one.output == u'😄 👍 💯 😄 🕛\n'
    assert result_two.output == u'Life is short 😄 , use ✨ Python ✨\n'
