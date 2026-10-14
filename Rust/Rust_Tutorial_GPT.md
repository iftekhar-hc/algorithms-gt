# The Complete Rust Tutorial for C++ Programmers

_A practical guide to learning Rust by translating your existing C++ knowledge into Rust concepts._

Rust is a systems programming language designed for performance, memory safety, and concurrency. If you already know C++, many Rust concepts will feel familiar: structs, enums, generics, traits, iterators, closures, pattern matching, and zero-cost abstractions.

However, Rust makes some fundamentally different design choices. Instead of relying primarily on constructors, destructors, RAII, and programmer discipline to manage memory, Rust uses an ownership system and compile-time borrow checking to prevent many memory errors.

This tutorial takes you from basic syntax to advanced Rust programming, emphasizing the differences that matter most to a C++ programmer.

## Learning roadmap

We will cover the following topics:

1. Rust installation and development tools
2. Rust compared with C++
3. Variables, mutability, constants, and types
4. Functions, expressions, and control flow
5. Ownership, moves, borrowing, and references
6. Structs, enums, pattern matching, and methods
7. Strings, arrays, vectors, slices, and collections
8. Error handling with `Option` and `Result`
9. Generics, traits, and trait objects
10. Closures, iterators, and functional programming
11. Modules, crates, packages, and Cargo
12. Smart pointers and memory management
13. Lifetimes and advanced borrowing
14. Concurrency, threads, and synchronization
15. Asynchronous programming
16. File I/O and practical systems programming
17. Testing, debugging, and tooling
18. Unsafe Rust and FFI with C and C++
19. Performance, idiomatic design, and common pitfalls
20. A complete practical project
21. A C++-to-Rust reference guide and exercises

The examples use modern Rust 2024-edition conventions. Rust is evolving, so compiler diagnostics and some library APIs may vary slightly by toolchain version.

---

# 1\. Understanding Rust from a C++ perspective

## 1.1 What is Rust?

Rust is a statically typed, compiled programming language intended for applications where performance and control over resources matter.

Typical use cases include:

- Operating systems and system utilities
- Embedded software
- Networking and server infrastructure
- Command-line applications
- WebAssembly applications
- Database engines
- Game engines and performance-sensitive libraries
- Language runtimes and developer tools
- Applications that need reliable multithreading

Rust compiles to native machine code and can deliver performance comparable to C++ for many workloads.

Its defining feature is that it provides strong memory-safety guarantees without requiring a garbage collector.

For example, Rust prevents many common errors at compile time:

- Use-after-free
- Double-free
- Dangling references
- Iterator invalidation through many common safe APIs
- Data races involving ordinary safe shared memory
- Accidental use of moved values

Rust does not eliminate every possible bug. Logic errors, deadlocks, resource exhaustion, incorrect algorithms, and problems introduced through unsafe code remain possible.

## 1.2 Rust versus C++

| Feature | C++ | Rust |
| --- | --- | --- |
| Compilation | Native compilation | Native compilation |
| Static typing | Yes | Yes |
| Memory management | RAII, smart pointers, manual management | Ownership, borrowing, RAII |
| Garbage collector | Not required | Not required |
| Use-after-free prevention | Primarily design, tooling, and discipline | Enforced in safe code by the borrow checker |
| Null references | Raw pointers can be null | References cannot be null in safe Rust |
| Optional values | Often pointers or `std::optional` | `Option<T>` |
| Error handling | Exceptions, error codes, expected-like types | `Result<T, E>` and `Option<T>` |
| Object-oriented inheritance | Supported | No class inheritance |
| Polymorphism | Virtual functions, templates, type erasure | Traits, generics, trait objects |
| Templates and generics | Templates | Generics and monomorphization |
| Operator overloading | Supported | Supported through traits |
| RAII | Yes | Yes |
| Move semantics | Yes | Built into Rust's ownership model |
| Compile-time evaluation | `constexpr`, `consteval`, templates | `const`, `const fn`, generics, macros |
| Concurrency safety | Available, but many mistakes are possible | Strong compile-time guarantees for safe code |
| Package management | Multiple tools and conventions | Cargo |
| Build system | Multiple options | Cargo is the standard tool |

The most important difference is not syntax. It is **how Rust represents and enforces the lifetime of data**.

### C++ example

```
#include <iostream>
#include <memory>

int main() {
    auto ptr = std::make_unique<int>(42);
    std::cout << *ptr << '\n';
}
```

The `std::unique_ptr` owns the integer and destroys it when the pointer goes out of scope.

### Rust equivalent

```
fn main() {
    let ptr = Box::new(42);
    println!("{}", *ptr);
}
```

Here, `Box<i32>` owns a heap-allocated integer. When `ptr` goes out of scope, the allocation is released.

The syntax differs, but both examples use deterministic resource management.

The deeper difference is that Rust's ownership and borrowing rules apply to ordinary values and references throughout the language, not just to smart-pointer types.

---

# 2\. Installing Rust and setting up your environment

Rust's standard toolchain manager is called `rustup`.

## 2.1 Install Rust

Visit the official installation page:

https://www.rust-lang.org/tools/install

On Linux or macOS, the official installer can be run using the command shown on that page. On Windows, follow the official instructions for the supported installer and any required C++ build tools.

After installation, check the toolchain:

```
rustc --version
cargo --version
rustup --version
```

These commands represent three different tools:

- `rustc`: The Rust compiler.
- `cargo`: The package manager and build tool.
- `rustup`: The toolchain installer and version manager.

To install the stable toolchain and select it as the default:

```
rustup toolchain install stable
rustup default stable
```

To update it later:

```
rustup update
```

## 2.2 Create your first project

Run:

```
cargo new hello_rust
cd hello_rust
```

Cargo creates a project resembling this:

```
hello_rust/
├── Cargo.toml
└── src/
    └── main.rs
```

The `Cargo.toml` file contains project metadata and dependencies.

The `src/main.rs` file contains the executable's entry point.

Open `src/main.rs`:

```
fn main() {
    println!("Hello, Rust!");
}
```

Run the program:

```
cargo run
```

Compile without running:

```
cargo build
```

Compile with optimizations:

```
cargo build --release
```

Run tests:

```
cargo test
```

Check the code without producing the final executable:

```
cargo check
```

`cargo check` is especially useful during development because it can detect many errors more quickly than a full build.

## 2.3 Rust project structure versus C++

A small C++ project might contain:

```
project/
├── CMakeLists.txt
├── include/
│   └── math_utils.hpp
├── src/
│   ├── main.cpp
│   └── math_utils.cpp
└── tests/
```

A Rust project might instead look like:

```
project/
├── Cargo.toml
├── Cargo.lock
├── src/
│   ├── main.rs
│   └── lib.rs
└── tests/
```

Rust does not require header files.

The compiler discovers modules through Rust's module system, and Cargo coordinates compilation, dependencies, testing, and packaging.

For editor support, install the Rust Analyzer extension or plugin for your editor. It provides completion, navigation, diagnostics, and refactoring support.

---

# 3\. Variables, mutability, and data types

## 3.1 Variables are immutable by default

In C++, you might write:

```
int x = 10;
x = 20;
```

In Rust:

```
fn main() {
    let x = 10;

    // x = 20; // Compile-time error
    println!("{x}");
}
```

Rust variables are immutable by default.

To permit reassignment, use `mut`:

```
fn main() {
    let mut x = 10;

    x = 20;

    println!("{x}");
}
```

Think of `mut` as an explicit declaration that a binding may be modified.

This is a fundamental Rust convention: **prefer immutability unless mutation is necessary**.

It makes data flow easier to understand and helps prevent accidental state changes.

### C++ comparison

```
int x = 10;          // Mutable
const int y = 20;    // Immutable through this name
```

Rust:

```
let mut x = 10;
let y = 20;
```

There is an important distinction: Rust's immutability applies to the binding, not necessarily to every object reachable through it. Interior-mutability types such as `Cell<T>` and `RefCell<T>` allow controlled mutation even when the containing binding is not declared `mut`.

## 3.2 Type inference

Rust infers many types from the value assigned to a variable.

```
fn main() {
    let age = 30;
    let price = 19.99;
    let active = true;
    let letter = 'R';

    println!("{age}, {price}, {active}, {letter}");
}
```

The inferred types are approximately:

```
let age: i32 = 30;
let price: f64 = 19.99;
let active: bool = true;
let letter: char = 'R';
```

You can always annotate a type explicitly:

```
let count: u64 = 1_000_000;
let ratio: f32 = 0.75;
let name: &str = "Rust";
```

Rust generally requires sufficient type information for the compiler to determine each expression's type.

## 3.3 Primitive types

Rust's commonly used primitive types include:

| Category | Rust types | Example |
| --- | --- | --- |
| Signed integers | `i8`, `i16`, `i32`, `i64`, `i128`, `isize` | `let x: i32 = -10;` |
| Unsigned integers | `u8`, `u16`, `u32`, `u64`, `u128`, `usize` | `let x: u32 = 10;` |
| Floating point | `f32`, `f64` | `let x: f64 = 3.14;` |
| Boolean | `bool` | `let x = true;` |
| Unicode scalar value | `char` | `let x = 'A';` |
| String slice | `&str` | `let x = "hello";` |
| Owned string | `String` | `let x = String::from("hello");` |

Rust does not have C++-style implicit conversions between arbitrary numeric types.

For example:

```
fn main() {
    let x: i32 = 10;
    let y: i64 = 20;

    // let z = x + y; // Error: mismatched types

    let z = i64::from(x) + y;

    println!("{z}");
}
```

For numeric types that support it, explicit casts use `as`:

```
let x: i32 = 10;
let y: i64 = x as i64;
```

Prefer explicit conversions that communicate your intent. In particular, `as` can truncate integers or produce surprising results when converting between numeric types.

## 3.4 Integer overflow

C++ signed integer overflow is undefined behavior. Rust's behavior depends on the operation and build configuration: ordinary overflowing arithmetic typically panics in debug builds, while optimized builds may use wrapping arithmetic.

When the desired behavior matters, express it explicitly:

```
fn main() {
    let x: u8 = 250;

    println!("{}", x.wrapping_add(10));
    println!("{}", x.saturating_add(10));
    println!("{:?}", x.checked_add(10));
}
```

Output:

```
4
255
None
```

The methods mean:

- `wrapping_add`: Wrap around at the type's boundary.
- `saturating_add`: Stop at the maximum representable value.
- `checked_add`: Return `None` if the operation overflows.

These methods are valuable when implementing parsers, protocol handlers, counters, and other low-level code.

## 3.5 Constants and shadowing

Rust has constants:

```
const MAX_CONNECTIONS: usize = 100;
```

Constants require an explicit type and a compile-time evaluable expression.

Rust also supports shadowing:

```
fn main() {
    let value = "42";
    let value: i32 = value.parse().unwrap();

    println!("{}", value + 8);
}
```

The second `value` is a new binding, not a reassignment.

Unlike `mut`, shadowing can change the type of a binding.

### When to use each

- `let`: A normal immutable binding.
- `let mut`: A binding that needs reassignment or mutable access to its value.
- `const`: A named compile-time constant.
- `static`: A static item with a fixed storage location, used when shared static storage is needed.

---

# 4\. Functions, expressions, and control flow

## 4.1 Function definitions

C++:

```
int add(int a, int b) {
    return a + b;
}
```

Rust:

```
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    println!("{}", add(10, 20));
}
```

Rust functions declare parameter types and return types explicitly.

If a function returns nothing meaningful, its return type is `()`—the unit type.

```
fn print_message() {
    println!("Hello");
}
```

You may also write:

```
fn print_message() -> () {
    println!("Hello");
}
```

The first form is idiomatic.

## 4.2 Expressions versus statements

One of the most important syntactic differences is that Rust distinguishes expressions from statements.

An expression produces a value.

A statement performs an action without itself producing a value that can be used as an expression.

Consider:

```
fn square(x: i32) -> i32 {
    x * x
}
```

The final expression is returned implicitly because it has no semicolon.

This is equivalent to:

```
fn square(x: i32) -> i32 {
    return x * x;
}
```

Now consider:

```
fn square(x: i32) -> i32 {
    x * x;
}
```

