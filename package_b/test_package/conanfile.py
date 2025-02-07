from conan import ConanFile

class TestBasicConanfile(ConanFile):
    name = "test_package_b"
    version = "1.0"
    description = "A basic recipe"
    license = "<Your project license goes here>"
    homepage = "<Your project homepage goes here>"

    def requirements(self):
        self.requires(self.tested_reference_str)
        self.requires("package_a/1.0")

    def build(self):
        pass

    def test(self):
        pass
