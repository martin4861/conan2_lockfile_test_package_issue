from conan import ConanFile

class BasicConanfile(ConanFile):
    name = "package_b"
    version = "1.0"
    description = "A basic recipe"
    license = "<Your project license goes here>"
    homepage = "<Your project homepage goes here>"

    def requirements(self):
        # this would depend on some packages using version ranges.

    def build(self):
        pass

    def package(self):
        pass
