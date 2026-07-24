# SOLID Cheat Sheet

What are SOLID Principles?
SOLID is an acronym that represents five core principles of object-oriented design:

- **S - Single Responsibility** Principle 
- **O - Open/Closed** Principle
- **L - Liskov Substitution** Principle 
- **I - Interface Segregation** Principle 
- **D - Dependency Inversion** Principle 


## 1. Single Responsibility Principle
> A class should have only have one job or responsibility.


## 2. Open/Closed Principle (OCP)
> Software entities (classes, modules, functions, …) should be open for extension but closed for modification.

Prefer interfaces over modifying a base class.


## 3. Liskov Substitution Principle (LSP)
> Let ‍ m() be a property provable about objects ‍ x of type T. Then ‍ m() should be true for objects ‍y of type S where S is a subtype of T.

`Objects` of a parent class should be replaceable with `Objects` of a child class without affecting the correctness of a program.


## 4. Interface Segregation Principle (ISP)
> A client should not be forced to implement behaviors it doesn’t use. Instead of one large interface, we should have multiple smaller, specific interfaces.

Prefer smaller specific interfaces over one big one.


## 5. Dependency Inversion Principle (DIP)
> High-level modules (class that knows what to do) should not depend on low-level modules (the class that knows how to do it). Both should depend on abstractions.
>
> Abstractions should not depend on details. Details should depend on abstractions.

A class doesn't have to know specific implementations of its dependencies, it only needs the interface.

```csharp
public interface PaymentProcessor {
    void processPayment();
}

public class PaypalPaymentProcessor implements PaymentProcessor {
    @Override
    public void processPayment() {
        // PayPal payment processing logic
    }
}
```