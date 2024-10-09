# Copyright 2023-2024 DreamWorks Animation LLC and Intel Corporation
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
import sys

name = 'arras4_node'

@early()
def version():
    """
    Increment the build in the version.
    """
    _version = '4.7.1'
    from rezbuild import earlybind
    return earlybind.version(this, _version)

description = 'Arras package'

authors = ['Dreamworks Animation R&D - JoSE Team',
           'psw-jose@dreamworks.com']

help = ('For assistance, '
        "please contact the folio's owner at: psw-jose@dreamworks.com")

variants = [
    ['os-CentOS-7', 'refplat-vfx2021.0'],
    ['os-CentOS-7', 'refplat-vfx2022.0'],
    ['os-rocky-9', 'refplat-vfx2021.0'],
    ['os-rocky-9', 'refplat-vfx2022.0'],
    ['os-rocky-9', 'refplat-vfx2023.1'],
]

requires = [
    'arras4_core-4.10'
]

private_build_requires = [
    'cmake_modules-1.0',
    'gcc-9.3.x|11.x'
]

def commands():
    prependenv('PATH', '{root}/bin:{root}/sbin')
    prependenv('LD_LIBRARY_PATH', '{root}/lib')


uuid = '2798ce16-36b2-46a7-80ac-7d90994706d'

config_version = 0
