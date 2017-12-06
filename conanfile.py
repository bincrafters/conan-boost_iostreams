from conans import ConanFile, tools


class BoostIostreamsConan(ConanFile):
    name = "Boost.Iostreams"
    version = "1.65.1"

    options = {"shared": [True, False], 'use_zlib': [True, False], 'use_bzip2': [True, False]}
    default_options = "shared=False", "use_zlib=True", "use_bzip2=True"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Bind/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Function/1.65.1@bincrafters/testing", \
        "Boost.Integer/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Random/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.Regex/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing"

    def requirements(self):
        if not self.options.shared:
            if self.options.use_bzip2:
                self.requires("bzip2/1.0.6@conan/stable")
            if self.options.use_zlib:
                self.requires("zlib/1.2.11@conan/stable")

    def configure(self):
        if self.options.use_bzip2:
            self.options["bzip"].shared = False
        if self.options.use_zlib:
            self.options["zlib"].shared = False

    lib_short_names = ["iostreams"]
    is_header_only = False

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-iostreams"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
