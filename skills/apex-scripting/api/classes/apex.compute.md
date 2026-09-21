# apex.compute — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.compute.ComputeEnvironment`
A class used to define the compute environment for Generative design. A base class for all solver specific compute environments.
Properties: `activeComputeEnvironmentNastran`

Methods:

- `addComputeEnvironmentNastran(target: apex.compute.ComputeEnvironmentNastran) -> apex.compute.ComputeEnvironmentNastran` — add a Nastran compute environment
- `exportComputeEnvironmentNastran(filename: str) -> None` — export all ComputeEnvironmentNastran settings to XML file
- `exportEnv(filename: str) -> None`
- `getActiveComputeEnvironmentNastran() -> apex.compute.ComputeEnvironmentNastran` — the active compute environment for Nastran
- `getComputeEnvironmentNastran(name: str) -> apex.compute.ComputeEnvironmentNastran` — returns a Nastran compute environment
- `getComputeEnvironmentsNastran() -> [apex.compute.ComputeEnvironmentNastran]` — returns a list of Nastran compute environment
- `getDescription() -> str` — a description for this ComputeEnvironment
- `getName() -> str` — a name to identify this ComputeEnvironment
- `importComputeEnvironmentNastran(filename: str) -> apex.compute.ComputeEnvironmentNastran` — import all ComputeEnvironmentNastran settings form existing XML file
- `removeComputeEnvironmentNastran(target: apex.compute.ComputeEnvironmentNastran) -> None` — remove a Nastran compute environment
- `setActiveComputeEnvironmentNastran(activeComputeEnvironmentNastran: apex.compute.ComputeEnvironmentNastran) -> None` — the active compute environment for Nastran
- `setDescription(description: str) -> None` — a description for this ComputeEnvironment
- `setName(name: str) -> None` — a name to identify this ComputeEnvironment

## `apex.compute.ComputeEnvironmentGenDes`  (extends `ComputeEnvironment`)
A class used to define the compute environment for Generative design.
Properties: `solverType`

Methods:

- `asLocalSolver() -> apex.compute.LocalSolver`
- `asRemoteSolver() -> apex.compute.RemoteSolver`
- `asRemoteSolverGroup() -> apex.compute.RemoteSolverGroup`
- `getSolverType() -> SolverType` — the property that controls whether Local or Remote solver to be used.

## `apex.compute.ComputeEnvironmentNastran`
A base class used to define the compute environment for Nastran.
Properties: `activeExternalSolver`, `computeEnvironmentNastranExternal`, `computeEnvironmentNastranIntegrated`, `name`

Methods:

#### `ComputeEnvironmentNastran(computeEnvironmentNastranExternal: apex.compute.ComputeEnvironmentNastranExternal, computeEnvironmentNastranIntegrated: apex.compute.ComputeEnvironmentNastranIntegrated, name: str, activeExternalSolver: bool = False) -> None`
Constructor for the nastran compute environment.

- `computeEnvironmentNastranExternal` — External Nastran ComputeEnvironment
- `computeEnvironmentNastranIntegrated` — Integrated Nastran ComputeEnvironment
- `name` — Name of the compute environment
- `activeExternalSolver` — Active External Nastran solver. The default is false, which use integrated solver to run simulation. If it is false,ComputeEnvironmentNastranIntegrated will be used; if it is true,ComputeEnvironmentNastranExternal will be used.

- `getActiveExternalSolver() -> bool` — Active External Nastran solver. The default is false, which use integrated solver to run simulation. If it is false,ComputeEnvironmentNastranIntegrated will be used; if it is true,ComputeEnvironmentNastranExternal will be used.
- `getComputeEnvironmentNastranExternal() -> apex.compute.ComputeEnvironmentNastranExternal` — External Nastran ComputeEnvironment.
- `getComputeEnvironmentNastranIntegrated() -> apex.compute.ComputeEnvironmentNastranIntegrated` — Integrated Nastran ComputeEnvironment.
- `getName() -> str` — Name of the compute environment.
- `thisSPtr() -> apex.compute.ComputeEnvironmentNastran`
- `~ComputeEnvironmentNastran() -> None`

## `apex.compute.ComputeEnvironmentNastranExternal`
A class used to define the compute environment for Nastran.
Properties: `bufferpool`, `buffersize`, `cputhreads`, `deleteScratchOnCompletion`, `fxphysical`, `inputFileFolder`, `memory`, `memoryAllocationMethod`, `memorymax`, `memorymaxMethod`, `resultFileFolder`, `scratchFileFolder`, `solverExecutionPreference`, `solverPath`

Methods:

#### `ComputeEnvironmentNastranExternal(solverPath: str, inputFileFolder: str, scratchFileFolder: str, resultFileFolder: str, buffersize: int, bufferpool: float, memorymax: float = 16 GB, fxphysical: float = 0.75f, memory: float = 12 GB, cputhreads: int = 4, deleteScratchOnCompletion: apex.compute.DeleteScratchFiles = apex.compute.DeleteScratchFiles.Yes, solverExecutionPreference: apex.compute.SolverExecutionPreference = apex.compute.SolverExecutionPreference.Auto, memorymaxMethod: apex.compute.MemorymaxMethod = apex.compute.MemorymaxMethod.Fraction, memoryAllocationMethod: apex.compute.NastranMemoryAllocationMethod = apex.compute.NastranMemoryAllocationMethod.Max) -> None`
constructor for the compute environment.

- `solverPath` — fully qualified path to the Nastran installation folder.For example r"D:\MSC\Software\Nastran\2022.1\bin\nastranw.exe"
- `inputFileFolder` — the fully qualified pathname of the folder where the Nastran input file(s) will be written
- `scratchFileFolder` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written
- `resultFileFolder` — the fully qualified pathname of the folder where the Nastran result file(s) will be written. If omits, the system will generate the result files in the input file folder.
- `buffersize` — represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `bufferpool` — represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `memorymax` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. This setting defines an upper limit for other memory settings in this compute environment. 1.If the associated "memory" setting is set to "Automatic", Nastran will estimate the optimal amount of memory required to solve each job. If the estimated memory requirement exceeds the value of memorymax defined here, Nastran will limit memory usage to the value defined here 2.If the associated "memory" setting is set to "Manual" and a memory size greater than the value of memorymax defined here is specified, Nastran will limit memory usage to the value defined here maxMemory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system.It is only required when MemoryMaxMethod = User.
- `fxphysical` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.
- `memory` — the amount of memory that will be allocated to Nastran for solution of jobs. memory is only required when memoryAllocationMehod is set to apex.compute.NastranMemoryAllocationMethod.User and is silently ignored in all other cases. memory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `cputhreads` — Define the cpu threads to be used in simulation.
- `deleteScratchOnCompletion` — Status of Scratch files on completion.
- `solverExecutionPreference` — Preference to set solver/parallel/memory. If SolverExecutionPreferenc = Auto, Nastran will automatically select the solver/parallel/memory. It is not required the setting of memorymax, memory, cupthreads, buffersize, bufferpool. If SolverExecutionPreferenc = Manual, user can configure the setting of memorymax, memory, cupthreads, buffersize, bufferpool.
- `memorymaxMethod` — Max memory definition method.
- `memoryAllocationMethod` — enumeration specifying the method that will be used to allocate memory to Nastran for solution of jobs. Setting this value to apex.compute.NastranMemoryAllocationMethod.Estimate will cause Nastran to determine an optimal memory allocation based on examination of the job, limited only by the value of memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.Max will cause Nastran to allocate memory for each job equal to the value defined for memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.User requires that a value be assigned to memory and that memory value will be used

