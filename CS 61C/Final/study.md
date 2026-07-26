# CS61C Final Study Sheet

## Number Representation 
- Fill this in later

## Assembly
- In C, the main objective of the linker(?) is to translate the code written in C into 
a lower-level language, called **assembly.** 
- In assembly, everything is stored in a **register**, of which there are 28, separated into 
several classes:
	- `x0`: Null register. This register always holds the value 0, and cannot be modified. 
	It is protected in the same way that the address `0x0` is not accessible by C code (you will 
	segfault if you do).
	- `a0-a7`: registers generally used as arguments to be passed into a function. 
	- `s0-s11`: called "save registers". 
	- `t0-t6`: temporary registers. 
	- `ra`: return address; register exclusively used to store the return address of a function
	- `sp`: stack pointer: the pointer to the bottom of the stack in memory (remember that 
	stack grows downward, so this is the furthest we go)
	- `gp`, `tp`: thread and global pointers, don't worry about these.

### Calling Convention
- In order to make sure our code runs smoothly across all platforms, we generally adhere to 
a **calling convention**. The convention tells us which variables the *caller* needs to keep 
track of and which ones the *callee* needs to keep track of:
	- Caller saved variables: These are variables that the *caller* is responsible for handling. 
	This means that if the *callee* uses these variables, it's up to the *caller* to ensure 
	that its value remains unchanged. These variables include `ra`, `t0-t6`, `a0-a7`. 
		- `ra` needs to be stored by the caller becuase if it makes further function calls, 
		the value of `ra` may change, and we need to make sure that `ra` is correct so that when
		we leave the function call, we return to the correct location in the program.
		- `t0-t6` are temporary registers, hence the callee can use these at their discretion, 
		so it's up to us (the caller) to make sure that these values remain unchanged. 
		- `a0-a7` must be stored for more or less the same reason: the callee may make further 
		function calls, so we need to make sure that these values remain uncahnged too.
	- Callee saved variables: these are ones that the callee must take care of. These include:
	`s0-s11`, `sp`.
		- `s0-s11` needs to be saved because these are save registers, and should not be changed 
		during a function call by convention. Hence, the callee must make sure that if it uses 
		these variables, that they are restored to their initial values before 
		exiting the function. 
		- `sp` needs to be restored to its original location in order to prevent us 
		from running out of memory. This is equivalent to the "function frame" being deleted and 
		no longer having access to anything below that in the stack.
### Arithmetic, Logical Operations
- There are many different kinds of instructions that assembly allows us to use. A lot of them 
share commonalities with one another, so this will be a brief overview of all the different 
types of instructions. See the reference card for a full list.
	- `add rd rs1 rs2`: adds the two values in `rs1` and `rs2` and stores them in `rd`. Anything
	of this form performs some logical operation on `rs1`, `rs2` and stores the result in `rd`.
	- `addi rd rs1 imm`: adds the value `imm` to `rs1`, and stores the result in `rd`. 
	- `lw rd imm(rs1)`: loads a word (4 bytes) from the location `rs1` in memory into `rd`.  
	- `sw rs2 imm(rs1)`: stores the value `rs2` into the address specified by `rs1 + imm`. 
	- `beq rs1 rs2 label`: branch instruction that branches to the PC specified by `label` if 
	`rs1` and `rs2` are equal in value.
	- `jal rd label`: jump to the PC specified by `label`, and set `ra = PC + 4` (the next 
	line to be executed once the function is executed). 
	- `auipc rd immu`: adds unsigned value (12-bit) `immu` to the PC and stores that value 
	in `rd`. <span style = "color:red"> why are we left-shifting by 12? </span>
	- `lui rd immu`: stores unsigned value (12-bit) `immu` into `rd`. 

### Instruction Formats
- Since all instructions are basically machine code at the end of the day, we need to be able to 
translate all assembly lines (such as `add rd rs1 rs2`) into a 32-bit binary number. To do that, 
each instruction type has its own opcode, and for certain instruction types, the identifiers 
`funct3` and `funct7` are also provided. 
- To translate from binary to instruction:
	- First use the opcode (last 7 bits) to figure out the instruction type.
	- With the instruction type determined, look at the table to find the breakdown of which bits
	correspond to what kinds of data entry. 
	- From there, it's possible to figure out what the other fields refer to. The values of `rd`, 
	`rs1` and `rs2` have a corresponding value that we can translate 
	to binary (e.g. register `a4` is `x14` in decimal, or `0b1110` in binary.). 
