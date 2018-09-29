#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostIostreamsConan(base.BoostBaseConan):
    name = "boost_iostreams"
    url = "https://github.com/bincrafters/conan-boost_iostreams"
    lib_short_names = ["iostreams"]
    options = {"shared": [True, False], 'use_zlib': [True, False], 'use_bzip2': [True, False], 'use_lzma': [True, False]}
    default_options = "shared=False", "use_zlib=True", "use_bzip2=True", "use_lzma=True"
    b2_defines = ["LZMA_API_STATIC"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_function",
        "boost_integer",
        "boost_iterator",
        "boost_mpl",
        "boost_preprocessor",
        "boost_random",
        "boost_range",
        "boost_regex",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]

    def requirements(self):
        if self.options.use_bzip2:
            self.requires("bzip2/1.0.6@conan/stable")
        if self.options.use_zlib:
            self.requires("zlib/1.2.11@conan/stable")
        if self.options.use_lzma:
            self.requires("lzma/5.2.3@bincrafters/stable")

    def package_info_additional(self):
        if self.options.use_bzip2:
            self.cpp_info.defines.append("CONAN_BOOST_IOSTREAMS_USE_BZIP2=1")
        if self.options.use_zlib:
            self.cpp_info.defines.append("CONAN_BOOST_IOSTREAMS_USE_ZLIB=1")
        if self.options.use_lzma:
            self.cpp_info.defines.append("CONAN_BOOST_IOSTREAMS_USE_LZMA=1")
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_DYN_LINK=1")