- `getBufferpool() -> float` — bufferpool represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `getBuffersize() -> int` — buffersize represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `getCputhreads() -> int` — Define the cpu threads to be used in simulation.
- `getDeleteScratchOnCompletion() -> apex.compute.DeleteScratchFiles` — Status of Scratch files on completion.
- `getFxphysical() -> float` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.
- `getInputFileFolder() -> str` — the fully qualified pathname of the folder where the Nastran input file(s) will be written
- `getMemory() -> float` — the amount of memory that will be allocated to Nastran for solution of jobs. memory is only required when memoryAllocationMehod is set to apex.compute.NastranMemoryAllocationMethod.User and is silently ignored in all other cases. memory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `getMemoryAllocationMethod() -> apex.compute.NastranMemoryAllocationMethod` — enumeration specifying the method that will be used to allocate memory to Nastran for solution of jobs. Setting this value to apex.compute.NastranMemoryAllocationMethod.Estimate will cause Nastran to determine an optimal memory allocation based on examination of the job, limited only by the value of memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.Max will cause Nastran to allocate memory for each job equal to the value defined for memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.User requires that a value be assigned to memory and that memory value will be used
- `getMemorymax() -> float` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. This setting defines an upper limit for other memory settings in this compute environment. 1.If the associated "memory" setting is set to "Automatic", Nastran will estimate the optimal amount of memory required to solve each job. If the estimated memory requirement exceeds the value of memorymax defined here, Nastran will limit memory usage to the value defined here 2.If the associated "memory" setting is set to "Manual" and a memory size greater than the value of memorymax defined here is specified, Nastran will limit memory usage to the value defined here maxMemory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system.It is only required when MemoryMaxMethod = User.
- `getMemorymaxMethod() -> apex.compute.MemorymaxMethod` — Max memory definition method.
- `getResultFileFolder() -> str` — the fully qualified pathname of the folder where the Nastran result file(s) will be written. If omits, the system will generate the result files in the input file folder.
- `getScratchFileFolder() -> str` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written
- `getSolverExecutionPreference() -> apex.compute.SolverExecutionPreference` — Preference to set solver/parallel/memory. If SolverExecutionPreferenc = Auto, Nastran will automatically select the solver/parallel/memory. It is not required the setting of memorymax, memory, cupthreads, buffersize, bufferpool. If SolverExecutionPreferenc = Manual, user can configure the setting of memorymax, memory, cupthreads, buffersize, bufferpool.
- `getSolverPath() -> str` — fully qualified path to the Nastran installation folder.For example r"D:\MSC\Software\Nastran\2022.1\bin\nastranw.exe"
- `setBufferpool(bufferpool: float) -> None` — bufferpool represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `setBuffersize(buffersize: int) -> None` — buffersize represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `setCputhreads(cputhreads: int) -> None` — Define the cpu threads to be used in simulation.
- `setDeleteScratchOnCompletion(deleteScratchOnCompletion: apex.compute.DeleteScratchFiles) -> None` — Status of Scratch files on completion.
- `setFxphysical(fxphysical: float) -> None` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.
- `setInputFileFolder(inputFileFolder: str) -> None` — the fully qualified pathname of the folder where the Nastran input file(s) will be written
- `setMemory(memory: float) -> None` — the amount of memory that will be allocated to Nastran for solution of jobs. memory is only required when memoryAllocationMehod is set to apex.compute.NastranMemoryAllocationMethod.User and is silently ignored in all other cases. memory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system
- `setMemoryAllocationMethod(memoryAllocationMethod: apex.compute.NastranMemoryAllocationMethod) -> None` — enumeration specifying the method that will be used to allocate memory to Nastran for solution of jobs. Setting this value to apex.compute.NastranMemoryAllocationMethod.Estimate will cause Nastran to determine an optimal memory allocation based on examination of the job, limited only by the value of memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.Max will cause Nastran to allocate memory for each job equal to the value defined for memorymax Setting this value to apex.compute.NastranMemoryAllocationMethod.User requires that a value be assigned to memory and that memory value will be used
- `setMemorymax(memorymax: float) -> None` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. This setting defines an upper limit for other memory settings in this compute environment. 1.If the associated "memory" setting is set to "Automatic", Nastran will estimate the optimal amount of memory required to solve each job. If the estimated memory requirement exceeds the value of memorymax defined here, Nastran will limit memory usage to the value defined here 2.If the associated "memory" setting is set to "Manual" and a memory size greater than the value of memorymax defined here is specified, Nastran will limit memory usage to the value defined here maxMemory represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system.It is only required when MemoryMaxMethod = User.
- `setMemorymaxMethod(memorymaxMethod: apex.compute.MemorymaxMethod) -> None` — Max memory definition method.
- `setResultFileFolder(resultFileFolder: str) -> None` — the fully qualified pathname of the folder where the Nastran result file(s) will be written. If omits, the system will generate the result files in the input file folder.
- `setScratchFileFolder(scratchFileFolder: str) -> None` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written
- `setSolverExecutionPreference(solverExecutionPreference: apex.compute.SolverExecutionPreference) -> None` — Preference to set solver/parallel/memory. If SolverExecutionPreferenc = Auto, Nastran will automatically select the solver/parallel/memory. It is not required the setting of memorymax, memory, cupthreads, buffersize, bufferpool. If SolverExecutionPreferenc = Manual, user can configure the setting of memorymax, memory, cupthreads, buffersize, bufferpool.
- `setSolverPath(solverPath: str) -> None` — fully qualified path to the Nastran installation folder.For example r"D:\MSC\Software\Nastran\2022.1\bin\nastranw.exe"

## `apex.compute.ComputeEnvironmentNastranIntegrated`
A class used to define the compute environment for Nastran.
Properties: `fxphysical`, `matrixConditionLimit`, `memorymax`, `memorymaxMethod`, `scratchFileFolder`

Methods:

#### `ComputeEnvironmentNastranIntegrated(scratchFileFolder: str, matrixConditionLimit: float = 1.00E+12f, memorymax: float = 4.0 GB, fxphysical: float = 0.75f, memorymaxMethod: apex.compute.MemorymaxMethod = apex.compute.MemorymaxMethod.Fraction) -> None`
Constructor of IntegratedSolverNastran.