This is incorrect because the semicolon turns the expression into a statement, leaving the function without the required `i32` return value.

This feature becomes particularly useful when writing concise code:

```
fn absolute_value(x: i32) -> i32 {
    if x < 0 {
        -x
    } else {
        x
    }
}
```

Unlike C++, an `if` expression can directly produce a value.

Both branches must produce compatible types.

## 4.3 Conditional expressions

Rust:

```
fn main() {
    let temperature = 30;

    let description = if temperature > 25 {
        "hot"
    } else {
        "cool"
    };

    println!("{description}");
}
```

In C++, the same idea might be expressed using the conditional operator:

```
const char* description =
    temperature > 25 ? "hot" : "cool";
```

Rust's `if` is more flexible because each branch can contain multiple statements.

There is no need for parentheses around the condition.

## 4.4 Loops

Rust has three main looping constructs.

### `loop`

An infinite loop that can return a value through `break`:

```
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 5 {
            break counter * 2;
        }
    };

    println!("{result}"); // 10
}
```

### `while`

```
fn main() {
    let mut n = 3;

    while n > 0 {
        println!("{n}");
        n -= 1;
    }
}
```

### `for`

```
fn main() {
    for i in 0..5 {
        println!("{i}");
    }
}
```

The range `0..5` includes zero and excludes five.

To include the endpoint, use `0..=5`.

This is usually preferable to manually managing a loop counter.

### Iterating over a collection

```
fn main() {
    let numbers = [10, 20, 30];

    for number in numbers {
        println!("{number}");
    }
}
```

You can also iterate over references:

```
fn main() {
    let numbers = vec![10, 20, 30];

    for number in &numbers {
        println!("{number}");
    }

    println!("{numbers:?}");
}
```

Borrowing the collection avoids consuming the vector.

## 4.5 `match`: More than a switch statement

C++:

```
switch (code) {
    case 1:
        std::cout << "One";
        break;
    case 2:
        std::cout << "Two";
        break;
    default:
        std::cout << "Other";
}
```

Rust:

```
fn main() {
    let code = 2;

    match code {
        1 => println!("One"),
        2 => println!("Two"),
        _ => println!("Other"),
    }
}
```

Rust's `match` is exhaustive: all possible cases must be covered.

The `_` pattern matches anything not covered by previous patterns.

You can match multiple values:

```
match code {
    1 | 2 | 3 => println!("Small"),
    4..=10 => println!("Medium"),
    _ => println!("Other"),
}
```

You can also return values:

```
let category = match code {
    1 => "small",
    2 => "medium",
    _ => "large",
};
```

`match` is central to Rust's design because it works naturally with enums and error-handling types.

## 4.6 Loop labels

Nested loops can be controlled with labels:

```
fn main() {
    'outer: for i in 0..5 {
        for j in 0..5 {
            if i == 2 && j == 3 {
                break 'outer;
            }
        }
    }
}
```

The labeled `break` exits the specified loop.

This can be useful in parsing, search algorithms, and state machines, although extracting a function can sometimes make nested control flow clearer.

---

# 5\. Ownership: Rust's most important concept

If you learn only one major Rust concept, learn ownership.

C++ programmers already understand resource ownership through RAII, `std::unique_ptr`, `std::shared_ptr`, and move semantics. Rust extends ownership into the language's fundamental rules for ordinary values.

## 5.1 Every value has an owner

Consider:

```
fn main() {
    let text = String::from("Hello");

    println!("{text}");
}
```

The binding `text` owns a `String`.

When `text` goes out of scope, Rust drops the string and releases its heap allocation.

Conceptually:

```
text
 |
 v
String metadata
 |
 v
Heap allocation: "Hello"
```

The `String` value manages the heap allocation. The binding owns the `String`.

In C++, this resembles:

```
#include <string>

int main() {
    std::string text = "Hello";
}
```

The key difference is that Rust tracks ownership transfers statically and rejects invalid uses.

## 5.2 Move semantics

Consider this code:

```
fn main() {
    let first = String::from("Hello");
    let second = first;

    // println!("{first}"); // Compile-time error
    println!("{second}");
}
```

Why is `first` no longer usable?

A `String` contains metadata about a heap allocation, including a pointer, length, and capacity. Assigning it to `second` moves ownership rather than implicitly cloning the heap allocation.

Conceptually:

Before the move:

```
first ──> heap allocation
```

After the move:

```
second ──> heap allocation

first: no longer usable
```

The heap allocation has not been duplicated.

Rust prevents `first` from being used because that could otherwise lead to two values trying to release the same allocation.

### C++ comparison

A C++ programmer might write:

```
std::string first = "Hello";
std::string second = std::move(first);
```

Rust's assignment behaves like a move for types that do not implement `Copy`.

In C++, `std::move` is generally a cast that enables move operations; it does not itself transfer a resource. Rust's move semantics are built into the language's ownership rules.

## 5.3 Copy types versus move types

Not all assignments invalidate the original binding.

For simple types such as integers:

```
fn main() {
    let first = 10;
    let second = first;

    println!("{first}");
    println!("{second}");
}
```

Both bindings remain usable because `i32` implements the `Copy` trait.

Copyable types generally have simple, inexpensive value-copy semantics.

Examples include:

- Integer types
- `bool`
- `char`
- Floating-point types
- Tuples whose elements are all `Copy`

A tuple of owned strings is not `Copy`:

```
let first = (String::from("hello"), 10);
let second = first;

// first is no longer usable as a whole.
println!("{}", second.0);
```

### The rule

- If a type implements `Copy`, copying it preserves the original value.
- Otherwise, moving it transfers ownership when it is assigned or passed by value.

`Copy` is not the same as `Clone`.

`Copy` means an implicit bitwise-style value copy is valid for the type under Rust's type rules. `Clone` is an explicit operation that may perform a deeper or more expensive copy.

## 5.4 Cloning

If you need two independent owned strings, clone explicitly:

```
fn main() {
    let first = String::from("Hello");
    let second = first.clone();

    println!("{first}");
    println!("{second}");
}
```

For `String`, cloning generally allocates a separate buffer and copies the contents.

The distinction is important for performance.

C++ programmers should recognize this difference:

```
std::string first = "Hello";
std::string second = first; // Copies the string
```

Rust makes the corresponding ownership duplication explicit:

```
let first = String::from("Hello");
let second = first.clone();
```

Avoid unnecessary cloning, but do not avoid it when independent ownership is genuinely needed.

## 5.5 Ownership and function calls

Passing an owned value to a function moves it into the function.

```
fn consume(text: String) {
    println!("{text}");
}

fn main() {
    let message = String::from("Hello");

    consume(message);

    // println!("{message}"); // Error
}
```

The function `consume` receives ownership.

After the call, `message` is no longer valid.

This is useful when a function is intended to take responsibility for a resource.

But what if the function only needs to inspect the string?

That is where borrowing comes in.

---

# 6\. Borrowing and references

Borrowing lets you access a value without taking ownership of it.

Rust references resemble C++ references, but Rust adds strict rules governing how they can be used.

## 6.1 Immutable references

C++:

```
void print_name(const std::string& name);
```

Rust:

```
fn print_name(name: &String) {
    println!("{name}");
}

fn main() {
    let name = String::from("Alice");

    print_name(&name);

    println!("{name}");
}
```

The `&name` expression creates a reference to `name`.

The function receives `&String`, which allows it to inspect the string without taking ownership.

The original value remains usable afterward.

### A more idiomatic signature

For a function that only needs to read string contents, prefer `&str`:

```
fn print_name(name: &str) {
    println!("{name}");
}

fn main() {
    let name = String::from("Alice");

    print_name(&name);
    print_name("Bob");
}
```

This function accepts both string literals and borrowed strings.

It is similar in spirit to designing a C++ function that accepts a non-owning view such as `std::string_view`.

## 6.2 Mutable references

C++:

```
void increment(int& value) {
    ++value;
}
```

Rust:

```
fn increment(value: &mut i32) {
    *value += 1;
}

fn main() {
    let mut number = 10;

    increment(&mut number);

    println!("{number}");
}
```

The `&mut i32` type is a mutable reference to an `i32`.

The `*value` expression dereferences the reference to access the underlying integer.

A mutable borrow requires the original binding to permit mutation.

## 6.3 The borrowing rules

Rust enforces a key rule for ordinary references:

**At a given time, you may have either multiple immutable references or one mutable reference to a value, subject to the borrow checker's lifetime rules.**

For example:

```
fn main() {
    let mut value = 10;

    let first = &value;
    let second = &value;

    println!("{first} {second}");

    // A mutable borrow cannot overlap with
    // active immutable borrows.
    let third = &mut value;

    *third += 1;

    println!("{third}");
}
```

This is valid because the immutable references are no longer used when the mutable borrow begins.

Rust's non-lexical lifetime analysis allows a borrow to end after its last use, even if the reference variable remains in scope.

Now consider:

```
fn main() {
    let mut value = 10;

    let first = &value;

    // let second = &mut value; // Error

    println!("{first}");
}
```

The compiler rejects the conflicting borrow because `first` is still used after the point where the mutable borrow would be created.

### Why does Rust impose this restriction?

Suppose one part of a program reads an object while another modifies or reallocates it.

Without carefully controlled aliasing, the reader could observe inconsistent state or access invalid memory.

Rust's borrowing rules eliminate many such problems without requiring runtime locks for ordinary references.

## 6.4 References cannot outlive their referents

Consider:

```
fn main() {
    let reference;

    {
        let value = 42;
        // reference = &value; // Would be invalid
    }

    // println!("{reference}");
}
```

The value `value` is destroyed at the end of the inner scope.

Allowing `reference` to survive would create a dangling reference.

Rust rejects such programs.

This is a major distinction from C++, where dangling references can compile successfully and lead to undefined behavior.

## 6.5 Borrowing a vector

```
fn main() {
    let mut numbers = vec![10, 20, 30];

    let first = &numbers[0];

    println!("{first}");

    numbers.push(40);
}
```

The key detail is that `first` is no longer used when `numbers.push(40)` executes, so the immutable borrow can end before the mutation.

If you tried to use `first` after a vector operation that might reallocate its storage, the compiler would reject the conflicting access.

This prevents a common C++ bug: retaining an element reference or iterator after a vector reallocation invalidates it.

## 6.6 Borrowing versus smart pointers

These concepts solve different problems:

| Rust type | Rough C++ analogy | Purpose |
| --- | --- | --- |
| `T` | An ordinary value | Owns its value |
| `&T` | `const T&` or a non-owning view | Immutable borrowing |
| `&mut T` | `T&` | Exclusive mutable borrowing |
| `Box<T>` | `std::unique_ptr<T>` | Heap ownership |
| `Rc<T>` | `std::shared_ptr<T>` without thread-safe reference counting | Shared ownership within one thread |
| `Arc<T>` | `std::shared_ptr<T>` with atomic reference counting | Shared ownership across threads |
| `Weak<T>` | `std::weak_ptr<T>` | Non-owning reference to shared ownership |

These are analogies, not exact equivalences. Rust references carry compiler-checked lifetime constraints that ordinary C++ references and pointers do not enforce.

---

# 7\. Structs, methods, and encapsulation

Rust uses structs to group related data. Unlike C++, structs do not automatically support inheritance, but they can have methods and implement traits.

## 7.1 Defining a struct

C++:

```
struct Point {
    double x;
    double y;
};
```

Rust:

```
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p = Point {
        x: 3.0,
        y: 4.0,
    };

    println!("{}, {}", p.x, p.y);
}
```

Struct fields are private to their defining module by default.

Use `pub` when a field must be accessible outside the module.

```
pub struct Point {
    pub x: f64,
    pub y: f64,
}
```

This is an important difference from C++'s default `public` access in a `struct`.

## 7.2 Mutable structs

```
struct Counter {
    value: i32,
}

fn main() {
    let mut counter = Counter { value: 0 };

    counter.value += 1;

    println!("{}", counter.value);
}
```

The binding must be mutable to modify its fields directly.

Rust does not automatically provide a `this` pointer. Methods use `self` explicitly.

## 7.3 Methods and associated functions

```
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }
}

fn main() {
    let mut rectangle = Rectangle::new(10.0, 5.0);

    println!("{}", rectangle.area());

    rectangle.scale(2.0);

    println!("{}", rectangle.area());
}
```

