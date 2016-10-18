#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  build for Private Network Origin add-on
#	Copyright (C) 2016 Julien Férard <www.github.com/jferard>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import zipfile
import os

NAME = 'privatenwo'
SOURCE_PATH = os.path.join('..', NAME)
VERSION = '0.0.1b'
EXT = '.xpi'

def main():
    fnames = []
    for root, dirs, files in os.walk(SOURCE_PATH):
        for name in files:
            if not '.git' in root and not name in ['.gitignore', 'HISTORY.md', 'LICENSE', 'README.md']:
                fnames.append(os.path.join(root, name))

    xpi_file = NAME+'-'+VERSION+EXT
    print(xpi_file)
    with zipfile.ZipFile(xpi_file, 'w') as ext_zip:
        for fname in fnames:
            ext_zip.write(fname, fname[len(SOURCE_PATH)+1:])

if __name__ == '__main__':
   main()