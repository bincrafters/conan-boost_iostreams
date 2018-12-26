#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostIostreamsConan(base.BoostBaseConan):
    name = "boost_iostreams"
    url = "https://github.com/bincrafters/conan-boost_iostreams"
    lib_short_names = ["iostreams"]
    cycle_group = "boost_cycle_group_c"
    options = {
        "shared": [True, False],
        "use_bzip2": [True, False],
        "use_lzma": [True, False],
        "use_zlib": [True, False],
        "use_zstd": [True, False]
    }
    default_options = "shared=False", "use_bzip2=True", "use_lzma=True", "use_zlib=True", "use_zstd=True"
    b2_requires = ["boost_cycle_group_c"]
