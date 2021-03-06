#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer Application Framework
# ============================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(name="isomer-library",
      version="0.0.1",
      description="isomer-library - a federated small library management system",
      author="Isomer Community",
      author_email="riot@c-base.org",
      url="https://github.com/isomeric/isomer-library",
      license="GNU Affero General Public License v3",
      packages=find_packages(),
      long_description="""Isomer - Library
================

A modern, opensource approach to library management.

This software package is a plugin module for Isomer.
""",
      install_requires=[
          'isomer>=1.0.0',
          'isbntools>=4.3.3',
          'isbnlib>=3.6.6'
      ],
      entry_points="""[isomer.components]
    library=isomer.library.manager:Manager
[isomer.schemata]
    book=isomer.library.book:Book
    """,
      test_suite="tests.main.main",
      )
