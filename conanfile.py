from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os


class LibaioConan(ConanFile):
    name = "libaio"
    version = "0.3.111"
    description = "The Linux-native asynchronous I/O facility"
    topics = ("conan", "libaio", "linux", "asynchronous", "io", )
    url = "https://github.com/bincrafters/conan-libaio"
    homepage = "https://pagure.io/libaio"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "LGPL-2.1"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd
        if self.settings.os != 'Linux':
            raise ConanInvalidConfiguration("libaio is only designed for Linux.")

    def source(self):
        sha256 = "1e7c9f70fb1dacd685affa1989fed44519f6b60b5d7b73d70960f5d9e88a3a99"
        tools.get("{0}/archive/libaio-{1}/libaio-libaio-{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
