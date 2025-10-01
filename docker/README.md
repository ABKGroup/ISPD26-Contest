# ISPD26 Contest: Containers and Submission Information

## Container

The intention of this container is to provide a consistent interactive environment for development and evaluation. It is based on Ubuntu 24.04 and contains:
- OpenROAD - Binary installation with sources at `/OpenROAD` (Commit `2976317355a8370ad56605ce95cbe7a9afdf18e4`)
    - This version is patched to support the [evaluator](../scripts/evaluation.tcl), see [`ord.patch`](ord.patch) if you wish to build your own version.
- OpenROAD-Flow-Scripts (commit `66e441c6cbb6cb9ac871726fc8373317f164ed84`)
- Conda 25.7.0 (Miniconda)
- Miscellaneous tools including Yosys.

See the [Dockerfile here](./dockerfile). A precompiled image can be retrieved from the Docker Hub [`udxs/ispd26:v1`](https://hub.docker.com/repository/docker/udxs/ispd26/tags/v1/sha256-cb27311078045ffe6849dc31a488a48230efce6bd5ead215e21a6dd755f810c3). This image is also compatbile with Apptainer (formerly Singularity) - see below.

### Using Apptainer (Singularity)

For users with supercomputing environments, including contestants granted access to the Purdue Anvil system, it is possible to use Apptainer/Singularity instead of Docker. Unlike Docker, Apptainer (in `fakeroot` mode) will make your container directories read-only.

Thus, to support package installation, you need to create a writable "overlay" layer first, where Apptainer will store all changes. The process to do this and run the container is as follows:
```sh
# You only need to do this once but may create multiple overlays to represent multiple isolated instances.
# This example creates a 20 GB overlay but you may change this amount.
singularity overlay create --fakeroot -S -s 20480 my_overlay.img 

# For CPU only operation
singularity run -o my_overlay.img --fakeroot docker://udxs/ispd26:v1
# For CUDA-capable NVIDIA GPUs:
singularity run -o my_overlay.img --fakeroot --nv docker://udxs/ispd26:v1
```


## Submission Formatting 

 When you prepare your submission, you will be required to submit a ZIP file containing:
- A `setup.sh` that installs all necessary dependencies (incl. the ability to use `apt` and `pip`)
- A `run.sh` that will run your application. This should use the same environment variables as defined in [`evaluation.tcl`](../scripts/evaluation.tcl) to produce the required `<design_name>.def`, `<design_name>.v` and `<design_name>.changelist` into the directory referenced by the environment variable `OUTPUT_DIR`.
- Any necessary data or code that is not already retrieved in your `setup.sh`.

This will be extracted within the container and executed when it comes time to official evaluation. Please thus ensure that your submission works in a fresh Docker or Apptainer/Singularity container when extracted to *any* location. 