- To translate from instruction to binary:
	- Start with the opcode, and also decode all the registers into their binary 
	values. 
	- Translate other values such as `funct3` and `funct7` into their binary values as well
	- Stitch the whole thing together according to the table on page 2

<span style = "color:green"> Note that in J and B-type instructions, we don't store the last bit, 
since we already know that bit's going to be a 0! </span> 

## Compiler, Assembler, Linker, Loader
- This section covers roughly how `gcc` turns code written in C into an executable `a.out` that 
we get.
- The C code goes through in this exact order: `foo.c` $\rightarrow$ compiler $\rightarrow$
`foo.s` $\rightarrow$ assembler $\rightarrow$`foo.o` $\rightarrow$ Linker $\rightarrow$ `a.out`. 
	- We then have the choice to execute `a.out` using a loader. 
	- The compiler takes a high-level language code (e.g. C) and outputs the corresponding 
	code in assembly (`foo.s`). At this point, the output can still contain pseudoinstructions. 
	- The assembler takes the assembly code and **gets rid of all pseudoinstructions**, and 
	converts everything to **machine readable code**.
		- In doing so, it has to pass through the code twice. This is becuase in C (and also in 
		our assembly code), we have labels telling us where to jump. However, when converting this 
		to machine code, we need to get rid of this entirely and use an *absolute scale*, so 
		we need to pass through the code twice in order to figure out where all the jump 
		instructions lead.
	- The linker then takes these object files and combines them to produce an 
	executable. Naively, we could link the files together statically -- If we edit part of the 
	library, we'd have to recompile the program in order to receive these 
	changes. However, on most windows/UNIX systems, we now have *dynamically linked libraries*, 
	which are marked with the `.dll` extension. These are useful becuase we no longer need to 
	recompile, but this comes at the cost of a runtime overhead of needing to look at these 
	libraries every time. 
	- The loader takes the executable and executes it. In reality, it is basically just the 
	operating system doing its work.

## Synchronous Digital Systems (SDS)

### Transistors
- Here, we study the foundations behind how a CPU is actually made, from the circuitry itself. 
While historically logic gates were implemented using transistors, in recent decades we've
switched entirely to using transistors instead.
- MOS: stands for Metal-Oxide Semiconductor, and act as voltage-controlled switches (basically, 
when a voltage passes a certain threshold it allows current through). They have three components: 
Drain, Gate, Source
	-  **n-channel**: open when voltage at $G$ is low, and closes when $V(G) > V(S) + \epsilon$.
	- **p-channel**: closed when voltage at $G$ is low, and opens when $V(G) > V(S) + \epsilon$. 
	- Note that for both these transistors, the condition that they switch states is the same, but 
	they are opposites of each other.
	<span style = "color:red"> Do we need to explicitly know the circuitry behind how 
	logic gates are created? </span>
	- These gates can be used to create AND, OR, NOT, and NAND gates, and this is all you need 
	to build a computer!

### Signals and Waveforms
- We treat signals as having the ability to travel instantaneously from one logic component 
to the next. In reality of course, we do have to account for some delays. 
- SDS are made of two basic circuit components:
	- **Combinatinonal Logic (CL)**: these are elements whose output is a function of the 
	inputs only. An adder is an example of a CL block.
	- State elements: circuits that store information. 

### Combinational Logic
- Truth tables are way for us to identify what an output of a combinational logic block is given 
an input. 
- Given a function $F$, and a set of inputs, how do we figure out what kind of combinational 
logic block $F$ is? To do this, we use *boolean algebra*. 
- To figure out the identity of a combinational logic block when given its truth table, we take 
the sum of all the combinations that evaluate to 1, and take a sum of all of these. Suppose 
we're given:

|abc|y|
|-|-|
|000|1|
|001|1|
|010|0|
|011|0|
|100|1|
 
Then, we'd take a sum of all the values that evaluate to 1: $\overline a\overline b \overline c +
\overline a \overline b c + a\overline b \overline c$. Then, we can use the rules of 
boolean algebra to simplify this expression and figure out the combinational logic.

### Single Cycle Datapath
- So now that we've seen what a combinational logic block does and how to simplify it, let's
move towards figuring out how we can execute a given instruction (given in assembly, not machine 
code). 
- We will abstract away all the combinational logic blocks and instead just work with boxes
instead. 
- On every tick of the clock:
	- All combinational logic blocks read in the value passed in at input, and does its 
	computation. (these elements come from the state elements)
	- The outputs of the combinational logic blocks arrive at the input to the state elements, 
	**but the value of the state elements are not changed until the next rising clock**.  
