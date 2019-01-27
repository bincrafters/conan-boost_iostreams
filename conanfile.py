#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostIostreamsConan(base.BoostBaseConan):
    name = "boost_iostreams"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_iostreams"
    lib_short_names = ["iostreams"]
    cycle_group = "boost_cycle_group_c"
    options = {
        "shared": [True, False],
        "use_bzip2": [True, False],
        "use_lzma": [True, False],
        "use_zlib": [True, False]
    }
    default_options = "shared=False", "use_bzip2=True", "use_lzma=True", "use_zlib=True"
    b2_defines = ["LZMA_API_STATIC"]
    b2_requires = ["boost_cycle_group_c"]

    def requirements_additional(self):
        if self.options.use_bzip2:
            self.requires("bzip2/1.0.6@conan/stable")
        if self.options.use_zlib:
            self.requires("zlib/1.2.11@conan/stable")
        if self.options.use_lzma:
            self.requires("lzma/5.2.4@bincrafters/stable")

    def package_info_additional(self):
        if self.options.use_bzip2:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_BZIP2=1")
        if self.options.use_zlib:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_ZLIB=1")
        if self.options.use_lzma:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_LZMA=1")
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_DYN_LINK=1")