The `impl` block defines methods and associated functions.

Three common receiver forms are:

```
fn inspect(&self)
fn modify(&mut self)
fn consume(self)
```

They correspond to different ownership requirements:

- `&self`: Borrow the instance immutably.
- `&mut self`: Borrow the instance mutably.
- `self`: Take ownership of the instance.

The `new` function is an associated function, not a special language-level constructor. Rust does not have constructors in exactly the same sense as C++.

`Self` refers to the implementing type.

## 7.4 Builder-style APIs

A common Rust pattern is to consume a value and return a modified one.

```
struct Config {
    width: u32,
    height: u32,
}

impl Config {
    fn new() -> Self {
        Self {
            width: 800,
            height: 600,
        }
    }

    fn width(mut self, width: u32) -> Self {
        self.width = width;
        self
    }

    fn height(mut self, height: u32) -> Self {
        self.height = height;
        self
    }
}

fn main() {
    let config = Config::new()
        .width(1920)
        .height(1080);

    println!("{}x{}", config.width, config.height);
}
```

This is possible because the methods take ownership of `self` and return it.

The pattern is particularly useful for configuration objects and fluent APIs.

---

# 8\. Enums and pattern matching

Rust enums are significantly more powerful than traditional C++ enums.

## 8.1 Basic enums

```
enum Direction {
    North,
    South,
    East,
    West,
}

fn main() {
    let direction = Direction::North;

    match direction {
        Direction::North => println!("Going north"),
        Direction::South => println!("Going south"),
        Direction::East => println!("Going east"),
        Direction::West => println!("Going west"),
    }
}
```

Unlike an ordinary C++ enum, a Rust enum can contain data in each variant.

## 8.2 Enums with associated data

```
enum Message {
    Quit,
    Text(String),
    Move { x: i32, y: i32 },
    ChangeColor(u8, u8, u8),
}

fn process(message: Message) {
    match message {
        Message::Quit => {
            println!("Quit requested");
        }
        Message::Text(text) => {
            println!("Text: {text}");
        }
        Message::Move { x, y } => {
            println!("Move to {x}, {y}");
        }
        Message::ChangeColor(r, g, b) => {
            println!("RGB: {r}, {g}, {b}");
        }
    }
}
```

This enum represents four different message structures.

The compiler guarantees that every variant is handled, unless you explicitly use a wildcard or otherwise cover all remaining patterns.

### C++ comparison

A similar design in C++ might use `std::variant`:

```
using Message = std::variant<
    QuitMessage,
    TextMessage,
    MoveMessage,
    ColorMessage
>;
```

Rust's enum combines the concept of a tagged union with language-level pattern matching.

It is commonly used for:

- Protocol messages
- Abstract syntax trees
- State machines
- Command representations
- Domain models
- Error types

## 8.3 `if let`

When you care about only one variant, `if let` can be more concise than a full `match`.

```
enum Status {
    Ready,
    Failed(String),
}

fn main() {
    let status = Status::Failed("Network error".to_string());

    if let Status::Failed(message) = status {
        println!("Failure: {message}");
    }
}
```

For cases with an optional value, this pattern is especially useful.

## 8.4 `let else`

You can also use `let else` to handle an unexpected pattern and exit the current control-flow path.

```
fn process(value: Option<i32>) {
    let Some(number) = value else {
        println!("No value available");
        return;
    };

    println!("Value: {number}");
}
```

This is helpful when a function should proceed only if certain conditions hold.

---

# 9\. Strings, arrays, vectors, and slices

String handling is one of the most noticeable differences between Rust and C++.

## 9.1 `String` versus `&str`

Rust has two major string types:

- `String`: An owned, growable UTF-8 string.
- `&str`: A borrowed view into UTF-8 string data.

Example:

```
fn main() {
    let literal: &str = "Hello";
    let mut owned: String = String::from("World");

    owned.push('!');
    owned.push_str(" Rust");

    println!("{literal}");
    println!("{owned}");
}
```

The string literal is stored in the program's binary and borrowed through `&str`.

The `String` owns its contents and can grow dynamically.

### C++ comparison

| Rust | Rough C++ equivalent |
| --- | --- |
| `&str` | `std::string_view` or a borrowed character range |
| `String` | `std::string` |
| `&String` | `const std::string&`, with some differences |
| `String::from("abc")` | `std::string("abc")` |

Prefer `&str` for read-only string parameters when ownership is not required.

## 9.2 String concatenation

```
fn main() {
    let first = String::from("Hello");
    let second = String::from(" Rust");

    let combined = first + &second;

    println!("{combined}");

    // `first` was moved into the concatenation.
    // `second` remains usable.
    println!("{second}");
}
```

The `+` operator for `String` takes ownership of its left operand and borrows its right operand.

This can surprise C++ programmers because ordinary C++ string concatenation typically does not invalidate the left operand.

For formatting multiple values, `format!` is often clearer:

```
let language = "Rust";
let version = 2024;

let message = format!("{language} edition {version}");

println!("{message}");
```

`format!` creates a new `String` without taking ownership of the variables being formatted.

## 9.3 UTF-8 and character indexing

Rust strings are UTF-8 encoded.

You cannot directly index a string by character position:

```
let text = String::from("hello");

// let ch = text[0]; // Compile-time error
```

This restriction exists because a character's UTF-8 representation can occupy multiple bytes.

For example, a string containing `é` may represent that character using two UTF-8 bytes.

Rust distinguishes:

- Bytes
- Unicode scalar values (`char`)
- Grapheme clusters, which more closely correspond to user-perceived characters

Iterate over Unicode scalar values:

```
fn main() {
    let text = "héllo";

    for ch in text.chars() {
        println!("{ch}");
    }
}
```

Iterate over bytes:

```
for byte in text.bytes() {
    println!("{byte}");
}
```

Use the `unicode-segmentation` crate if your application needs to split text into grapheme clusters.

Do not assume that `chars().count()` gives the number of user-perceived characters.

## 9.4 Arrays

Rust arrays have a fixed length encoded in their type.

```
fn main() {
    let numbers: [i32; 4] = [10, 20, 30, 40];

    println!("{}", numbers[0]);
    println!("Length: {}", numbers.len());
}
```

The type `[i32; 4]` means an array of four `i32` values.

This resembles:

```
int numbers[4] = {10, 20, 30, 40};
```

However, Rust arrays integrate more directly with the type system and standard library.

## 9.5 Vectors

A `Vec<T>` is a growable, heap-allocated collection.

```
fn main() {
    let mut numbers: Vec<i32> = vec![10, 20, 30];

    numbers.push(40);
    numbers.push(50);

    println!("{numbers:?}");
}
```

The macro `vec!` initializes a vector.

Common methods include:

```
numbers.push(60);
numbers.pop();
numbers.len();
numbers.is_empty();
numbers.clear();
```

Rust's `Vec<T>` is broadly comparable to C++'s `std::vector<T>`.

### Safe element access

Indexing can panic when the index is out of bounds:

```
let numbers = vec![10, 20, 30];
println!("{}", numbers[0]);
```

When an index may be invalid, use `get`:

```
fn main() {
    let numbers = vec![10, 20, 30];

    match numbers.get(10) {
        Some(value) => println!("{value}"),
        None => println!("Index out of range"),
    }
}
```

This returns an `Option<&T>` rather than panicking.

## 9.6 Slices

A slice is a borrowed view of a sequence.

```
fn sum(values: &[i32]) -> i32 {
    values.iter().sum()
}

fn main() {
    let array = [1, 2, 3, 4];
    let vector = vec![5, 6, 7, 8];

    println!("{}", sum(&array));
    println!("{}", sum(&vector));
}
```

The `&[i32]` parameter accepts a borrowed slice of integers, whether the data comes from an array, vector, or another compatible sequence.

This is similar to designing a C++ function that accepts `std::span<const int>`.

It is often preferable to accepting a particular collection type when the function only needs to inspect a contiguous sequence.

## 9.7 Other collections

Rust's standard library provides several useful collection types.

| Rust type | Purpose | C++ analogue |
| --- | --- | --- |
| `Vec<T>` | Growable contiguous sequence | `std::vector<T>` |
| `VecDeque<T>` | Double-ended queue | `std::deque<T>` |
| `LinkedList<T>` | Doubly linked list | `std::list<T>` |
| `HashMap<K, V>` | Hash map | `std::unordered_map<K, V>` |
| `BTreeMap<K, V>` | Ordered map | `std::map<K, V>` |
| `HashSet<T>` | Hash set | `std::unordered_set<T>` |
| `BTreeSet<T>` | Ordered set | `std::set<T>` |
| `BinaryHeap<T>` | Priority queue | `std::priority_queue<T>` |

Example:

```
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();

    scores.insert("Alice", 95);
    scores.insert("Bob", 88);

    if let Some(score) = scores.get("Alice") {
        println!("Alice scored {score}");
    }
}
```

One important difference from C++ is that `HashMap::get` returns an `Option` containing a reference to the value.

---

# 10\. Error handling: `Option`, `Result`, and `?`

Rust generally encourages explicit error handling through return types rather than exceptions.

C++ supports exceptions and also has error-code conventions and types such as `std::optional` and `std::expected`.

Rust provides two central enums:

- `Option<T>`: A value may or may not exist.
- `Result<T, E>`: An operation may succeed or fail.

## 10.1 `Option<T>`

Conceptually:

```
enum Option<T> {
    Some(T),
    None,
}
```

This is a simplified representation of the standard library type.

Example:

```
fn find_user(id: u32) -> Option<String> {
    if id == 1 {
        Some(String::from("Alice"))
    } else {
        None
    }
}

fn main() {
    match find_user(1) {
        Some(name) => println!("Found: {name}"),
        None => println!("User not found"),
    }
}
```

This is similar to `std::optional<T>`.

Rust does not use null for ordinary references. Instead, optionality is represented explicitly in the type.

## 10.2 `Result<T, E>`

Conceptually:

```
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

This is the usual return type for fallible operations.

```
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(10.0, 2.0) {
        Ok(value) => println!("Result: {value}"),
        Err(error) => println!("Error: {error}"),
    }
}
```

For floating-point division, actual IEEE 754 behavior can include infinities and NaNs, so this example deliberately imposes a separate application-level error policy.

### C++ comparison

```
std::expected<double, std::string>
divide(double a, double b);
```

`Result<T, E>` is conceptually similar to `std::expected<T, E>` in C++23.

Rust does not require every error to be represented by `Result`; panics remain available for unrecoverable failures and violated assumptions.

## 10.3 The `?` operator

The `?` operator propagates errors to the caller.

Consider reading a file:

```
use std::fs;
use std::io;

fn read_file(path: &str) -> Result<String, io::Error> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}
```

If reading succeeds, execution continues.

If reading fails, the error is returned immediately from the function.

The `?` operator can also propagate `None` in a function returning `Option`, and it works with other compatible residual types.

This is usually much cleaner than manually matching every fallible operation.

## 10.4 Chaining fallible operations

```
fn parse_double(input: &str) -> Result<i32, std::num::ParseIntError> {
    let value = input.parse::<i32>()?;

    Ok(value * 2)
}
```

You can propagate parsing errors without manually converting them to strings.

For more complex applications, define a dedicated error enum or use a library such as `thiserror` to reduce repetitive error-type implementations.

## 10.5 `unwrap` and `expect`

You will often see:

```
let value = Some(42).unwrap();
```

If the value is `Some(42)`, it returns `42`. If the value is `None`, it panics.

Similarly:

```
let content = std::fs::read_to_string("data.txt")
    .expect("Could not read data.txt");
```

`expect` panics on error and includes a supplied message.

These methods are useful in examples, tests, prototypes, and places where failure is deliberately treated as fatal.

For production code that should recover from failure, prefer explicit handling or `?`.

## 10.6 Designing error types

A practical application may define:

```
use std::fmt;

#[derive(Debug)]
enum AppError {
    InvalidInput,
    NotFound,
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            AppError::InvalidInput => write!(f, "Invalid input"),
            AppError::NotFound => write!(f, "Resource not found"),
        }
    }
}

