# Review

## Coding Stuff
- Abstract lists: essentially a "template method" where we fill out the missing parts of the code.

## Timing

- amortized time: things that appear to have constant time but they only appear tha tway becuase we're "averging" them out


## Data Structures
- Collection interface and its subtypes
- Map interface and its subtypes
  - `HashMap`, `TreeMap`,`SetMap`, etc.
- Generic skeleton implementations of collections, lists, maps (`AbstractList`, etc.)


## Sequences
- Collections of data structures that are sequential (have a notion of order)
- Linked lists vs. arrays
- Circular buffering
  - Single and double linked lists
  - Use of sentinels and why they're useful
  - Stacks, deques, and why they're useful
- Costs of basic operations
  - For all of these data strucures, how long is it going to take to execute a specific operation (use table)


## Trees
- Recursive structures
- Basic operations such as insertion and deletion, tree traversals
- A couple representations of it
- Tree as a concept: game trees


## Searching
- Searching in trees, range searching
  - searching in seqeucnes
- Hashing   
  - Heuristic way of dividing up data to make searching faster
- Priority queues and heaps
  - Adding weights to objects to make searching for them also more efficient
- Balanced Trees
  - The naive implementation of trees can lead to very long search times, to get around that:
    - Rebalancing by rotation (red-black trees)
    - Balance by construction (B-trees)
    - Probabilistic balance (skip lists) 
    - Tries 
- Search times of all these data structures should also be known


## Sorting 

- Uses of sorting
- Insertion sort
- Selection sort
- Merge sort
- Heap sort
- Quicksort and selection
- Distribution sort
- Radix sort
- Runtimes for all these sorting algorithms (use table) 

## Random numbers 

- How to get the computer to do something that looks random?
- The idea of a pseudo-random sequence


## Graphs
- The algorithms that operate on them, and the times that they require 
- What are they good for? Where have we used them in this course?
  - Networks are a form of graph


## Debugging
- What debuggers can do 
- How to use to pin down bugs
- The details of some debugger 
- Unit testing: what it means, how to use it
  - Learning how to make unit tests that are comprehensive
- JUnit mechanics (provided by Berkeley's software)
  - You'll see similar variations of this in the future: in later courses or even in industry

## Version Control 
- What is it for?
- Basic concepts
  - Working copy vs. repository copy
  - Committing changes
  - Updating and merging changes
  - Tagging
- Come to terms with the benefits of version control LOL?
- Finding out that the gitlet project was created by a TA and not by hilfinger himself is a major plot twist.


## Assorted side trips

Some things that weren't really heavily covered, but are nice to know:

- Compression 
- Parallel processing
- Storage management and garbage collection
  - What java does behind the scenes 

## Future (upper div) courses that you could potentially take

**There's another slide here**

- CS170: Efficient algorithms and Intractable problems 
- CS174: Combinatorics and Discrete Probability
- CS172: Computability and Complexity
- CS182: Deep Neural Networks
- CS188: Artificial Intelligence
- CS189: Machine Learning
- CS171: Cryptography
- CSC191: Quantum information ciecne and Technology

### More

- CS194: assorted special topics (computer vision and computational photography)
- CS195: social implicatoins of computer technology
- Lots of Graduate courses: advanced versions of 152, 160, 161, etc. (see lecture notes here)
- EECS COURSES :vomit:
- Research or independent study (199), or directed group studies (198)


## Internships
- Internships offer more specific skills and exposure to real problems