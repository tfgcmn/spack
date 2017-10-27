- always (!) set your umask firsd:
  ```
  umask 0222
  ```

- fetch outstanding pull requests, e.g.:
  ```
  git remote add upstream https://github.com/LLNL/spack.git
  git fetch upstream pull/3227/head:PR_filesystemview
  git merge PR_filesystemview
  ```

- unload any modules you may have loaded and load the spack commands:
  ```
  source share/spack/setup-env.sh
  ```

- install visionary-defaults:
  ```
  export TEST_TMPDIR=/tmp # set to a non-NFS filesystem (for bazel)
  spack install 'visionary-defaults@0.2.15^py-pybind11@2.1.1'
  ```
  Note that the version of py-pybind11 has to be specified explicitly since pybind11 2.2.0 fails to
  build with gcc 4.9.2.

- Create a filesystem view:
  ```
  spack view -d yes add -i spackview visionary-defaults
  ```