impl std::error::Error for AppError {}
```

This allows your error type to participate in Rust's standard error-handling ecosystem.

For a large application, you might add underlying error sources, contextual information, and conversions between lower-level and application-level errors.

---

# 11\. Generics and traits

C++ programmers will recognize Rust generics as a counterpart to templates. Rust traits provide shared behavior and support static and dynamic polymorphism.

## 11.1 Generic functions

C++:

```
template <typename T>
T maximum(T a, T b) {
    return a > b ? a : b;
}
```

Rust:

```
fn maximum<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        a
    } else {
        b
    }
}

fn main() {
    println!("{}", maximum(10, 20));
    println!("{}", maximum(3.5, 2.1));
}
```

The `T: PartialOrd` constraint says that `T` must implement `PartialOrd`, which provides partial ordering operations.

Unlike a C++ template, which may be accepted until a particular operation fails during instantiation, Rust generally requires the capabilities used by a generic function to be declared through trait bounds.

The bound also makes the function's requirements explicit.

## 11.2 Multiple generic parameters

```
fn pair<A, B>(first: A, second: B) -> (A, B) {
    (first, second)
}

fn main() {
    let result = pair("Rust", 42);

    println!("{:?}", result);
}
```

The two parameters can have different types.

Generic functions are often monomorphized: the compiler generates specialized machine code for concrete types used by the program.

This is similar to C++ template instantiation and helps Rust achieve zero-cost abstractions.

## 11.3 Defining traits

A trait describes behavior that a type can implement.

```
trait Drawable {
    fn draw(&self);
}

struct Circle {
    radius: f64,
}

struct Square {
    side: f64,
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle of radius {}", self.radius);
    }
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Drawing a square of side {}", self.side);
    }
}
```

This resembles a C++ abstract base class:

```
struct Drawable {
    virtual void draw() const = 0;
    virtual ~Drawable() = default;
};
```

But the mechanisms are different.

Rust traits define shared behavior without requiring class inheritance.

A type can implement multiple traits, and unrelated types can implement the same trait.

## 11.4 Static polymorphism with trait bounds

```
trait Drawable {
    fn draw(&self);
}

struct Circle;

impl Drawable for Circle {
    fn draw(&self) {
        println!("Circle");
    }
}

fn render<T: Drawable>(item: &T) {
    item.draw();
}

fn main() {
    let circle = Circle;

    render(&circle);
}
```

The generic function is resolved using the concrete type.

This is a common way to write reusable, statically dispatched code.

You can express the same requirement using `impl Trait`:

```
fn render(item: &impl Drawable) {
    item.draw();
}
```

For a function parameter, this is a convenient way to declare that the argument implements a trait.

## 11.5 Dynamic dispatch with trait objects

Sometimes you want a collection containing multiple concrete types that implement the same behavior.

Use a trait object:

```
trait Drawable {
    fn draw(&self);
}

struct Circle;

struct Square;

impl Drawable for Circle {
    fn draw(&self) {
        println!("Circle");
    }
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Square");
    }
}

fn main() {
    let shapes: Vec<Box<dyn Drawable>> = vec![
        Box::new(Circle),
        Box::new(Square),
    ];

    for shape in &shapes {
        shape.draw();
    }
}
```

The `dyn Drawable` type enables dynamic dispatch.

The `Box` values provide owned heap allocation for the heterogeneous objects.

### Static versus dynamic dispatch

| Property | Generic trait bound | Trait object |
| --- | --- | --- |
| Example | `T: Drawable` | `dyn Drawable` |
| Dispatch | Generally static | Dynamic |
| Typical performance | No virtual-dispatch requirement | Indirect call through a vtable |
| Different concrete types in one collection | Not directly in a homogeneous `Vec<T>` | Yes, through a common trait object |
| Code generation | May generate specialized versions | Can share dispatch-oriented code |

Neither approach is universally superior.

Use static dispatch when concrete types and optimization are important. Use trait objects when runtime flexibility and heterogeneous collections are useful.

## 11.6 Default trait methods

Traits can provide default implementations:

```
trait Animal {
    fn name(&self) -> &str;

    fn speak(&self) {
        println!("{} makes a sound", self.name());
    }
}

struct Dog;

impl Animal for Dog {
    fn name(&self) -> &str {
        "Dog"
    }
}

fn main() {
    let dog = Dog;

    dog.speak();
}
```

The `Dog` type receives the default `speak` implementation.

It only needs to provide `name`.

## 11.7 Common standard traits

Rust's standard library provides traits that express common behavior.

| Trait | Purpose | Approximate C++ connection |
| --- | --- | --- |
| `Copy` | Implicit value copying | Trivial value-copy semantics |
| `Clone` | Explicit cloning | Copying through a member or free function |
| `Debug` | Developer-oriented formatting | Debug printers or stream-based diagnostics |
| `Display` | User-facing formatting | Often `operator<<` |
| `PartialEq` | Partial equality comparison | `operator==` |
| `Eq` | Full equivalence equality contract | Stronger equality semantics |
| `PartialOrd` | Partial ordering | Comparison operators |
| `Ord` | Total ordering | Strict weak/total ordering interfaces, with different contracts |
| `Default` | Default value | Default construction |
| `Iterator` | Iterator behavior | STL iterator and range concepts |
| `From` / `Into` | Value conversions | Conversion constructors and operators |
| `Drop` | Cleanup when a value is dropped | Destructor |
| `Send` | Safe transfer across threads | A property enforced by Rust's type system |
| `Sync` | Safe sharing across threads | A property enforced by Rust's type system |

Traits can also be derived automatically when appropriate:

```
#[derive(Debug, Clone, PartialEq)]
struct User {
    id: u64,
    name: String,
}

fn main() {
    let user = User {
        id: 1,
        name: String::from("Alice"),
    };

    println!("{user:?}");

    let copy = user.clone();

    assert_eq!(user, copy);
}
```

The `derive` attribute asks the compiler to generate implementations for supported traits.

Note that `Clone` here performs an explicit clone of the owned `String`; `User` does not automatically become `Copy`.

---

# 12\. Closures and iterators

Rust's iterator and closure APIs are especially useful for programmers accustomed to modern C++ ranges and algorithms.

## 12.1 Closures

A closure is an anonymous function that can capture values from its surrounding environment.

```
fn main() {
    let multiplier = 3;

    let multiply = |x: i32| x * multiplier;

    println!("{}", multiply(10));
}
```

The closure captures `multiplier` from the environment.

A similar C++ example would be:

```
int multiplier = 3;

auto multiply = [multiplier](int x) {
    return x * multiplier;
};
```

Rust often infers closure parameter and return types:

```
let add = |a, b| a + b;

println!("{}", add(10, 20));
```

## 12.2 Closure capture modes

Closures can capture values in several ways.

- By immutable borrow.
- By mutable borrow.
- By taking ownership.

The compiler determines the requirements based on how the closure uses captured values, unless you use the `move` keyword.

```
fn main() {
    let text = String::from("Hello");

    let print_text = || {
        println!("{text}");
    };

    print_text();
    println!("{text}");
}
```

The closure only needs an immutable borrow of `text`.

Now consider:

```
fn main() {
    let text = String::from("Hello");

    let consume_text = move || {
        println!("{text}");
    };

    consume_text();

    // text is no longer usable here.
}
```

The `move` keyword forces the closure to capture referenced variables by value. For non-`Copy` values such as `String`, that generally transfers ownership.

A subtle point: `move` does not necessarily mean every captured value is physically moved. For `Copy` types, the capture can copy the value.

## 12.3 Iterators

C++:

```
std::vector<int> numbers = {1, 2, 3, 4, 5};

for (const auto& n : numbers) {
    std::cout << n << '\n';
}
```

Rust:

```
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    for number in numbers.iter() {
        println!("{number}");
    }
}
```

Rust provides three especially important iterator methods:

```
numbers.iter()
numbers.iter_mut()
numbers.into_iter()
```

They differ in ownership:

- `iter()` produces references to the elements.
- `iter_mut()` produces mutable references to the elements.
- `into_iter()` consumes the collection and yields its elements by value, subject to the relevant type and iteration context.

For example:

```
fn main() {
    let numbers = vec![1, 2, 3];

    let sum: i32 = numbers.iter().sum();

    println!("{sum}");
    println!("{numbers:?}");
}
```

The vector remains usable because the iterator borrows its elements.

## 12.4 Iterator adapters

Rust's iterators support operations such as `map`, `filter`, `take`, `flat_map`, `enumerate`, and `fold`.

```
fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6];

    let result: Vec<i32> = numbers
        .iter()
        .filter(|&&x| x % 2 == 0)
        .map(|&x| x * x)
        .collect();

    println!("{result:?}");
}
```

Output:

```
[4, 16, 36]
```

The pipeline filters even numbers, squares them, and collects the results into a vector.

A simpler equivalent uses copied values:

```
let result: Vec<i32> = numbers
    .iter()
    .copied()
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .collect();
```

The `.copied()` call copies each `i32` from its reference.

This version is often easier to read.

## 12.5 Lazy evaluation

Most iterator adapters are lazy.

For example:

```
let numbers = vec![1, 2, 3];

let doubled = numbers.iter().map(|x| x * 2);
```

At this point, the transformation has not necessarily been performed for every element. The iterator describes the operation.

To consume it:

```
let result: Vec<i32> = doubled.copied().collect();
```

The iterator is evaluated as it is consumed.

This resembles C++20 ranges and views.

## 12.6 Avoid unnecessary intermediate collections

Instead of:

```
let doubled: Vec<i32> = numbers
    .iter()
    .map(|x| x * 2)
    .copied()
    .collect();
```

you can often chain the next operation directly:

```
let total: i32 = numbers
    .iter()
    .map(|x| x * 2)
    .sum();
```

This avoids allocating an intermediate vector.

The compiler can often optimize iterator pipelines efficiently, although actual performance should be measured rather than assumed.

---

# 13\. Modules, crates, and Cargo

Rust has a built-in module system and a standard package manager.

## 13.1 Package structure

A Cargo package contains a `Cargo.toml` manifest.

A package can contain one or more crates, such as a library crate and executable crates.

A crate is a compilation unit.

The `src/main.rs` file defines a binary crate, while `src/lib.rs` defines a library crate.

A simple library project might look like:

```
my_project/
├── Cargo.toml
├── src/
│   ├── lib.rs
│   └── main.rs
└── tests/
    └── integration_test.rs
```

## 13.2 Defining modules

Suppose your project contains:

```
src/
├── main.rs
└── math.rs
```

In `math.rs`:

```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

In `main.rs`:

```
mod math;

fn main() {
    println!("{}", math::add(10, 20));
}
```

The declaration `mod math;` tells Rust to include the module.

The `pub` keyword makes `add` visible outside its defining module.

## 13.3 Nested modules

```
mod geometry {
    pub mod circle {
        pub fn area(radius: f64) -> f64 {
            std::f64::consts::PI * radius * radius
        }
    }
}

fn main() {
    let area = geometry::circle::area(5.0);

    println!("{area}");
}
```

The `pub` visibility modifier is needed at each relevant level to expose the item outside its parent module.

Rust also provides `pub(crate)`, `pub(super)`, and `pub(in path)` for narrower visibility.

## 13.4 Imports

Use `use` to bring names into scope:

```
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();

    map.insert("language", "Rust");
}
```

This resembles `using` declarations in C++, but Rust's module paths and visibility rules are different.

## 13.5 Cargo dependencies

To add an external library, edit `Cargo.toml`:

```
[package]
name = "my_project"
version = "0.1.0"
edition = "2024"

[dependencies]
serde = { version = "1", features = ["derive"] }
```

The `serde` crate is commonly used for serialization and deserialization.

Then use it in your code:

```
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct User {
    id: u64,
    name: String,
}
```

The example defines a serializable data type. To serialize it into JSON, you would also add a JSON library such as `serde_json`.

Cargo manages dependency resolution, compilation, and the lockfile.

## 13.6 `Cargo.lock`

Cargo commonly generates a `Cargo.lock` file recording the resolved dependency versions.

For applications and executables, committing the lockfile is generally recommended so that builds use reproducible dependency selections.

For published libraries, the conventions around lockfiles differ because downstream consumers resolve dependencies in their own projects.

---

# 14\. Smart pointers and memory management

Rust's ownership model does not eliminate heap allocation. Instead, it makes the ownership rules explicit.

## 14.1 `Box<T>`

`Box<T>` provides owned heap allocation.

```
fn main() {
    let value = Box::new(42);

    println!("{value}");
}
```

Use `Box<T>` when:

- You need an owned heap allocation.
- A recursive type needs indirection.
- You want to store a large value indirectly.
- You need an owned concrete value behind a trait object.

For example:

```
enum List {
    Cons(i32, Box<List>),
    Nil,
}
```

Without `Box<List>`, the compiler could not determine the size of this recursive type.

## 14.2 `Rc<T>`: Shared ownership in one thread

`Rc<T>` provides reference-counted shared ownership.

```
use std::rc::Rc;

fn main() {
    let first = Rc::new(String::from("Hello"));

    let second = Rc::clone(&first);
    let third = Rc::clone(&first);

    println!("{first}");
    println!("{second}");
    println!("{third}");

    println!("Owners: {}", Rc::strong_count(&first));
}
```

`Rc::clone` increments the reference count; it does not clone the underlying string.

Use `Rc<T>` when multiple parts of a single-threaded program need to own the same allocation.

`Rc<T>` is not suitable for ordinary cross-thread shared ownership.

Reference cycles can prevent allocations from being freed, so `Rc` and `RefCell` designs need care when cyclic graphs are involved.

## 14.3 `Arc<T>`: Shared ownership across threads

`Arc<T>` uses atomic reference counting and is suitable for shared ownership across threads when its contained type satisfies the required thread-safety constraints.

```
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![10, 20, 30]);

    let shared = Arc::clone(&data);

    let handle = thread::spawn(move || {
        println!("{shared:?}");
    });

    handle.join().unwrap();

    println!("{data:?}");
}
```

The cloned `Arc` shares ownership of the same vector allocation.

However, `Arc<T>` does not automatically make `T` safe for concurrent mutation. Shared mutation requires additional synchronization or a suitable atomic type.

## 14.4 `RefCell<T>`: Runtime borrowing checks

Ordinary references use compile-time borrowing rules.

`RefCell<T>` instead checks borrowing rules at runtime.

```
use std::cell::RefCell;

fn main() {
    let value = RefCell::new(10);

    *value.borrow_mut() += 5;

    println!("{}", value.borrow());
}
```

The value can be mutated through `RefCell` even though the binding itself does not need to be declared `mut`.

If conflicting borrows occur, the program panics at runtime.

This is a trade-off: more flexibility, but with runtime checks and the possibility of panics.

`RefCell<T>` is not a thread-safe synchronization primitive.

## 14.5 Interior mutability and shared ownership

You will frequently encounter combinations such as:

```
Rc<RefCell<T>>
```

or:

```
Arc<Mutex<T>>
```

The first is a common pattern for single-threaded shared ownership with mutation.

The second is a common pattern for thread-safe shared ownership with synchronized mutation.

These are tools for specific ownership problems, not defaults for every object.

Prefer ordinary ownership and borrowing whenever they adequately express the design.

## 14.6 RAII and `Drop`

Rust uses deterministic destruction through its `Drop` trait.

```
struct Resource {
    name: String,
}

impl Drop for Resource {
    fn drop(&mut self) {
        println!("Dropping {}", self.name);
    }
}

fn main() {
    let _resource = Resource {
        name: String::from("Database connection"),
    };

    println!("Function is running");
}
```

When `_resource` goes out of scope, Rust calls its destructor-like `drop` method.

This resembles C++ RAII and destructors.

The `_resource` binding also illustrates an important convention: a name beginning with an underscore suppresses the unused-variable warning without discarding the value immediately. By contrast, `_` itself is a discard pattern.

Rust generally drops local variables when they leave scope, subject to ownership transfers and compiler rules. The exact timing of some temporaries and explicitly dropped values can matter in advanced code.

---

# 15\. Lifetimes: Making reference validity explicit

Lifetimes are often the most challenging Rust concept for experienced C++ programmers.

The core idea is straightforward:

**A reference must never outlive the value it references.**

The borrow checker infers lifetimes in many cases. Explicit lifetime annotations are needed when the relationships between references cannot be inferred from local rules alone.

## 15.1 The dangling-reference problem

Consider this invalid example:

```
// Invalid Rust:
//
// fn create_reference() -> &String {
//     let text = String::from("Hello");
//     &text
// }
```

The function tries to return a reference to a local `String`.

The local value is destroyed when the function returns, so the reference would dangle.

Rust rejects this code.

In C++, the analogous bug may compile:

```
const std::string& create_reference() {
    std::string text = "Hello";
    return text; // Dangling reference
}
```

This is one of the most important safety differences between the languages.

## 15.2 Lifetime annotations

Consider a function that returns the longer of two string slices.

```
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() {
        x
    } else {
        y
    }
}
```

The lifetime parameter `'a` expresses a relationship between the input references and the returned reference.

The return value cannot be used for longer than the lifetime guaranteed by both input references.

Example:

```
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() >= y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let first = String::from("Rust");
    let second = String::from("C++");

    let result = longest(&first, &second);

    println!("{result}");
}
```

The annotation does not extend the life of either string. It tells the compiler how the validity of the returned reference relates to the inputs.

## 15.3 Lifetimes are not runtime objects

A lifetime annotation:

```
'a
```

does not create a runtime timer or keep an object alive.

It is a compile-time constraint used to validate references.

This differs from `std::shared_ptr` in C++, which extends an object's lifetime through runtime reference counting.

In Rust, lifetimes describe validity; ownership determines who is responsible for a value's destruction.

## 15.4 Structs containing references

A struct that stores a borrowed reference must specify the lifetime relationship.

```
struct Article<'a> {
    title: &'a str,
    body: &'a str,
}

fn main() {
    let title = String::from("Rust");
    let body = String::from("Memory safety without a garbage collector.");

    let article = Article {
        title: &title,
        body: &body,
    };

    println!("{}: {}", article.title, article.body);
}
```

The lifetime parameter communicates that the struct cannot be used to access these references beyond their validity.

In application design, storing owned strings may sometimes be simpler:

```
struct Article {
    title: String,
    body: String,
}
```

This eliminates the external lifetime dependency, at the cost of owning the text.

## 15.5 Lifetime elision

Rust can infer many lifetime relationships without explicit annotations.

For example:

```
fn first_word(text: &str) -> &str {
    text.split_whitespace().next().unwrap_or("")
}
```

You do not need to write:

```
fn first_word<'a>(text: &'a str) -> &'a str {
    text.split_whitespace().next().unwrap_or("")
}
```

The two signatures express the same lifetime relationship in this case.

### Practical advice for C++ programmers

When learning Rust, do not begin by adding lifetime annotations everywhere.

Instead:

1. Start with ordinary references.
2. Let the compiler infer lifetimes where possible.
3. Read borrow-checker errors carefully.
4. Add explicit lifetime parameters when the type relationship requires them.
5. Consider whether the design should own the data instead of borrowing it.

Lifetimes become much easier once ownership and borrowing are already familiar.

---

# 16\. Concurrency and multithreading

Rust's type system is designed to prevent data races in safe code.

A data race occurs when multiple threads access the same memory concurrently, at least one access is a write, and the accesses are not properly synchronized.

Rust's ownership system and thread-safety traits help prevent such situations at compile time.

## 16.1 Creating threads

```
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Hello from a thread!");
    });

    handle.join().unwrap();
}
```

`thread::spawn` starts a new thread and returns a join handle.

Calling `join()` waits for that thread to finish.

## 16.2 Moving data into a thread

```
use std::thread;

fn main() {
    let message = String::from("Hello from Rust");

    let handle = thread::spawn(move || {
        println!("{message}");
    });

    handle.join().unwrap();
}
```

The `move` closure transfers ownership of `message` into the new thread.

This is important because the spawned thread may outlive the stack frame that originally contained the variable.

Rust requires spawned thread closures to satisfy the necessary ownership and thread-safety bounds.

## 16.3 Sharing data with `Arc`

Suppose multiple threads need to read the same data.

```
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![1, 2, 3, 4]);

    let mut handles = Vec::new();

    for _ in 0..3 {
        let shared_data = Arc::clone(&data);

        let handle = thread::spawn(move || {
            println!("{shared_data:?}");
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```

Each thread gets a cloned `Arc`, but all clones point to the same underlying vector.

Because the vector is only read, additional mutation synchronization is unnecessary.

## 16.4 `Mutex<T>`

To coordinate mutable access across threads, use a mutex.

```
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));

    let mut handles = Vec::new();

    for _ in 0..10 {
        let counter = Arc::clone(&counter);

        let handle = thread::spawn(move || {
            let mut value = counter.lock().unwrap();

            *value += 1;
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Counter: {}", *counter.lock().unwrap());
}
```

Output:

```
Counter: 10
```

The mutex ensures that only one thread holds the lock for mutable access at a time.

`Arc` provides shared ownership. `Mutex` provides synchronization. They solve different problems.

## 16.5 Atomic types

For simple numeric operations, atomic types can avoid a mutex.

```
use std::sync::atomic::{AtomicUsize, Ordering};

fn main() {
    let counter = AtomicUsize::new(0);

    counter.fetch_add(1, Ordering::Relaxed);

    println!("{}", counter.load(Ordering::Relaxed));
}
```

`Ordering::Relaxed` guarantees atomicity of the operation but does not establish additional synchronization ordering with other memory operations.

Choosing an ordering correctly requires understanding the synchronization relationship your program needs.

For simple independent counters, relaxed ordering can be appropriate. For publishing or coordinating other shared state, stronger ordering or locks may be necessary.

## 16.6 Channels

Channels allow threads to communicate by sending messages.

```
use std::sync::mpsc;
use std::thread;

fn main() {
    let (sender, receiver) = mpsc::channel();

    thread::spawn(move || {
        sender.send(String::from("Hello")).unwrap();
    });

    let message = receiver.recv().unwrap();

    println!("{message}");
}
```

The sender transfers a `String` through the channel.

This approach can reduce the need for shared mutable state.

### Concurrency summary

| Requirement | Typical Rust solution |
| --- | --- |
| Start a thread | `std::thread::spawn` |
| Share immutable data across threads | `Arc<T>` |
| Protect shared mutable data | `Mutex<T>` |
| Read/write access with multiple readers | `RwLock<T>` |
| Simple atomic counters | `AtomicUsize` or another atomic type |
| Send messages between threads | Channels |
| Single-threaded shared ownership | `Rc<T>` |
| Single-threaded interior mutability | `RefCell<T>` |

Two important traits are:

- `Send`: A type can be transferred safely between threads.
- `Sync`: A type can be shared by reference between threads.

These traits are automatically implemented for many types when their components satisfy the required properties.

The compiler uses them to reject many unsafe thread-sharing patterns.

---

# 17\. Asynchronous programming

Rust supports asynchronous programming through `async`, `await`, and the `Future` trait.

Unlike languages with a built-in asynchronous runtime, Rust generally uses an external runtime library to execute asynchronous tasks.

Popular runtimes include Tokio and async-std.

## 17.1 An async function

```
async fn calculate() -> i32 {
    42
}
```

Calling an async function creates a future representing the computation.

It does not necessarily execute the entire computation immediately.

To await the result, you need an asynchronous execution context.

## 17.2 A Tokio example

Add Tokio to `Cargo.toml`:

```
[dependencies]
tokio = { version = "1", features = ["macros", "rt-multi-thread", "time"] }
```

Then write:

```
use tokio::time::{sleep, Duration};

async fn perform_task() {
    println!("Task started");

    sleep(Duration::from_secs(1)).await;

    println!("Task finished");
}

#[tokio::main]
async fn main() {
    perform_task().await;
}
```

The `#[tokio::main]` macro sets up a Tokio runtime.

The `await` expression suspends the current asynchronous task when its future is pending, allowing the runtime to schedule other work.

It does not necessarily block the operating-system thread.

## 17.3 Running multiple tasks

```
use tokio::time::{sleep, Duration};

async fn task(name: &'static str) {
    println!("{name} started");

    sleep(Duration::from_secs(1)).await;

    println!("{name} finished");
}

#[tokio::main]
async fn main() {
    tokio::join!(
        task("A"),
        task("B")
    );
}
```

