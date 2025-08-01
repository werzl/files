# `Memory <T>`

## `Memory<T>` and `Span<T>` Usage Guidelines
https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/memory-t-usage-guidelines

- Rule #1: For a synchronous API, use `Span<T>` instead of `Memory<T>` as a parameter if possible
- Rule #2: Use ReadOnly`Span<T>` or ReadOnly`Memory<T>` if the buffer should be read-only
- Rule #3: If your method accepts `Memory<T>` and returns void, you must not use the `Memory<T>` instance after your method returns
- Rule #4: If your method accepts a `Memory<T>` and returns a Task, you must not use the `Memory<T>` instance after the Task transitions to a terminal state
- Rule #5: If your constructor accepts `Memory<T>` as a parameter, instance methods on the constructed object are assumed to be consumers of the `Memory<T>` instance
- Rule #6: If you have a settable `Memory<T>`-typed property (or an equivalent instance method) on your type, instance methods on that object are assumed to be consumers of the - `Memory<T>` instance
- Rule #7: If you have an `MemoryOwner<T>` reference, you must at some point dispose of it or transfer its ownership (but not both)
- Rule #8: If you have an `IMemoryOwner<T>` parameter in your API surface, you are accepting ownership of that instance
- Rule #9: If you're wrapping a synchronous P/Invoke method, your API should accept `Span<T>` as a parameter
- Rule #10: If you're wrapping an asynchronous p/invoke method, your API should accept `Memory<T>` as a parameter