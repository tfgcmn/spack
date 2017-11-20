- note that you have to build on a machine whose instruction set is
  common to all machines the software will be used on.  in our case
  that likely is one of the older cluster nodes, i.e. AMTHostN.
  (passing `-march` and `-mtune` flags did not work reliably)

- always (!) set your umask first:
  ```
  umask 0002
  ```

- fetch outstanding pull requests, e.g.:
  ```
  git remote add upstream https://github.com/LLNL/spack.git
  git fetch upstream pull/3227/head:PR_filesystemview
  git merge PR_filesystemview
  ```

- unload any modules you may have loaded:
  ```
  module purge
  ```

- load the spack commands:
  ```
  source share/spack/setup-env.sh
  ```

- install visionary-defaults:
  ```
  export TEST_TMPDIR=/tmp # set to a non-NFS filesystem (for bazel)
  spack install visionary-defaults
  ```

- Create a filesystem view:
  ```
  spack view -d yes hardlink -i spackview visionary-defaults
  ```