- There are four state elements:
	- PC: Program counter
		- Keeps track of where we are in the code, done through a 32-bit register.   
	- RegFile: register file 
		- A "file" keeping track of the value of all the registers. It's basically a big file 
		full of registers. 
		- As input, it takes in data, a write-enable flag, a `writeIndex` (which tells us
		which register to write to), and two `readIndex` values. Note that if the `regWEn = 0`, 
		then none 
		of the registers are changed. 
		- As output, it returns the values of the registers that we referenced with 
		`readIndex`. 
		- <span style="color:#1AE4E4"> Note that this block behaves like a combinational block 
		for read operations! </span>
	- DMEM: memory (think RAM and data memory)
		- Just like we did with C and assembly, this is addressed using 32-bit blocks, so 
		1 word is equal to 4 bytes.  
	- IMEM: instruction memory, where the code lives. Also has a `writeEn` flag, which tells us 
	when to edit memory. 
	- As with state elements, these are elements that change once at the rising edge of the clock, 
	and **don't change again**. 
	- <span style="color:#1AE4E4"> In reality, we know that these memory locations are really 
	there in place of caches, which we'll talk more about later. </span>
- A single instruction is done in multiple phases:
	- Instruction Fetch: Here, the program counter is incremented and the instruction is read 
	in from IMEM. 
	- Instruction Decode (ID): Where the instruction is broken down to identify what the 
	instruction wants us to do. Here, registers are being read and their values are being 
	passed through.
	- Execute (Ex): Where the instruction is executed. The requisite things are being passed 
	into the ALU (if necessary).
	- Memory Access (Mem): If required, we store the values back into memory.
	- Write Back (WB): If necessary, write back the values into some registers.  
- Because not all instructions require all these steps, we implement a file called `control_logic`
that tells us which parts of the datapath are needed to execute the instruction.   

#### `add` datapath
- First, we add 4 to PC, the mux for PC.
- `regWen = 1`, becuase we need to write back the resulting value into the corresponding register.
- `immsel = 0`, we don't care about the immediate here 
- `Asel = 0`, we need the data from regfile.
- `Bsel = 0`, same reason
- `BrUn`, `BrEq`, `BrLt`, can be set to anything because we don't care (we'll set it to 0 for 
simplicity's sake). 
- `ALUSel = add`, we need to add the two inputs together
- `MemRW = 0`, we don't need to write to memory here
- `WBSel = 1`, we need to take the result from the ALU and write it back into the register.      

#### `beq` datapath
- `PCSel` depends on what the result of the branch comparison was. We won't worry about it for
*this* cycle, because we don't know the result of the branch comparison yet.
- `RegWEn = 0`, we don't want to change any registers here.
- `BrUn = 0`, this is not an unsigned comparison
- `ASel = 1`, `Bsel = 1`, we want to grab the value for the PC as well as the immediate in case 
we need to add for a jump.
- `ALUSel = add`, we want to add `PC` and `imm` together. 
- `MemRW = 0`, we don't want to write to memory here.
- `WBSel = any`, we don't care what we select here becse `RegWEn = 0`.   

#### `jal` datapath
- `PCSel = 1`, we want the result from the ALU into the PC.  
- `RegWEn = 1`, we want to write `PC + 4` to some register.  
- `ImmSel = 1` (whatever the corresponding bitstring is for a j-type), we want to get the correct 
value to jump to
- `BrUn = 0`, we don't care because we're not branching
- `ASel = 1, BSel = 1`, we want to add `imm` to `PC`
- `MemRW = 0`, don't write to memory
- `WBSel = 2`, want to write `PC + 4` to some register. 

### Pipelining
- One way we can make our code run a bit faster, is to shorten the time between instructions. 
This is done via *pipelining*, where we section the entire circuit into multiple segments, so that 
instructions can be stacked on top of one another. 
- To do this, we need to store the values in certain lines as we go down the pipeline. This 
is what we call a **pipeline register**. 
	- these are registers that store the data in **outgoing lines**, so for instance if 
	we wanted to make a pipeline between IF and ID, we'd need 3 pipeline registers: one for the 
	instruction, one for the `PC`, and one for `PC + 4`.  
	
	<span style = "color:red">  check this later, it seems like there are only two pipeline 
	registers in IF-ID on the slides. 

