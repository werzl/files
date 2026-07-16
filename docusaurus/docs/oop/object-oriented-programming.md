# Object Oriented Programming (OOP)
Programming paradigm for modelling real-world entities into objects - which combine data and behaviour/logic.

The 4 main principles are:
- **Encapsulation**
- **Inheritance**
- **Abstraction**
- **Polymorphism**


## Class
A class is a blueprint for creating objects. It bundles 2 core components into one unit:
- **Properties** - Variables or data fields that definte the state or properties of the class
- **Methods** - The functions or operations that define what the class can do, or how it manipulates its data

Classes occupy no memory address for data, they are just instructions.

## Object
An object is an instance of a class. Data members and methods of a class cannot be used directly - the class must be instantiated - at which point it becomes an object (an instance of a class).

Objects have a unique address in memory, multiple objects can be created from one class - each with different data.

Memory is allocated the moment an object is created.


## Encapsulation
Binding of data and methods into a single unit, and keeping the internals of an object hidden from outside code.

- **Data hiding** - Language feature to restrict access to members of an object, e.g `private`, `protected` members in C#.
- **Keeping related data and methods together (cohesion)** - Data, and the methods that operate on that data are bundled together. e.g keeping related methods & properties together in a class.
- **Decoupling** - Organise code so that only certain parts of the data are used by related functions, e.g objects act as a boundary between their internal workings, and external consuming code.


## Inheritance
The mechanism that allows a new class to adopt the attributes and methods of an existing class.

### Single Inheritance
It establishes a "is-a" relationship between classes.
- **Parent class** - a.k.a *base class* or *superclass* - The existing class that contains the original code.
- **Child class** - a.k.a *derived class* or *subclass* - The new class that inherits the code and can add additional features.

### Multiple Inheritance
Allows a child class to inherit directly from more than one parent class.

Not available in C# for classes, but IS for interfaces.

```csharp
public class Vehicle { }

public interface IFlyable
{
	void Fly();
}

public interface IDriveable
{
	void Drive();
}

public class FlyingCar : Vehicle, IFlyable, IDriveable
{
	public void Fly() { }
	public void Drive() { }
}
```


## Abstraction
When creating an object, use abstraction to show only essential information - 'hiding' complex internal details.

It reduces complexity by letting you focus on *what* an object does, instead of *how*.

- **Abstract classes** - Classes that can't be instantiated, more like a template for other classes. Often contain **abstract methods** (methods without any code body) which child classes must implement. Abstract methods CAN contain logic/implementations.
- **Interfaces** - A contract that defines what methods a class must have, but doesn't contain any implementation logic.


## Polymorphism
The word `Polymorphism` means having many forms. It allows different classes to be treated as instances of the same class through a common interface.

### Compile-time Polymorphism (static binding)
At compile time, the compiler decides which method to run based on the method signature.

- **Method overloading** - Multiple methods with the same name but different parameters.
```csharp
public int GetUserAge(string name)
...

public int GetUserAge(Guid id)
...
```

### Runtime Polymorphism (dynamic binding)
When an app is already running, the computer decides which method to run based on the object type.

- **Method overriding** - A child class provides its own version of a method that is already defined in its parent class.
```csharp
public class Vehicle
{
	public virtual void Start()
	...
}

public class Truck : Vehicle
{
	public override void Start()
	...
}
```
> In C# - the `virtual` modifier is used in a parent class to declare a method that can be overriden by any class that inherits from it.

## References
- https://en.wikipedia.org/wiki/Object-oriented_programming
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Object-oriented_programming
- https://www.geeksforgeeks.org/interview-prep/oops-interview-questions/