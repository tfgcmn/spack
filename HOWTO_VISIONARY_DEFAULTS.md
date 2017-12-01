- note that you have to build on a machine whose instruction set is
  common to all machines the software will be used on.  in our case
  that likely is one of the older cluster nodes, i.e. AMTHostN.
  (passing `-march` and `-mtune` flags did not work reliably)

- always (!) set your umask first:
  ```
  umask 0002
  ```

- set up the repository
  ```
  git init --shared=all
  git remote add origin https://github.com/electronicvisions/spack
  git checkout 2017-12-01
  ```

- unload any modules you may have loaded:
  ```
  module purge
  ```

- load the spack commands:
  ```
  source share/spack/setup-env.sh
  ```

- install a newer compiler:
  ```
  spack fetch --dependencies gcc@7.2.0
  srun --pty --mem 14G -N1 -c8 -p compile spack install gcc@7.2.0 %gcc@4.9.2
  ```

- activate compiler:

- install visionary-defaults:
  ```
  srun --pty --mem 14G -N1 -c8 -p compile spack install visionary-defaults
  ```

- Create a filesystem view:
  ```
  spack view -d yes hardlink -i spackview visionary-defaults
  ```
