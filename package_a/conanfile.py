from conan import ConanFile

class BasicConanfile(ConanFile):
    name = "package_a"
    version = "1.0"
    description = "A basic recipe"
    license = "<Your project license goes here>"
    homepage = "<Your project homepage goes here>"

    def build(self):
        pass

    def package(self):
        pass