The two tasks can make progress concurrently while waiting for their timers.

For I/O-bound workloads, this can allow one thread to manage many operations efficiently.

## 17.4 Async versus threads

| Threads | Async tasks |
| --- | --- |
| Often use operating-system threads | Usually scheduled by an async runtime |
| Useful for CPU-bound parallel work | Especially useful for many concurrent I/O operations |
| Blocking operations occupy the thread | Properly asynchronous operations yield while waiting |
| Thread creation and synchronization have costs | Task scheduling has its own costs |

Async is not automatically faster.

For CPU-intensive work, threads and parallel computation may be more appropriate. Blocking operations inside an asynchronous task can also reduce runtime efficiency unless handled appropriately.

---

# 18\. File I/O and practical systems programming

Let's combine ownership, borrowing, error handling, and the standard library.

## 18.1 Reading a file

```
use std::fs;
use std::io;

fn read_text(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

fn main() {
    match read_text("input.txt") {
        Ok(content) => println!("{content}"),
        Err(error) => eprintln!("Could not read file: {error}"),
    }
}
```

`read_to_string` returns an owned `String` wrapped in a `Result`.

The file's contents remain valid after the file operation completes because the returned string owns its data.

## 18.2 Writing a file

```
use std::fs;
use std::io;

fn write_text(path: &str, content: &str) -> Result<(), io::Error> {
    fs::write(path, content)
}

fn main() -> Result<(), io::Error> {
    write_text("output.txt", "Hello from Rust!\n")?;

    Ok(())
}
```

The function borrows its input text through `&str` and returns `Result<(), io::Error>`.

The unit type `()` indicates that no meaningful value needs to be returned on success.

## 18.3 Reading a file line by line

For larger files, reading everything into memory may be undesirable.

```
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn count_lines(path: &str) -> io::Result<usize> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);

    let mut count = 0;

    for line in reader.lines() {
        let _line = line?;
        count += 1;
    }

    Ok(count)
}

fn main() -> io::Result<()> {
    let count = count_lines("input.txt")?;

    println!("Lines: {count}");

    Ok(())
}
```

The `BufReader` provides buffered reading, and `lines()` yields individual lines through an iterator.

Notice that `line?` propagates I/O errors instead of silently ignoring them.

## 18.4 Command-line arguments

```
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    for arg in args {
        println!("{arg}");
    }
}
```

Build and run:

```
cargo run -- one two three
```

The `--` separates Cargo's own command-line arguments from the arguments passed to your program.

For larger command-line applications, the `clap` crate provides argument parsing, validation, help messages, and subcommands.

---

# 19\. Testing, debugging, and code quality

Rust includes a testing framework and has a strong ecosystem of development tools.

## 19.1 Unit tests

Consider this function:

```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

You can write tests in the same module:

```
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_negative_values() {
        assert_eq!(add(-2, -3), -5);
    }
}
```

Run the tests:

```
cargo test
```

The `#[test]` attribute marks a test function.

The `#[cfg(test)]` attribute includes the test module when compiling for tests.

## 19.2 Assertions

Rust provides:

```
assert!(condition);
assert_eq!(actual, expected);
assert_ne!(actual, unexpected);
```

Example:

```
#[test]
fn vector_has_expected_length() {
    let values = vec![1, 2, 3];

    assert_eq!(values.len(), 3);
}
```

If an assertion fails, the test fails and reports diagnostic information.

## 19.3 Integration tests

Create a file:

```
tests/integration_test.rs
```

Example:

```
use my_project::add;

#[test]
fn addition_works() {
    assert_eq!(add(10, 20), 30);
}
```

Replace `my_project` with your package's library crate name.

Integration tests exercise the library through its public API, much like a separate consumer would.

## 19.4 Documentation tests

Rust can test code examples in documentation.

For example:

````
/// Adds two integers.
///
/// ```
/// assert_eq!(my_project::add(2, 3), 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
````

Documentation examples can be compiled and executed by the test runner.

This helps keep examples synchronized with the actual implementation.

## 19.5 Formatting and linting

Run the formatter:

```
cargo fmt
```

Run Clippy:

```
cargo clippy
```

Run tests:

```
cargo test
```

Check compilation:

```
cargo check
```

A useful development workflow is:

```
cargo fmt --check
cargo clippy --all-targets --all-features
cargo test
cargo build --release
```

Clippy identifies common mistakes and suggests more idiomatic Rust patterns.

The formatter keeps code style consistent across a team.

## 19.6 Debugging

Rust supports debugging through standard native debugging tools and IDE integrations.

Useful techniques include:

- Printing values with `println!`.
- Printing debug representations with `println!("{value:?}")`.
- Deriving `Debug` for custom structs and enums.
- Using `dbg!(&value)` for temporary diagnostics.
- Running under a debugger such as GDB or LLDB.
- Inspecting compiler errors and suggested fixes.

For example:

```
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 10, y: 20 };

    dbg!(&point);
}
```

The compiler's borrow-checker diagnostics are also a valuable learning tool. When a borrow fails, inspect which value is borrowed, whether the borrow is mutable, and where the value or reference is used.

---

# 20\. Unsafe Rust and C/C++ interoperability

Rust's safety guarantees apply to safe Rust code under the language's assumptions. Sometimes systems programming requires operations that the compiler cannot fully verify.

Examples include:

- Dereferencing raw pointers
- Calling certain foreign functions
- Accessing mutable global state
- Implementing low-level data structures
- Interacting with hardware or operating-system interfaces

Rust provides `unsafe` for these situations.

## 20.1 Raw pointers

Rust has raw pointer types:

```
*const T
*mut T
```

They resemble C and C++ pointers more closely than references do.

For example:

```
fn main() {
    let value = 42;
    let pointer = &value as *const i32;

    unsafe {
        println!("{}", *pointer);
    }
}
```

The pointer is derived from a valid reference, and it is dereferenced while the value remains alive.

The `unsafe` block tells the compiler that the programmer is taking responsibility for the requirements of the operation.

It does not automatically make invalid operations safe.

## 20.2 What `unsafe` permits

An unsafe block allows certain operations that safe Rust forbids, such as raw-pointer dereferencing.

It does not disable all Rust checks. Ordinary type checking and many other compiler checks still apply.

Unsafe code must uphold invariants that the compiler cannot establish automatically.

In particular, unsafe code must not create invalid references, violate aliasing requirements, or access memory outside its valid lifetime.

## 20.3 Calling C functions

Rust can call functions written in C through foreign-function interfaces.

A simplified example:

```
unsafe extern "C" {
    fn abs(value: i32) -> i32;
}

fn main() {
    let value = unsafe { abs(-10) };

    println!("{value}");
}
```

The function is declared using the C ABI.

This example assumes the platform's C library provides the declared symbol with the expected signature.

In production code, prefer the standard library or established bindings when they already provide the functionality you need.

## 20.4 Calling Rust from C++

Rust libraries can expose a C-compatible API using `extern "C"` and suitable C-compatible types.

For example:

```
#[unsafe(no_mangle)]
pub extern "C" fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}
```

On editions and toolchains that require the unsafe attribute syntax, `#[unsafe(no_mangle)]` is the appropriate form. The exact library build configuration and exported symbol behavior should be verified for the target toolchain.

A matching C or C++ declaration would be:

```
extern "C" int add_numbers(int a, int b);
```

The Rust function can then be compiled into a library and linked with a C++ application.

### Important FFI rules

When crossing a language boundary, verify:

- ABI compatibility.
- Type layout and alignment.
- Ownership and allocation responsibilities.
- String representation and encoding.
- Whether pointers may be null.
- Whether exceptions or panics can cross the boundary.
- Thread-safety requirements.
- How errors are communicated.

Do not pass a Rust `String`, `Vec<T>`, or arbitrary Rust struct directly across a C ABI and assume its layout matches a C++ type.

Use appropriate C-compatible representations, explicit conversion functions, and clear ownership contracts.

For more extensive interoperability, projects such as `cxx` can simplify communication between Rust and C++.

---

# 21\. A complete practical project: Build a task manager

Now let's apply the concepts in a small command-line application.

We will build a task manager that can:

- Add tasks.
- List tasks.
- Mark tasks as completed.
- Remove tasks.
- Save tasks to a file.
- Load tasks from a file.

This project demonstrates structs, enums, ownership, borrowing, collections, error handling, pattern matching, iterators, and file I/O.

## 21.1 Create the project

```
cargo new task_manager
cd task_manager
```

Replace `src/main.rs` with the following implementation.

## 21.2 Implementation

```
use std::fs;
use std::io::{self, Write};

#[derive(Debug, Clone)]
struct Task {
    id: u32,
    title: String,
    completed: bool,
}

#[derive(Debug, Default)]
struct TaskManager {
    tasks: Vec<Task>,
    next_id: u32,
}

impl TaskManager {
    fn new() -> Self {
        Self {
            tasks: Vec::new(),
            next_id: 1,
        }
    }

    fn add_task(&mut self, title: String) {
        let task = Task {
            id: self.next_id,
            title,
            completed: false,
        };

        self.tasks.push(task);
        self.next_id += 1;
    }

    fn list_tasks(&self) {
        if self.tasks.is_empty() {
            println!("No tasks found.");
            return;
        }

        for task in &self.tasks {
            let status = if task.completed {
                "Completed"
            } else {
                "Pending"
            };

            println!(
                "[{}] {} - {}",
                task.id,
                task.title,
                status
            );
        }
    }

    fn complete_task(&mut self, id: u32) -> bool {
        match self.tasks.iter_mut().find(|task| task.id == id) {
            Some(task) => {
                task.completed = true;
                true
            }
            None => false,
        }
    }

    fn remove_task(&mut self, id: u32) -> bool {
        let original_len = self.tasks.len();

        self.tasks.retain(|task| task.id != id);

        self.tasks.len() != original_len
    }

    fn save(&self, path: &str) -> io::Result<()> {
        let mut content = String::new();

        for task in &self.tasks {
            let completed = if task.completed { "1" } else { "0" };

            content.push_str(&format!(
                "{}\t{}\t{}\n",
                task.id,
                completed,
                task.title
            ));
        }

        fs::write(path, content)
    }

    fn load(path: &str) -> io::Result<Self> {
        let content = fs::read_to_string(path)?;
        let mut manager = Self::new();

        for line in content.lines() {
            let mut parts = line.splitn(3, '\t');

            let id = parts
                .next()
                .and_then(|s| s.parse::<u32>().ok());

            let completed = parts
                .next()
                .and_then(|s| s.parse::<u8>().ok());

            let title = parts.next();

            let (Some(id), Some(completed), Some(title)) =
                (id, completed, title)
            else {
                continue;
            };

            if completed > 1 {
                continue;
            }

            manager.tasks.push(Task {
                id,
                title: title.to_string(),
                completed: completed == 1,
            });

            manager.next_id = manager.next_id.max(id.saturating_add(1));
        }

        Ok(manager)
    }
}

fn read_line() -> io::Result<String> {
    let mut input = String::new();

    io::stdin().read_line(&mut input)?;

    Ok(input.trim().to_string())
}

fn main() -> io::Result<()> {
    const FILE_PATH: &str = "tasks.txt";

    let mut manager = match TaskManager::load(FILE_PATH) {
        Ok(manager) => manager,
        Err(error) if error.kind() == io::ErrorKind::NotFound => {
            TaskManager::new()
        }
        Err(error) => return Err(error),
    };

    loop {
        println!("\n=== Task Manager ===");
        println!("1. Add task");
        println!("2. List tasks");
        println!("3. Complete task");
        println!("4. Remove task");
        println!("5. Save and exit");
        print!("Choose an option: ");

        io::stdout().flush()?;

        let choice = read_line()?;

        match choice.as_str() {
            "1" => {
                print!("Enter task title: ");
                io::stdout().flush()?;

                let title = read_line()?;

                if title.is_empty() {
                    println!("Task title cannot be empty.");
                } else {
                    manager.add_task(title);
                    println!("Task added.");
                }
            }

            "2" => {
                manager.list_tasks();
            }

            "3" => {
                print!("Enter task ID: ");
                io::stdout().flush()?;

                let input = read_line()?;

                match input.parse::<u32>() {
                    Ok(id) => {
                        if manager.complete_task(id) {
                            println!("Task completed.");
                        } else {
                            println!("Task not found.");
                        }
                    }
                    Err(_) => println!("Invalid task ID."),
                }
            }

            "4" => {
                print!("Enter task ID: ");
                io::stdout().flush()?;

                let input = read_line()?;

                match input.parse::<u32>() {
                    Ok(id) => {
                        if manager.remove_task(id) {
                            println!("Task removed.");
                        } else {
                            println!("Task not found.");
                        }
                    }
                    Err(_) => println!("Invalid task ID."),
                }
            }

            "5" => {
                manager.save(FILE_PATH)?;
                println!("Tasks saved.");
                break;
            }

            _ => {
                println!("Invalid option.");
            }
        }
    }

    Ok(())
}
```

