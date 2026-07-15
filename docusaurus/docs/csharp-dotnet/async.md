# Asyncronous Programming in csharp
The Task Asynchronous Programming Model (TAP) is an abstraction over traditional async programming to make it easier to write and mantain.

The goal of task async programming is for code to read like a sequence of statements, but execute in a more complicated order. 


## The Breakfast Analogy
The instructions for making a breakfast might be provided as a list:

1. Pour a cup of coffee.
2. Heat a pan, then fry two eggs.
3. Cook three hash brown patties.
4. Toast two pieces of bread.
5. Spread butter and jam on the toast.
6. Pour a glass of orange juice.

You might complete these instructions asynchronously (start warming the pan for eggs, then start cooking the hash browns).

At each step of the process, you start a task, and then transition to other tasks that are ready for your attention.

Cooking breakfast is a good example of async work that isn't parallel. One person (or thread) can handle all the tasks. One person makes brekky async by starting the next task before the previous task completes.


## Concurrency vs Parallelism
This is different to a `parallel algorithm`, you would need multiple people who cook (or multiple threads). One person cooks eggs, another cooks hash browns, and so on. Each person focuses on their one specific task.

"A system is said to be concurrent if it can support two or more actions in progress at the same time. A system is said to be parallel if it can support two or more actions executing simultaneously" - ***The Art of Concurrency***


## Task Asynchronous Programming Model (TAP)
- **State machine** - Tracks *what* code needs to run
- **SynchronizationContext** - Tracks *Where* it should run (or which thread)
- **ThreadPool** - Provides the Physical CPU threads to execute the code


### State Machine
When you add `async` to a method, the compiler creates a [state](https://refactoring.guru/design-patterns/state) machine in the background. See `IAsyncStateMachine`.

It tracks the current completion status, preserves local variables across execution boundaries, and resumes methods exactly where they paused. 

Creating a state machine can be expensive, so it's essential to avoid creating them unnecessarily.

- It pauses code when hitting an incomplete await statement.
- It saves local variables and parameters so they survive across threads.
- It executes a `MoveNext()` method to jump to the next "state" once an asynchronous operation completes

#### Best Practices
Here are some best practices to keep in mind:

- Only use `async` in a method when you have an `await` in the method body.
- Don’t use `await` if you don’t need a value returned from a call to an asynchronous method. Just return the `Task` to the upstream caller.
- If you need to use `async` but don’t need to use `await` to get a required value and want to return from the method, use `Task.FromResult`.
- If you don’t want to return any value from the method, use `Task.CompletedTask`.
- Avoid using `async void` methods.


### Synchronization Context
`SynchronizationContext` is a class used to queue work to a specific "execution environment".

- It represents the "target environment" (e.g., the Main UI thread in WPF/WinForms, or the ThreadPool).
- Functions as a "fire-and-forget" worker queue.


### ThreadPool
By definition, a thread pool is managed pool of threads that can be used to execute tasks concurrently.

The threads managed by the thread pool are often called worker threads. The worker threads are optimized for short-running tasks.

Also, the worker threads are background threads.

It works by:
1. A thread pool spawns a number of threads upfront.
2. When you submit a task to a thread pool, the thread pool adds the tasks to a queue and assigns a thread from a pool to execute the task.
3. Once the thread completes the task, the thread is returned to the pool.

By doing this, the thread pool can reuse threads and avoid the overhead of creating and destroying threads for each task, which is very expensive.

#### Threads
Async methods are intended to be non-blocking operations. An `await` expression in an async method doesn't block the current thread while the awaited task is running

The `async` and `await` keywords don't cause extra threads to be created.

Async methods don't require multithreading because an async method doesn't run on its own thread.

The method runs on the current `synchronization context` and uses time on the thread only when the method is active. 


### Thread Synchronization
Refers to the coordination of multiple threads to ensure their safe and orderly execution in a multi-threaded environment.

Prevents race conditions, data corruption and other issue when multiple threads access shared resources concurrently.

The following are types that can be used to synchronise access to shared resources. See [Overview of Synchronization primitives](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives) for the full list.

#### Lock
`lock` is used to ensure mutual exclusion (prevent multiple threads from accessing a shared resource). 

When a thread encounters a lock, it attempts to acquire the lock on the specified object and if it is already held by another thread - waits until the lock is released before proceeding.


#### Deadlock
A deadlock is a situation where 2 or more threads are unable to proceed because each is waiting for a resource held by another thread also in the deadlock.

Circular dependency - all threads are blocked indefinitely.


#### Interlocked
The `System.Threading.Interlocked` class provides atomic operations for variables shared between threads. It operates directly at the CPU instruction level.

It offers thread-safe and atomic operations without the need for explicit locking mechanisms, such as lock or Monitor.




## References
- [Task Asynchronous Programming Model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)
- https://dev.to/sajadjalilian/c-concurrency-in-a-nutshell-2c3c
- https://refactoring.guru/design-patterns/state
- https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives
