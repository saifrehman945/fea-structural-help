# apex.compute

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.compute.DeleteScratchFiles`: `Yes`, `No`, `Min`, `Post`
  - To handle scratch files after complete

`apex.compute.MemorymaxMethod`: `Fraction`, `User`
  - Of Max Memory definition method

`apex.compute.NastranMemoryAllocationMethod`: `Estimate`, `Max`, `User`
  - Which method will be used to define how much memory Nastran allocates for jobs. Three options are provided, estimate - will cause Nastran to choose how much memory should be allocated for the job max - will cause Nastran to allocate the maximum of amount of memory configured for this compute environment (see the 'memorymax' seeting) user - the user must specify how much memory to use

`apex.compute.SolverExecutionPreference`: `Auto`, `Manual`
  - Of solver execution preference method

`apex.compute.SolverType`: `Local`, `Remote`
  - Solver type to define if the simulation runs in local or remote machine. If "Local" is selected, the simulation will be run locally. If "Remote" is selected, the simulation will send and run on remote machine

## Module functions

### `apex.compute.executeGenDes(scenario: apex.studies.Scenario, computeEnvironmentGenDes: apex.compute.ComputeEnvironmentGenDes = None) -> None`
Executes the input Apex Generative Design Scenario on a Generative Design compute resource. The Generative Design compute resource must have been previously configured.

### `apex.compute.getGenDesComputeEnvironment() -> apex.compute.ComputeEnvironmentGenDes`

Returns: Returns the active solver in Generative Design compute Environment.It can be a LocalSolver or RemoteSolver.

### `apex.compute.setGenDesComputeEnvironment(target: apex.compute.ComputeEnvironmentGenDes) -> None`
Sets the Generative Design Compute Environment to as default one.

### `apex.compute.setNatranComputeEnvironment(target: apex.compute.ComputeEnvironment) -> None`
Sets the default Nastran Compute Environment.

## Classes in this module

Full method signatures are in `api/classes/apex.compute.md`.

`ComputeEnvironment`, `ComputeEnvironmentGenDes`, `ComputeEnvironmentNastran`, `ComputeEnvironmentNastranExternal`, `ComputeEnvironmentNastranIntegrated`, `LocalSolver`, `RemoteSolver`, `RemoteSolverGroup`