Run it:

```
cargo run
```

### Important production considerations

This implementation is a learning project rather than a production-ready task manager.

- The tab-separated storage format does not escape tabs or newlines in task titles. A production application should use a structured format such as JSON.
- The loader skips malformed records rather than reporting them.
- Task ID overflow is not fully handled when adding tasks.
- Saving is not transactional; a failure during writing may leave an incomplete file.
- There are no automated tests yet.

These limitations provide useful exercises for extending the project.

## 21.3 Understanding the Rust concepts in the project

### Ownership

```
fn add_task(&mut self, title: String)
```

The function takes ownership of the title. The caller transfers the string into the task manager.

This avoids copying the string's contents unnecessarily.

### Mutable borrowing

```
fn complete_task(&mut self, id: u32) -> bool
```

The method borrows the task manager mutably because it changes a task's completion state.

### Immutable borrowing

```
fn list_tasks(&self)
```

Listing tasks only reads their contents, so an immutable borrow is sufficient.

### Iterators

```
self.tasks.iter_mut().find(|task| task.id == id)
```

This searches the tasks using an iterator that yields mutable references.

The `find` method returns an optional matching element.

### Pattern matching

```
match self.tasks.iter_mut().find(|task| task.id == id) {
    Some(task) => {
        task.completed = true;
        true
    }
    None => false,
}
```

The `match` expression handles both possible outcomes explicitly.

### Error handling

```
fn save(&self, path: &str) -> io::Result<()>
```

The function returns an I/O error to the caller instead of assuming that saving always succeeds.

### Borrow checker

The method signatures make access requirements explicit:

- `&self` means read access.
- `&mut self` means exclusive mutable access.

This makes the code's mutation boundaries easier to understand.

## 21.4 Exercises to improve the project

Try implementing these features yourself:

1. Add a task priority field.
2. Support editing task titles.
3. Add a command to list only incomplete tasks.
4. Add a task creation timestamp.
5. Replace tab-separated storage with JSON using `serde` and `serde_json`.
6. Add unit tests for `add_task`, `complete_task`, and `remove_task`.
7. Extract the task manager into `src/lib.rs`.
8. Add command-line arguments using `clap`.
9. Return meaningful errors for malformed task records.
10. Add atomic file replacement so an interrupted save is less likely to corrupt the task file.

These exercises will help you move from writing Rust syntax to designing Rust programs.

---

# 22\. Common mistakes C++ programmers make in Rust

Understanding these differences will save you considerable time.

## Mistake 1: Treating Rust assignment like C++ assignment

C++:

```
std::string a = "hello";
std::string b = a;
```

Both variables remain usable.

Rust:

```
let a = String::from("hello");
let b = a;

// a is no longer usable.
```

**Fix:** Use `clone()` when you need independent ownership, or borrow the value when ownership is unnecessary.

## Mistake 2: Using `String` for every string parameter

Less flexible:

```
fn print_name(name: String) {
    println!("{name}");
}
```

More flexible:

```
fn print_name(name: &str) {
    println!("{name}");
}
```

The first function takes ownership of a `String`. The second only borrows string contents.

**Fix:** Prefer borrowed parameters for read-only access unless ownership is required.

## Mistake 3: Adding `clone()` to silence every ownership error

This works:

```
let second = first.clone();
```

But it may allocate memory or duplicate expensive data.

**Fix:** Ask whether the second owner is actually necessary. Could the function accept a reference instead?

Cloning is appropriate when independent ownership is part of the design. It is not inherently bad.

## Mistake 4: Fighting the borrow checker

A common reaction to a borrow-checker error is to introduce `Arc<Mutex<T>>`, `Rc<RefCell<T>>`, or unnecessary clones.

These tools are sometimes correct, but they add complexity.

**Fix:** First examine the intended ownership structure. Determine who should own the data, who needs to read it, and who needs to mutate it.

A simpler design may eliminate the conflict.

## Mistake 5: Expecting class inheritance

Rust does not support C++-style class inheritance.

Instead, it combines:

- Structs and enums for data modeling.
- Traits for shared behavior.
- Composition for combining functionality.
- Generics for static polymorphism.
- Trait objects for dynamic polymorphism.

**Fix:** Model data using structs and enums, then express shared capabilities through traits.

## Mistake 6: Assuming every error should cause a panic

This is convenient:

```
let content = std::fs::read_to_string("data.txt").unwrap();
```

But it crashes if the file cannot be read.

**Fix:** Use `Result`, `?`, and explicit error handling when failure is recoverable.

Reserve panics for situations where continuing is not appropriate or where a violated invariant indicates a programming error.

## Mistake 7: Assuming `Arc<T>` makes everything thread-safe

`Arc<T>` makes shared ownership thread-safe, but it does not automatically make the contained value safe for arbitrary concurrent mutation.

**Fix:** Use an appropriate synchronization mechanism, such as `Mutex<T>`, or choose a type with suitable atomic behavior.

## Mistake 8: Using explicit lifetimes before understanding ownership

Lifetimes can seem intimidating when encountered too early.

**Fix:** First learn owned values, immutable references, mutable references, and scope. Then study lifetime annotations as a way to describe reference-validity relationships.

## Mistake 9: Ignoring idiomatic Rust

Valid Rust is not always idiomatic Rust.

For example, a manual loop may be less expressive than a simple iterator operation.

However, concise functional code is not automatically better. Clarity should come first.

**Fix:** Use Clippy, read standard-library documentation, and study well-maintained Rust projects.

---

# 23\. Advanced Rust concepts worth learning next

Once you are comfortable with the basics, these concepts will help you write more sophisticated systems software.

## 23.1 Const generics

Rust supports generic parameters that represent constant values, including array lengths.

```
struct Buffer<T, const N: usize> {
    data: [T; N],
}
```

You can instantiate the type with different array sizes:

```
let a: Buffer<i32, 4>;
let b: Buffer<i32, 16>;
```

These are different concrete types.

Const generics are useful for fixed-size buffers, embedded systems, numerical programming, and APIs that need array lengths encoded in the type system.

C++ programmers can compare them with non-type template parameters.

## 23.2 Macros

Rust has two major macro mechanisms:

- Declarative macros, defined with `macro_rules!`.
- Procedural macros, which operate on Rust syntax and are commonly used for derives and attributes.

For example:

```
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

fn main() {
    say_hello!();
}
```

Macros can generate code that would otherwise require repetitive implementations.

Rust also has familiar built-in macros:

```
println!("Hello");
format!("Value: {}", 42);
vec![1, 2, 3];
assert_eq!(2 + 2, 4);
```

Unlike ordinary functions, macros operate through macro expansion.

Do not use macros for everything. Ordinary functions, generics, and traits are often easier to understand and maintain.

## 23.3 Associated types

Traits can define associated types:

```
trait Container {
    type Item;

    fn get(&self) -> Option<&Self::Item>;
}

struct NumberContainer {
    value: i32,
}

impl Container for NumberContainer {
    type Item = i32;

    fn get(&self) -> Option<&Self::Item> {
        Some(&self.value)
    }
}
```

The implementation chooses the concrete type represented by `Item`.

Associated types are particularly useful for iterators, collection abstractions, and complex generic interfaces.

## 23.4 Trait bounds and `where` clauses

When a generic type has many constraints, a `where` clause can improve readability.

```
use std::fmt::Debug;

fn inspect<T>(value: &T)
where
    T: Debug + Clone,
{
    let copy = value.clone();

    println!("{copy:?}");
}
```

This resembles constraints on C++ templates, although the language mechanisms and associated semantics differ.

## 23.5 `impl Trait` in return types

You can return a value that implements a trait without exposing its concrete type in the signature:

```
fn numbers() -> impl Iterator<Item = i32> {
    0..5
}

fn main() {
    for number in numbers() {
        println!("{number}");
    }
}
```

The concrete return type is fixed for the function, even though callers see the trait-based interface.

This differs from `Box<dyn Iterator<Item = i32>>`, which uses dynamic dispatch and an owned trait object.

## 23.6 Pinning and self-referential data

Advanced asynchronous code sometimes uses `Pin<T>`.

Pinning provides guarantees that help types rely on their memory location remaining stable under specified conditions.

It is particularly relevant to certain self-referential structures and asynchronous state machines.

You usually do not need to use `Pin` directly when beginning Rust. Learn it when working with low-level asynchronous libraries or APIs that require pinned futures.

## 23.7 The type-state pattern

Rust can use different types to represent different stages of an object's lifecycle.

For example:

```
struct Draft;
struct Published;

struct Document<State> {
    content: String,
    state: std::marker::PhantomData<State>,
}

impl Document<Draft> {
    fn new(content: String) -> Self {
        Self {
            content,
            state: std::marker::PhantomData,
        }
    }

    fn publish(self) -> Document<Published> {
        Document {
            content: self.content,
            state: std::marker::PhantomData,
        }
    }
}

impl Document<Published> {
    fn display(&self) {
        println!("{}", self.content);
    }
}

fn main() {
    let draft = Document::<Draft>::new(
        String::from("Hello Rust")
    );

    let published = draft.publish();

    published.display();
}
```

The `Draft` and `Published` states are represented as types.

The `display` method is available only on `Document<Published>`.

This lets the compiler enforce certain application rules that might otherwise require runtime checks.

Type-state designs can be particularly useful for protocol implementations, resource initialization, and APIs where operations must occur in a specific order.

---

# 24\. Performance and zero-cost abstractions

Rust is designed to make high-level abstractions compatible with efficient native code.

However, understanding its performance model is essential if you are coming from C++.

## 24.1 Generics and monomorphization

Consider:

```
fn identity<T>(value: T) -> T {
    value
}
```

When called with different concrete types, Rust can generate specialized implementations.

This resembles C++ template instantiation.

The benefits include static dispatch and opportunities for inlining.

The trade-off is that extensive generic specialization can increase binary size.

## 24.2 Stack versus heap

Rust values are not all allocated on the heap.

For example:

```
let number = 42;
let point = (10, 20);
```

These values can be stored directly in their enclosing storage context.

By contrast:

```
let numbers = Box::new([1, 2, 3]);
```

allocates the array through a `Box`.

Similarly:

```
let values = vec![1, 2, 3];
```

stores the vector's elements in a heap allocation, while the vector value itself contains metadata about that allocation.

The precise placement of values is an implementation and optimization detail, but understanding ownership and allocation behavior is important when tuning performance.

## 24.3 Avoid unnecessary allocation

Consider:

```
fn greet(name: &str) -> String {
    format!("Hello, {name}!")
}
```

This function allocates a new `String` because it returns an owned result.

That is appropriate if the caller needs to retain the generated message.

But if the function only needs to print the greeting, it can avoid constructing the result string:

```
fn greet(name: &str) {
    println!("Hello, {name}!");
}
```

The second function performs output directly.

Do not eliminate allocations blindly, however. An owned return value may make the API much more convenient and correct.

## 24.4 Release builds

Always benchmark optimized builds when evaluating application performance:

```
cargo build --release
```

Debug builds prioritize development diagnostics and may have substantially different performance characteristics.

## 24.5 Benchmark instead of guessing

Useful techniques include:

- Measuring representative workloads.
- Profiling CPU usage.
- Tracking allocation counts.
- Measuring memory consumption.
- Comparing algorithms and data structures.
- Inspecting compiler output when appropriate.