#### Hazards
- These are potential issues that we may run into while pipelining. 
- When we run into a branch instruction and jump, we need to make sure that the next 
lines (which are already being executed given that our circuit is pipelined) aren't 
going to finish executing, since this would mean that our program was executing things 
out of order!
	- Structural Hazard: two instructions require access to a single resource. These are not 
	really of great concern in 61C. For instance, `add t0 t1 t2` would cause issues, since we'd 
	need to simultaneously read and write to the regfile in a single cycle. 
	This is something that we *will* do,
	but does need to be taken into consideration. Also, if we separate IMEM and DMEM out, 
	then we'll completely avoid structural hazards entirely.
	- Data Hazard: there are two different lines of code that are referencing the same value 
	in memory, we cannot have this.
		- Load instructions can't be forwarded, 
		because memory access is executed on the same step as 
	the next instruction's ALU, meaning that we require a stall.
	- Control hazard: the jump/branch instructions discussed above. 
		- There is something called *branch prediction* that allows us to foresee a branch, guess
		which way the branch goes, and then flush if we're wrong. 
- There are two solutions to hazards: either we stall the execution, or we forward data.
	- Stalling the execution is the naive method which works, but slows down the execution of our 
	program. 
	- Forwarding uses the result of the data immediately as it is produced, which eliminates
	the need to stall. However, this would then require the implementation of *forwarding 
	control logic*, so we don't do it here. 
- Computing cycles per instruction:
$$ CPI = \frac{\text{time}}{\text{program}} \div 
\left( \frac{\text{instructions}}{\text{program}} \times \frac{\text{time}}{\text{cycle}}\right)$$

## Caches
- So we've learned that memory access is very costly. What can we do to minimize the number of 
times we access memory? The answer, create an *auxillary* memory close to the CPU that's 
smaller, but with the added benefit of being easy to access. 
- The cache is divided up into *blocks*, where certian contiguous pieces of memory are located. 
There are different kinds of caches:
	- **Direct Mapped:** Basically "stripe" memory into certain sections, so to check whether a
	memory block already exists in cache is a single inquiry. 
		- The size of the direct-mapped cache tells us how wide a block of data is. 
		- To determine which piece of memory is there, we supply the cache with a 
		tag, index and offset which uniquely specifies a specific location in memory.
			- To calculate the offset, determine how many bits is necessary to specify the 
			correct byte within a block (so if we have 4-byte blocks, then we'd require 2 bits 
			to encode the offset)
			- To calculate the index, we determine how many bits are required to specify the 
			specific block. If the cache size is 8 bytes and we have 2-byte blocks, then 
			a specific block is given by $8/2 = 4 = 2^2$, so we need 2 bits to store this 
			information
			- The remaining indices are used for the tag (32 - I + O) = tag size.  
		- The size of the cache is given by the product of its height and width. 
- Terminology:
	- Cache Hit: when data we try to access is found within the cache
	- Cache Miss: when we have to grab from memory because the value was not found 
	in cache
	- Cache miss, block replacement: when the cache is full, we need to evict a block from the 
	cache. Different systems do this process differently. 
- We also use a valid bit to determine whether the data within that block is something we can 
trust. This has the added benefit that when we want to clear the cache, we just set all the valid
bits to zero, and there's no need to set the actual cache memory to zero.
- Compulsory miss: a miss as a result of the fact the program just started. Every block of 
memory will have one compulsory miss (because that data will never exist in the cache beforehand). 
- Conflict miss: a miss that occurs because two memory accesses compete for the same 
spot in the cache. These conflict misses are solved in a *fully-associative cache*, where the block
literally goes anywhere in the cache. 
- Capacity miss: A miss as a result of the cache running out of space.   
- See slides for a flowchart on how to categorize misses. 

### Set-Associative Caches
- Tag and offset are the same as before, but here, the index points to which "set" we are in.
<span style = "color:red"> Does this mean that we require $\log_2(N)$ bits for the index? 
- Given a memory address, we first find the set using the index value, then we compare the 
tag with all tags within the set. If the tag matches, then we get a hit, otherwise we get a miss. 
In the case of a hit, we use the offset to find the data within the block.  
- Caches can also be multilevel -- as is the case in nearly all of our modern systems: the 
caches are L1, L2, L3 respectively, and each respective
cache is slightly slower than the former, but 
has the benefit of being able to hold slightly more data. 

## Parallelism

