#! /bin/bash
set -Eeuo pipefail

conan create package_a
conan lock create package_b

# fails with
# ERROR: Requirement 'package_a/1.0' not in lockfile 'requires'
conan create package_b