The fastest implementation is often determined more by algorithm choice, memory locality, and workload than by small syntax differences.

---

# 25\. A C++-to-Rust reference guide

This section summarizes common translations you will encounter when moving between the languages.

| C++ | Rust | Important difference |
| --- | --- | --- |
| `int x = 10;` | `let x: i32 = 10;` | Immutable by default |
| `int x = 10;` followed by assignment | `let mut x = 10;` | Mutation must be permitted |
| `const int x = 10;` | `let x = 10;` | `const` is also available for compile-time constants |
| `std::string` | `String` | Owned UTF-8 string |
| `std::string_view` | `&str` | Borrowed UTF-8 string slice |
| `std::vector<T>` | `Vec<T>` | Growable owned collection |
| `std::array<T, N>` | `[T; N]` | Fixed-size array |
| `std::span<const T>` | `&[T]` | Borrowed sequence |
| `std::unique_ptr<T>` | `Box<T>` | Owned heap allocation |
| `std::shared_ptr<T>` | `Arc<T>` | Atomic shared ownership |
| `std::weak_ptr<T>` | `Weak<T>` | Non-owning reference to shared ownership |
| `std::optional<T>` | `Option<T>` | Explicit presence or absence |
| `std::expected<T, E>` | `Result<T, E>` | Explicit success or error |
| Abstract base class | Trait | Behavior without class inheritance |
| Virtual function | Trait object dispatch | Dynamic dispatch when using `dyn Trait` |
| Function template | Generic function | Trait bounds express requirements |
| `std::variant` | Enum | Tagged alternatives with pattern matching |
| `std::map<K, V>` | `BTreeMap<K, V>` | Ordered map |
| `std::unordered_map<K, V>` | `HashMap<K, V>` | Hash map |
| `std::mutex` | `Mutex<T>` | Ownership integrated with synchronization |
| `std::thread` | `std::thread::spawn` | Thread closure must satisfy ownership constraints |
| Destructor | `Drop` | Deterministic cleanup |
| `const T&` | `&T` | Immutable borrow |
| `T&` | `&mut T` | Exclusive mutable borrow |
| `std::move(x)` | Moving `x` | Rust moves are part of the language's ownership rules |
| `try`/`catch` | `Result` and `?` | Explicit error propagation is common |
| `nullptr` or optional pointer | `Option<T>` or `Option<&T>` | Choose owned or borrowed optional data |
| `constexpr` function | `const fn` | Compile-time evaluation has different rules |
| C++ header | Rust module and visibility | No header-file requirement |
| CMake and package manager | Cargo | Integrated build and dependency workflow |
| C++ unit tests | Rust `#[test]` | Built-in test support |

These translations are starting points rather than exact equivalences. For example, `Arc<T>` and `std::shared_ptr<T>` have similar ownership goals, but their thread-safety rules, mutation models, and APIs differ.

---

# 26\. Practice exercises with solutions

The best way to learn Rust is to write small programs and deliberately explore how the compiler responds.

Here are five exercises, progressing from basic syntax to ownership and error handling.

## Exercise 1: Reverse a string

Write a function that reverses a string.

**Solution:**

```
fn reverse_string(input: &str) -> String {
    input.chars().rev().collect()
}

fn main() {
    let text = "Rust";
    let reversed = reverse_string(text);

    println!("{reversed}");
}
```

Output:

```
tsuR
```

The function accepts a borrowed string slice and returns a newly owned string.

It reverses Unicode scalar values, not grapheme clusters. For languages with combining characters or complex emoji, reversing user-perceived characters requires more sophisticated Unicode handling.

## Exercise 2: Find the largest number

Write a generic function that returns the largest element in a slice.

**Solution:**

```
fn largest<T: Ord + Copy>(values: &[T]) -> Option<T> {
    values.iter().copied().max()
}

fn main() {
    let numbers = [10, 40, 20, 90, 30];

    match largest(&numbers) {
        Some(value) => println!("Largest: {value}"),
        None => println!("The collection is empty"),
    }
}
```

The function returns `None` when the slice is empty.

The `Ord` trait provides total ordering, and `Copy` allows the selected element to be returned by value.

## Exercise 3: Count word frequencies

Write a program that counts how often each word appears in a sentence.

**Solution:**

```
use std::collections::HashMap;

fn word_frequencies(text: &str) -> HashMap<String, usize> {
    let mut frequencies = HashMap::new();

    for word in text.split_whitespace() {
        *frequencies
            .entry(word.to_lowercase())
            .or_insert(0) += 1;
    }

    frequencies
}

fn main() {
    let text = "Rust is fast and Rust is safe";

    let frequencies = word_frequencies(text);

    println!("{frequencies:?}");
}
```

This example demonstrates:

- Borrowed string parameters.
- Iteration.
- Owned strings as map keys.
- Hash maps.
- The `entry` API.
- Mutable references.

The frequency map's printed order is unspecified because `HashMap` is not an ordered map.

## Exercise 4: Parse an integer safely

Write a function that parses a string into an integer and returns a meaningful error.

**Solution:**

```
use std::num::ParseIntError;

fn parse_number(input: &str) -> Result<i32, ParseIntError> {
    input.parse::<i32>()
}

fn main() {
    match parse_number("123") {
        Ok(number) => println!("Number: {number}"),
        Err(error) => println!("Invalid input: {error}"),
    }

    match parse_number("abc") {
        Ok(number) => println!("Number: {number}"),
        Err(error) => println!("Invalid input: {error}"),
    }
}
```

The function does not panic on invalid input. It returns a `Result` that the caller can inspect.

## Exercise 5: Implement a generic stack

Create a stack that supports pushing, popping, and checking whether it is empty.

**Solution:**

```
struct Stack<T> {
    elements: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Self {
            elements: Vec::new(),
        }
    }

    fn push(&mut self, value: T) {
        self.elements.push(value);
    }

    fn pop(&mut self) -> Option<T> {
        self.elements.pop()
    }

    fn is_empty(&self) -> bool {
        self.elements.is_empty()
    }

    fn len(&self) -> usize {
        self.elements.len()
    }
}

fn main() {
    let mut stack = Stack::new();

    stack.push(10);
    stack.push(20);
    stack.push(30);

    println!("Length: {}", stack.len());

    while let Some(value) = stack.pop() {
        println!("{value}");
    }

    println!("Empty: {}", stack.is_empty());
}
```

This stack works with any element type, provided the individual operations satisfy that type's requirements.

Notice that the `pop` method returns `Option<T>` instead of requiring the caller to check the stack's length first.

That is an example of an API that makes invalid operations harder to express.

---

# 27\. Recommended learning resources

Use official documentation as your primary reference.

### 1\. The Rust Programming Language

https://doc.rust-lang.org/book/

Often called _The Rust Book_, this is the best starting point for learning the language systematically.

Pay particular attention to:

- Ownership
- References and borrowing
- Structs and enums
- Error handling
- Generic types, traits, and lifetimes
- Smart pointers
- Concurrency

### 2\. Rust By Example

https://doc.rust-lang.org/rust-by-example/

A practical, example-driven introduction. It is useful when you already understand programming concepts and want to see how Rust expresses them.

### 3\. The Rust Standard Library

https://doc.rust-lang.org/std/

Use this to explore standard types and APIs, including `String`, `Vec`, `Option`, `Result`, `HashMap`, `Arc`, and `Mutex`.

### 4\. Rustlings

https://github.com/rust-lang/rustlings

Rustlings provides small exercises designed to teach Rust syntax, ownership, types, and idiomatic programming.

It is particularly useful alongside The Rust Book.

### 5\. The Rust Reference

https://doc.rust-lang.org/reference/

The language reference is more detailed and formal than the introductory book.

It is especially useful when investigating language rules, lifetimes, patterns, macros, and unsafe code.

### 6\. The Cargo Book

https://doc.rust-lang.org/cargo/

This explains project management, dependencies, workspaces, build configuration, testing, and publishing.

### 7\. Rust Performance Book

https://nnethercote.github.io/perf-book/

A useful resource for developers who need to optimize real Rust applications.

---

# 28\. A four-week learning plan for C++ developers

You do not need to relearn programming from scratch. Focus on the concepts where Rust differs most significantly from C++.

## Week 1: Syntax and ownership

Study:

- Variables and mutability.
- Primitive types and type inference.
- Functions and expressions.
- Structs and enums.
- Ownership and moves.
- Immutable and mutable borrowing.

Practice:

- Implement a calculator.
- Write a string-processing utility.
- Implement a generic stack.
- Rewrite small C++ functions in Rust.

**Goal:** Understand why Rust moves values and how borrowing avoids unnecessary ownership transfers.

## Week 2: Idiomatic Rust

Study:

- `Option` and `Result`.
- Error propagation with `?`.
- Pattern matching.
- Traits and generics.
- Iterators and closures.
- Modules and Cargo.

Practice:

- Build a word-frequency analyzer.
- Create a file-processing utility.
- Implement a small library with unit tests.
- Replace manual loops with iterators where appropriate.

**Goal:** Write code that uses Rust's abstractions naturally rather than mechanically translating C++ syntax.

## Week 3: Memory management and concurrency

Study:

- `Box<T>`, `Rc<T>`, and `Arc<T>`.
- `RefCell<T>` and `Mutex<T>`.
- Lifetimes.
- Threads and channels.
- `Send` and `Sync`.
- File I/O and resource management.

Practice:

- Build a multithreaded file analyzer.
- Implement a producer-consumer pipeline.
- Experiment with shared ownership and synchronization.

**Goal:** Understand how ownership and borrowing influence program architecture.

## Week 4: Real projects and advanced topics

Study:

- Async programming.
- Testing and benchmarking.
- Unsafe Rust.
- C and C++ interoperability.
- Performance profiling.
- Common ecosystem libraries.

Practice:

- Extend the task manager.
- Build a command-line application.
- Add structured serialization.
- Write integration tests.
- Profile an optimized release build.

**Goal:** Develop a small, maintainable application using idiomatic Rust.

---

# 29\. Final principles to remember

If you are an experienced C++ programmer, these ten principles will help you become productive in Rust.

1. **Ownership is fundamental.** Every value has an ownership model, and moves transfer ownership rather than implicitly duplicating non-`Copy` values.

2. **Borrowing is not ownership.** Use `&T` to read a value and `&mut T` when exclusive mutable access is needed.

3. **Immutability is the default.** Use `mut` when mutation is necessary.

4. **Prefer explicit error handling.** Use `Option<T>` for potentially absent values and `Result<T, E>` for operations that can fail.

5. **Use enums to model alternatives.** Rust enums and exhaustive pattern matching are excellent tools for making invalid states harder to represent.

6. **Use traits instead of class inheritance.** Traits define behavior, generics enable static polymorphism, and trait objects enable dynamic dispatch.

7. **Let the compiler help you.** Borrow-checker errors often reveal a problem with ownership or data flow. Fix the underlying design rather than immediately reaching for interior mutability or cloning.

8. **Prefer standard abstractions.** `Vec`, slices, iterators, smart pointers, and standard error types will solve many problems without requiring custom low-level code.

9. **Treat unsafe code as a responsibility.** It is a necessary tool for some systems programming tasks, but it requires careful reasoning about memory validity, aliasing, and thread safety.

10. **Measure performance.** Rust's abstractions can be highly efficient, but real performance depends on algorithms, allocations, data layout, and compiler optimizations.

## The most important mental shift

In C++, you can write code that compiles even when a pointer or reference will later become invalid. You then rely on design, discipline, static analysis, testing, and runtime tools to prevent or detect the problem.

In Rust, the ownership system and borrow checker move many of those checks into compilation.

Instead of asking only:

_How do I implement this algorithm?_

you also learn to ask:

- Who owns this data?
- Does this function need ownership or only a reference?
- Who is allowed to mutate this value?
- How long must this reference remain valid?
- Can the type system express the invariants I need?

These questions initially require extra thought. Over time, they become part of your design process.

**My recommendation:** Start with ownership, borrowing, and `Result`; then build the task manager in this tutorial without copying the solution. Once you can explain why each value is moved, borrowed, or returned, you will have established the foundation needed to tackle larger Rust projects.