### Single Thread Optimizations 
- Cache-optimized programming: this relies heavily on the fact that we can optimie our memory 
accesses to make better use of our cache -- the fewer things that need to be evicted, the 
faster our program can run.
- Variable Caching: store commonly used values in variables rather than registers,
so that we don't even need to access cache! 
This uses the fact that registers are faster to access than 
the cache. In C, we use the `register int` keyword to tell the compiler to store these 
values into a register rather than the cache. 
- Loop unrolling: Instead of using loops, we can just write them in lines instead! Function 
inlining is also basically here -- instead of using functions, just paste the body 
of the function in instead, since jumping also causes a lot of runtime delays. 
- SIMD: Parallel data calculations in order to speed up calculations even further. This uses 
the intel intrinsics (AVX and SSE family) instructions. This allows us to speed up our code 
even more because data is being calculated in parallel now.
	- Specifically we use `_mm256i` vectors of data, and their allowed methods in order to 
	access, compute, and optimize data.
	- In general, it will look something like this:
	```c
		int arr[4] = {3, 1, 4, 1};
		
		// Initialize sum vector to 0
		__m128i sum_vec = _mm_setzero_si128();

		// Load elements into a temporary vector (128 bit vector allows up to 4 32-bit ints, so 
		// no need to load this more than once.
		__mm128i temp = _mm_loadu_si128((__m128i*) arr);

		//add to sum vector
		sum_vec = _mm_add_epi32(sum_vec, tmp); 
		
		// make a temporary array so that we can sum over all elements
		int tmp_arr[4];
		_mm_storeu_si128((__m128i*) tmp_arr, sum_vec);

		int sum = tmp_arr[0] + tmp_arr[1] + tmp_arr[2] + tmp_arr[3];
	```
	- Couple things to note about this code:
		- If we had more elements in the array, we'd have to create a for loop 
		to iterate from 1 to the total size of the array. In doing so, we'd have to continuously 
		accumulate the sum into `sum_vec`, 
		and finally store the SIMD vector somewhere so we can sum over all 
		elements at the end. 

### Multithreaded Optimizations
- Utilizes OpenMP: an extension of C that allows us to multi-thread our code.  
- There are two philosophies with parallel loops: we can either interweave the threading, or 
we can block the threads altogether. The latter is generally faster when considering 
standard multithreading procedures (fork-join philosophy)
- One issue with multithreading is making sure that variable accesses are being done properly. 
Some threads run faster than others, meaning that it's entirely possible that one thread 
finishes before another, and edits some shared value before the other thread has the time to react.
	- To fix this, we could add a "critical" portion to our code, which allows us to limit the 
	number of threads that access that portion of the code to a single one, however this 
	significantly slows down our code. 

### Multiprocess Optimizations
- Instead of executing a task using multithreaded processes only, we can actually optimize 
further by making our code *multiprocess*. This is the framework where we allow our code to 
execute different tasks completely independently of each other. 
- This is executed using Open MPI
- Open MPI is another extension to C that allows us to execute mutiprocessed code. For us, we 
will focus on the manager-worker framework, where one process is the manager, delegating tasks 
to a host of workers.
- This is done using the `MPI_Recv()` and `MPI_Send()` commands to send results and 
tasks through. There's a discussion note showing how to do this explicitly.
- It is possible to multithread a multiprocessor code, since multithreading happens 
on an individual core, whereas multiprocess works between multiple cores.

## Virtual Memory
- The concept of virtual memory basically allows all programs that we use to "feel" as if 
we have access to the full memory (including disk), at the speed of a cache. 
- This allows us to both speed up processing, but also prevent two programs from accessing 
the same places in memory.
- Each program has a **page table** that the OS uses in order to translate the referenced memory
location from the program to a physical address space, which is hidden from the program 
entirely.
- We split DRAM up into "pages", so when a program accesses a 32-bit address, we have to 
translate it into a physical page address.
	- Take the virtual address, and find the top bits that correspond to the VPN. 
	- Reference the page table to convert the VPN into a PPN
	- Then take the PPN and combine it with the offset to get a physical address (address 
	on DRAM). 
<span style = color:red> How to determine the number of bits required for the page offset? 
</span>
- All virtual memory also uses **write back**, meaning that things are written to RAM, and 
only written to disk when either the program terminates or when that page needs to be 
evicted. 
- TLB is a cache that stores some of the page translations, so that we don't have to go 
through the process of looking up the page table every time for some instructions. In this 
framework, the TLB is the actual thing that does most of the translation, and we only access
 the page table when needed. 

<span style = color:green> Do I need to study IO?

## Spark and MapReduce
- This is the stuff behind the data-level parallelism between multiple servers and disks. There 
really isn't much in this lecture at all, we're just talking about conceptually about how 
these things would work.