- `scratchFileFolder` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written
- `matrixConditionLimit` — The matrix condition limit for analysis
- `memorymax` — Max memory definition method
- `fxphysical` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. memorymax represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system. It is only available when memorymaxMethod = User
- `memorymaxMethod` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.

- `getFxphysical() -> float` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. memorymax represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system. It is only available when memorymaxMethod = User.
- `getMatrixConditionLimit() -> float` — The matrix condition limit for analysis.
- `getMemorymax() -> float` — Max memory definition method.
- `getMemorymaxMethod() -> apex.compute.MemorymaxMethod` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.
- `getScratchFileFolder() -> str` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written
- `setFxphysical(fxphysical: float) -> None` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. memorymax represents a quantity of Digital Storage and must be specified using the units of Digital Storage from the active script unit system. It is only available when memorymaxMethod = User.
- `setMatrixConditionLimit(matrixConditionLimit: float) -> None` — The matrix condition limit for analysis.
- `setMemorymax(memorymax: float) -> None` — Max memory definition method.
- `setMemorymaxMethod(memorymaxMethod: apex.compute.MemorymaxMethod) -> None` — The maximum amount of memory that can be used for execution of Nastran jobs on this compute environment. fxphysical represents a fraction of physical memory, the fraction is between 0 and 1. It is only required when memorymaxMethod = Fraction.
- `setScratchFileFolder(scratchFileFolder: str) -> None` — the fully qualified pathname of the folder where the Nastran scratch file(s) will be written

## `apex.compute.LocalSolver`  (extends `ComputeEnvironmentGenDes`)
A class used to define the "Local" solver compute environment for Generative design.
Properties: `cpuThreads`, `enableGPU`, `scratchFileFolder`

Methods:

- `getCPUThreads() -> str` — the number of cpu threads that will be used for generative design solution of jobs.
- `getEnableGPU() -> bool` — enable if the GPU solver if the GPU and license are available.
- `getScratchFileFolder() -> str` — the fully qualified pathname of the folder where the generative design scratch file(s) will be written
- `setCPUThreads(cpuThreads: str) -> None` — the number of cpu threads that will be used for generative design solution of jobs.
- `setEnableGPU(enableGPU: bool) -> None` — enable if the GPU solver if the GPU and license are available.
- `setScratchFileFolder(scratchFileFolder: str) -> None` — the fully qualified pathname of the folder where the generative design scratch file(s) will be written

## `apex.compute.RemoteSolver`  (extends `ComputeEnvironmentGenDes`)
A class used to define the remote solver. The name, ip and port are required to connect with a remote computer.
Properties: `computerName`, `cpuThreads`, `enableGPU`, `ip`, `port`

Methods:

- `getCPUThreads() -> str` — the number of cpu threads that will be used for generative design solution of jobs.
- `getComputerName() -> str` — the name of remote computer to be used for running
- `getEnableGPU() -> bool` — enable if the GPU solver if the GPU and license are available.
- `getIP() -> str` — the ip of remote computer to be used for running
- `getPort() -> int` — the port number of remote engine to be installed in remote computer
- `setCPUThreads(cpuThreads: str) -> None` — the number of cpu threads that will be used for generative design solution of jobs.
- `setComputerName(name: str) -> None` — the name of remote computer to be used for running
- `setEnableGPU(enableGPU: bool) -> None` — enable if the GPU solver if the GPU and license are available.
- `setIP(ip: str) -> None` — the ip of remote computer to be used for running
- `setPort(port: int) -> None` — the port number of remote engine to be installed in remote computer

## `apex.compute.RemoteSolverGroup`  (extends `ComputeEnvironmentGenDes`)
A class used to define the collection of remote solvers. In current release, only a single remote solver can be activated and used to run simulation.
Properties: `activeSolver`

Methods:

- `addRemoteSolver(remoteSolver: apex.compute.RemoteSolver) -> None` — activate the remote solver to be used in simulation from the remote solver collections by index.
- `exportRemoteSolver(exportName: str) -> None` — Export a collection of remote solvers to XML file.
- `getActiveSolver() -> int` — activate the remote solver to be used in simulation from the remote solver collections by index.
- `importRemoteSolver(importName: str) -> None` — Import remote solvers form existing remote solvers defined in XML file.
- `removeRemoteSolver(index: int) -> None` — Remove a new remote solver from the remote solver collection by collection index.
- `setActiveSolver(activeSolver: int) -> None` — activate the remote solver to be used in simulation from the remote solver collections by index.

