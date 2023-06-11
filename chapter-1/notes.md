# Design Principles

### 1. Identify the aspects of your application that vary and separate them from what stays same.

Take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't.

### 2. Program to an interface, not an implementation.

Program to an interface really means program to a supertype. The point is to exploit polymorphism by programming to a supertype so that the actual runtime object isn't locked into the code.

### 3. Favor composition over inheritance.

Composition gives you a lot more flexibility. Not only does it let you encapsulate a family of algorithms into their own set of classes, but it also lets you change behavior at runtime as long as the object you're composing with implements the correct behavior interface.

## Design Pattern

### Strategy Pattern

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
