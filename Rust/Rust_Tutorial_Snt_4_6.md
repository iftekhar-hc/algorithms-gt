<a id="rust-for-c-programmers"></a>

# Rust for C++ Programmers

Contents

- [1. Philosophy & Design Goals](#_philosophy_design_goals)
- [2. Syntax Crash Course](#_syntax_crash_course)
  - [2.1. Variables & Mutability](#_variables_mutability)
  - [2.2. Functions](#_functions)
  - [2.3. Control Flow](#_control_flow)
  - [2.4. Closures](#_closures)
- [3. Type System](#_type_system)
  - [3.1. Primitive Types](#_primitive_types)
  - [3.2. Strings](#_strings)
  - [3.3. Collections](#_collections)
- [4. Ownership](#_ownership)
  - [4.1. The Three Rules](#_the_three_rules)
  - [4.2. Move Semantics — Default, Not
    Optional](#_move_semantics_default_not_optional)
  - [4.3. Copy Types](#_copy_types)
  - [4.4. RAII — Exactly What You Know](#_raii_exactly_what_you_know)
- [5. Borrowing & References](#_borrowing_references)
  - [5.1. Shared vs Mutable References](#_shared_vs_mutable_references)
  - [5.2. Slices — Rust’s `std::span`](#_slices_rusts_stdspan)
- [6. Lifetimes](#_lifetimes)
  - [6.1. Lifetime Elision vs Explicit
    Annotations](#_lifetime_elision_vs_explicit_annotations)
  - [6.2. Static Lifetime](#_static_lifetime)
- [7. Smart Pointers](#_smart_pointers)
  - [7.1. Interior Mutability — Rust’s Answer to
    `mutable`](#_interior_mutability_rusts_answer_to_mutable)
- [8. Structs & Enums](#_structs_enums)
  - [8.1. Structs (No Classes)](#_structs_no_classes)
  - [8.2. Enums — Algebraic Data Types](#_enums_algebraic_data_types)
  - [8.3. Option and Result — Enums in
    Disguise](#_option_and_result_enums_in_disguise)
- [9. Traits vs Concepts](#_traits_vs_concepts)
  - [9.1. Static vs Dynamic Dispatch](#_static_vs_dynamic_dispatch)
  - [9.2. Operator Overloading via
    Traits](#_operator_overloading_via_traits)
- [10. Generics & Templates](#_generics_templates)
  - [10.1. Where Clauses for Complex
    Bounds](#_where_clauses_for_complex_bounds)
- [11. Error Handling](#_error_handling)
  - [11.1. Custom Error Types](#_custom_error_types)
- [12. Threads & Sync](#_threads_sync)
  - [12.1. Channels — CSP Style](#_channels_csp_style)
- [13. Async / Await](#_async_await)
- [14. Cargo vs CMake](#_cargo_vs_cmake)
  - [14.1. Cargo.toml — The Manifest](#_cargo_toml_the_manifest)
  - [14.2. Built-in Test Framework](#_built_in_test_framework)
- [15. Unsafe Rust](#_unsafe_rust)
  - [15.1. What unsafe Allows](#_what_unsafe_allows)
- [16. FFI & Interop](#_ffi_interop)
  - [16.1. Calling C from Rust](#_calling_c_from_rust)
  - [16.2. Exposing Rust to C/C++](#_exposing_rust_to_cc)
- [17. C++ Patterns in Rust](#_c_patterns_in_rust)
  - [17.1. PIMPL → Box](#_pimpl_box)
  - [17.2. Builder Pattern](#_builder_pattern)
  - [17.3. Type State Pattern — Compile-time State
    Machines](#_type_state_pattern_compile_time_state_machines)
  - [17.4. Common Pitfalls from C++](#_common_pitfalls_from_c)

A comprehensive migration guide for systems programmers.\
You already think in memory layouts, object lifetimes, and performance.
This guide skips the basics and maps what you know to Rust’s model —
including where they diverge fundamentally.

**Covers:** Rust 2024 Edition · No GC · No Runtime · Compile-time Safety

------------------------------------------------------------------------

<a id="_philosophy_design_goals"></a>

## 1. Philosophy & Design Goals

Both C++ and Rust occupy the same niche: systems languages with
zero-cost abstractions and no garbage collector. But they make different
bets about where to put complexity.

| Concern | C++ Approach | Rust Approach |
|----|----|----|
| Memory safety | Programmer discipline + tools (ASan, Valgrind) | Compile-time borrow checker |
| Undefined behaviour | Vast UB surface; optimiser exploits it | Eliminated in safe code; opt-in via `unsafe` |
| Null pointers | Raw pointers, optional references | `Option<T>` — null is not a value |
| Error handling | Exceptions or error codes (mixed) | `Result<T, E>` — errors are values |
| Concurrency | Mutexes, atomic ops, programmer-verified | `Send`/`Sync` traits enforced at compile time |
| Abstraction cost | Zero-cost (mostly) | Zero-cost (guaranteed by design) |
| Build system | CMake / Meson / Bazel / make | Cargo (first-party, universal) |
| Package management | Conan, vcpkg (fragmented) | crates.io (first-party) |

|  |  |
|----|----|
| Note | Rust moves the complexity from runtime debugging into the type system. Code that compiles is *far* more likely to be correct. The borrow checker is not a limitation — it’s the compiler doing the work your code review was doing. |

------------------------------------------------------------------------

<a id="_syntax_crash_course"></a>

## 2. Syntax Crash Course

<a id="_variables_mutability"></a>

### 2.1. Variables & Mutability

In C++, variables are mutable by default; `const` opts out. Rust flips
this: **immutable by default**, `mut` opts in.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>int x = 42;          // mutable
const int y = 10;    // immutable
x = 99;              // ok
&#10;auto z = 3.14;       // type inferred</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let x = 42;           // immutable
let mut y = 10;       // mutable
y = 99;               // ok
&#10;let z: f64 = 3.14;   // explicit type
let w = 3.14_f64;    // suffix inferred</code></pre></td>
</tr>
</tbody>
</table>

<a id="_functions"></a>

### 2.2. Functions

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>int add(int a, int b) {
    return a + b;
}
&#10;auto mul(int a, int b) -&gt; int {
    return a * b;
}</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>fn add(a: i32, b: i32) -&gt; i32 {
    a + b  // no semicolon = return value
}
&#10;fn mul(a: i32, b: i32) -&gt; i32 {
    return a * b;
}</code></pre></td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Tip | Rust is expression-based. A block `{ …​ }` evaluates to its last expression if it lacks a trailing semicolon. This applies to `if`, `match`, loops, and function bodies. |

<a id="_control_flow"></a>

### 2.3. Control Flow

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>switch (status) {
  case 0: handle_ok();  break;
  case 1: handle_err(); break;
  default: break;
}
&#10;for (auto&amp; item : vec) {
    process(item);
}</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>match status {
    0 =&gt; handle_ok(),
    1 =&gt; handle_err(),
    _ =&gt; {}  // wildcard required
}
&#10;for item in &amp;vec {
    process(item);
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_closures"></a>

### 2.4. Closures

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>auto add = [=](int x) {
    return x + base;
};
&#10;std::function&lt;int(int)&gt; f = add;</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let add =</code></pre></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p>x</p></td>
<td class="tableblock halign-left valign-top"><p>x + base;</p>
<p>let f: Box&lt;dyn Fn(i32) → i32&gt; = Box::new(add);</p>
<p>fn apply(f: impl Fn(i32) → i32) { }</p></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<a id="_type_system"></a>

## 3. Type System

<a id="_primitive_types"></a>

### 3.1. Primitive Types

| C++ Type | Rust Equivalent | Notes |
|----|----|----|
| `int` | `i32` | Rust requires explicit width always |
| `unsigned int` | `u32` |  |
| `int64_t` | `i64` |  |
| `size_t` | `usize` | Pointer-sized, used for indexing |
| `float` | `f32` |  |
| `double` | `f64` | Rust default float literal type |
| `bool` | `bool` | Same |
| `char` | `char` | Rust `char` is always Unicode scalar (4 bytes) |
| `void` | `()` | Unit is a real zero-sized type, not absence |
| `T*` | `*const T` / `*mut T` | Raw pointers exist but require `unsafe` |
| `T&` | `&T` / `&mut T` | Always valid (lifetime-checked) |

<a id="_strings"></a>

### 3.2. Strings

C++ has `std::string` (heap, owned) and `std::string_view` (borrowed).
Rust mirrors this cleanly:

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::string owned = &quot;hello&quot;;
std::string_view view = owned;
&#10;const char* raw = &quot;literal&quot;;
owned += &quot; world&quot;;</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let owned: String = String::from(&quot;hello&quot;);
let view: &amp;str = &amp;owned;    // borrowed slice
let literal: &amp;str = &quot;world&quot;; // static lifetime
&#10;let mut s = owned;
s.push_str(&quot; world&quot;);</code></pre></td>
</tr>
</tbody>
</table>

<a id="_collections"></a>

### 3.3. Collections

| C++ Container             | Rust Equivalent           |
|---------------------------|---------------------------|
| `std::vector<T>`          | `Vec<T>`                  |
| `std::array<T,N>`         | `[T; N]`                  |
| `std::span<T>`            | `&[T]` / `&mut [T]`       |
| `std::unordered_map<K,V>` | `HashMap<K,V>`            |
| `std::map<K,V>`           | `BTreeMap<K,V>`           |
| `std::optional<T>`        | `Option<T>`               |
| `std::variant<A,B>`       | `enum Foo { A(…​), B(…​) }` |
| `std::tuple<A,B>`         | `(A, B)` tuple            |

------------------------------------------------------------------------

<a id="_ownership"></a>

## 4. Ownership

The single most important concept in Rust — and its biggest departure
from C++.

Every value in Rust has exactly one **owner**. When the owner goes out
of scope, the value is dropped (destructor called, memory freed). No GC,
no manual `delete`.

<a id="_the_three_rules"></a>

### 4.1. The Three Rules

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon">Important</td>
<td class="content"><ol>
<li><p>Every value has exactly one owner.</p></li>
<li><p>When the owner goes out of scope, the value is dropped.</p></li>
<li><p>Ownership can be <strong>moved</strong> or
<strong>cloned</strong>, never silently copied (for heap
types).</p></li>
</ol></td>
</tr>
</tbody>
</table>

<a id="_move_semantics_default_not_optional"></a>

### 4.2. Move Semantics — Default, Not Optional

C++ added move semantics in C++11, but copy is still the default for
types that implement it. In Rust, **move is always the default** for
non-`Copy` types.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::vector&lt;int&gt; v = {1,2,3};
std::vector&lt;int&gt; w = v;  // COPY
&#10;std::vector&lt;int&gt; x = std::move(v);</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let v: Vec&lt;i32&gt; = vec![1,2,3];
let w = v;        // MOVE (ownership transferred)
&#10;let x = w.clone(); // explicit deep copy</code></pre></td>
</tr>
</tbody>
</table>

<a id="_copy_types"></a>

### 4.3. Copy Types

Primitive types (`i32`, `f64`, `bool`, `char`) and types composed of
them implement the `Copy` trait. Copying is implicit and cheap — exactly
like C++ for `int`, `double`, etc.

```
let x: i32 = 5;
let y = x;  // copy, not move — x still valid
println!("{x} {y}");  // both work

// Your struct can opt into Copy:
#[derive(Copy, Clone)]
struct Point { x: f32, y: f32 }
```

<a id="_raii_exactly_what_you_know"></a>

### 4.4. RAII — Exactly What You Know

Rust’s drop semantics are identical to C++ RAII. The `Drop` trait is
`std::~Destructor`.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>struct File {
    FILE* f;
    ~File() { fclose(f); }
};
&#10;{
    File guard{fopen(&quot;x&quot;,&quot;r&quot;)};
} // destructor called here</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>struct File { ptr: *mut libc::FILE }
&#10;impl Drop for File {
    fn drop(&amp;mut self) {
        unsafe { fclose(self.ptr); }
    }
}
{
    let _guard = File { ptr: ... };
} // drop() called here</code></pre></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<a id="_borrowing_references"></a>

## 5. Borrowing & References

How Rust eliminates use-after-free, dangling pointers, and data races at
compile time.

Rust’s references are like C++ references — always valid, never null —
but with strict aliasing rules enforced by the compiler.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon">Warning</td>
<td class="content"><p><strong>The Aliasing XOR Mutability
Rule</strong></p>
<p>At any point in time, you may have <strong>either</strong>:</p>
<ul>
<li><p>Any number of shared references <code>&amp;T</code> (read-only),
<strong>or</strong></p></li>
<li><p>Exactly one mutable reference <code>&amp;mut T</code>
(read-write)</p></li>
</ul>
<p>But never both simultaneously. This is enforced at compile
time.</p></td>
</tr>
</tbody>
</table>

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::vector&lt;int&gt; v = {1,2,3};
const int&amp; r1 = v[0];
const int&amp; r2 = v[0];
v.push_back(4);  // UB! r1,r2 dangling
std::cout &lt;&lt; r1; // undefined behaviour</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let mut v = vec![1,2,3];
let r1 = &amp;v[0];
let r2 = &amp;v[0];
v.push(4);  // ❌ compile error!
            // cannot borrow `v` mutably
            // while immutably borrowed
println!(&quot;{r1}&quot;);</code></pre></td>
</tr>
</tbody>
</table>

<a id="_shared_vs_mutable_references"></a>

### 5.1. Shared vs Mutable References

```
fn print_len(s: &String) {           // shared borrow
    println!("{}", s.len());
}

fn append(s: &mut String) {          // mutable borrow
    s.push_str(" world");
}

let mut hello = String::from("hello");
print_len(&hello);                   // lends immutably
append(&mut hello);                  // lends mutably
print_len(&hello);                   // ok again
```

<a id="_slices_rusts_stdspan"></a>

### 5.2. Slices — Rust’s `std::span`

A slice `&[T]` is a fat pointer (pointer + length) — the equivalent of
`std::span<T>` but lifetime-checked.

```
fn sum(nums: &[i32]) -> i32 {   // works on Vec, array, or any contiguous memory
    nums.iter().sum()
}

let v = vec![1, 2, 3, 4];
sum(&v);          // whole Vec
sum(&v[1..3]);    // sub-slice [2, 3]
sum(&[10, 20]);   // array literal coerced
```

------------------------------------------------------------------------

<a id="_lifetimes"></a>

## 6. Lifetimes

Making the implicit explicit — and verifiable.

Lifetimes are Rust’s way of expressing "this reference must not outlive
the data it points to." In C++, this is checked at runtime (or not at
all). In Rust, it’s a compile-time annotation that the borrow checker
verifies.

|  |  |
|----|----|
| Note | The compiler infers lifetimes in simple cases (lifetime elision). You only write explicit lifetime annotations `'a` when the compiler can’t determine which input borrow ties to the output borrow. |

<a id="_lifetime_elision_vs_explicit_annotations"></a>

### 6.1. Lifetime Elision vs Explicit Annotations

```
// Compiler infers: output lives as long as input
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &b) in bytes.iter().enumerate() {
        if b == b' ' { return &s[..i]; }
    }
    s
}

// Must annotate: compiler can't decide which input owns output
fn longer<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
// 'a means: output lives as long as the shorter of x or y

// Struct holding a reference needs a lifetime
struct Excerpt<'a> {
    text: &'a str,
}
```

<a id="_static_lifetime"></a>

### 6.2. Static Lifetime

```
// String literals live for the entire program
let s: &'static str = "I live forever";

// Be wary of using 'static to "fix" lifetime errors —
// it usually signals a design issue.
```

------------------------------------------------------------------------

<a id="_smart_pointers"></a>

## 7. Smart Pointers

| C++ Type | Rust Type | Notes |
|----|----|----|
| `std::unique_ptr<T>` | `Box<T>` | Single owner, heap allocated |
| `std::shared_ptr<T>` | `Rc<T>` | Ref-counted, single-threaded |
| `std::shared_ptr<T>` | `Arc<T>` | Atomically ref-counted, thread-safe |
| `std::weak_ptr<T>` | `Weak<T>` | Non-owning ref to `Rc`/`Arc` |
| `std::mutex<T>` (conceptual) | `Mutex<T>` | Data *inside* the mutex, not separate |
| `mutable T` (interior mut.) | `Cell<T>` / `RefCell<T>` | Allows mutation through shared ref |

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>auto p = std::make_unique&lt;Widget&gt;(42);
use(*p);
&#10;auto s = std::make_shared&lt;Widget&gt;(1);
auto t = s;   // refcount++</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>let p = Box::new(Widget::new(42));
use_it(&amp;p);
&#10;let s = Rc::new(Widget::new(1));
let t = Rc::clone(&amp;s);  // refcount++</code></pre></td>
</tr>
</tbody>
</table>

<a id="_interior_mutability_rusts_answer_to_mutable"></a>

### 7.1. Interior Mutability — Rust’s Answer to `mutable`

Sometimes you need mutability behind a shared reference (e.g., caches,
event handlers). C++ uses `mutable` members; Rust uses `RefCell<T>`
(runtime borrow checking) or `Cell<T>` (copy types).

```
use std::cell::RefCell;

let data = RefCell::new(vec![1, 2, 3]);

// Borrow rules checked at runtime, not compile time
data.borrow().iter().for_each(|x| println!("{x}"));
data.borrow_mut().push(4);   // panics if already borrowed
```

------------------------------------------------------------------------

<a id="_structs_enums"></a>

## 8. Structs & Enums

<a id="_structs_no_classes"></a>

### 8.1. Structs (No Classes)

Rust has no classes. Structs hold data; `impl` blocks provide methods.
Inheritance doesn’t exist — composition and traits replace it.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>class Rectangle {
public:
    double width, height;
    Rectangle(double w, double h)
        : width(w), height(h) {}
    double area() const {
        return width * height;
    }
};</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>struct Rectangle {
    width: f64,
    height: f64,
}
&#10;impl Rectangle {
    fn new(w: f64, h: f64) -&gt; Self {
        Self { width: w, height: h }
    }
    fn area(&amp;self) -&gt; f64 {
        self.width * self.height
    }
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_enums_algebraic_data_types"></a>

### 8.2. Enums — Algebraic Data Types

Rust’s `enum` is vastly more powerful than C/C++ enums. Each variant can
carry data of different types — equivalent to a tagged union, but safe.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>using Shape = std::variant&lt;
    Circle, Rectangle, Triangle
&gt;;
&#10;auto area = std::visit(overloaded{
    [](Circle c)    { return M_PI*c.r*c.r; },
    [](Rectangle r) { return r.w * r.h; },
    [](Triangle t)  { return 0.5*t.b*t.h; },
}, shape);</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>enum Shape {
    Circle { radius: f64 },
    Rect   { w: f64, h: f64 },
    Tri    { base: f64, height: f64 },
}
&#10;let area = match shape {
    Shape::Circle { radius: r } =&gt;
        std::f64::consts::PI * r * r,
    Shape::Rect { w, h } =&gt; w * h,
    Shape::Tri { base: b, height: h } =&gt;
        0.5 * b * h,
};</code></pre></td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Tip | The compiler will refuse to compile a `match` that doesn’t cover all variants. Adding a new enum variant will produce compile errors everywhere it’s matched — exactly what you want. |

<a id="_option_and_result_enums_in_disguise"></a>

### 8.3. Option and Result — Enums in Disguise

```
// Option replaces nullable pointers
let maybe: Option<i32> = Some(42);
let none:  Option<i32> = None;

// pattern match
match maybe {
    Some(v) => println!("got {v}"),
    None    => println!("nothing"),
}

// or use combinators
let doubled  = maybe.map(|v| v * 2);
let fallback = none.unwrap_or(0);

// Result: Ok(value) or Err(error)
fn parse(s: &str) -> Result<i32, String> {
    s.parse().map_err(|e| e.to_string())
}

let n = parse("42")?;  // ? propagates error to caller
```

------------------------------------------------------------------------

<a id="_traits_vs_concepts"></a>

## 9. Traits vs Concepts

Traits are Rust’s answer to C++ abstract base classes *and* C++20
Concepts. They define shared behaviour without inheritance.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>class Drawable {
public:
    virtual void draw() const = 0;
    virtual ~Drawable() = default;
};
&#10;template&lt;typename T&gt;
concept Drawable = requires(T t) {
    { t.draw() } -&gt; std::same_as&lt;void&gt;;
};</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>trait Drawable {
    fn draw(&amp;self);
    // default implementations allowed:
    fn draw_twice(&amp;self) {
        self.draw(); self.draw();
    }
}
&#10;impl Drawable for Circle {
    fn draw(&amp;self) {
        println!(&quot;○ r={}&quot;, self.radius);
    }
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_static_vs_dynamic_dispatch"></a>

### 9.1. Static vs Dynamic Dispatch

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>template&lt;Drawable T&gt;
void render(T&amp; d) { d.draw(); }
&#10;void render(Drawable* d) { d-&gt;draw(); }
std::vector&lt;Drawable*&gt; scene;</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>fn render(d: impl Drawable) { d.draw(); }
&#10;fn render(d: &amp;dyn Drawable) { d.draw(); }
let scene: Vec&lt;Box&lt;dyn Drawable&gt;&gt; = vec![];</code></pre></td>
</tr>
</tbody>
</table>

<a id="_operator_overloading_via_traits"></a>

### 9.2. Operator Overloading via Traits

```
use std::ops::Add;

#[derive(Debug, Clone, Copy)]
struct Vec2 { x: f32, y: f32 }

impl Add for Vec2 {
    type Output = Vec2;
    fn add(self, other: Vec2) -> Vec2 {
        Vec2 { x: self.x + other.x, y: self.y + other.y }
    }
}

let a = Vec2 { x: 1.0, y: 2.0 };
let b = Vec2 { x: 3.0, y: 4.0 };
let c = a + b;  // Vec2 { x: 4.0, y: 6.0 }
```

------------------------------------------------------------------------

<a id="_generics_templates"></a>

## 10. Generics & Templates

Rust generics compile to the same efficient code as C++ templates
(monomorphization). But they’re checked at the point of definition, not
instantiation.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>template&lt;typename T&gt;
T largest(const std::vector&lt;T&gt;&amp; v) {
    T max = v[0];
    for (const T&amp; x : v)
        if (x &gt; max) max = x;
    return max;
}</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>fn largest&lt;T: PartialOrd&gt;(v: &amp;[T]) -&gt; &amp;T {
    let mut max = &amp;v[0];
    for x in v {
        if x &gt; max { max = x; }
    }
    max
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_where_clauses_for_complex_bounds"></a>

### 10.1. Where Clauses for Complex Bounds

```
// Long form with where (equivalent to inline bounds)
fn serialize_and_print<T>(item: &T)
where
    T: serde::Serialize + std::fmt::Debug + Send,
{
    println!("{item:?}");
    let json = serde_json::to_string(item).unwrap();
    println!("{json}");
}
```

------------------------------------------------------------------------

<a id="_error_handling"></a>

## 11. Error Handling

Rust has no exceptions. Errors are either recoverable (`Result<T, E>`)
or unrecoverable (`panic!`). This makes error paths explicit in every
function signature.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::string read_file(const std::string&amp; p) {
    std::ifstream f(p);
    if (!f) throw std::runtime_error(&quot;open failed&quot;);
    return {std::istreambuf_iterator&lt;char&gt;(f), {}};
}</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>fn read_file(path: &amp;str) -&gt; Result&lt;String, std::io::Error&gt; {
    std::fs::read_to_string(path)
}
&#10;fn process() -&gt; Result&lt;(), Box&lt;dyn std::error::Error&gt;&gt; {
    let content = read_file(&quot;data.txt&quot;)?;
    let n: i32 = content.trim().parse()?;
    println!(&quot;parsed: {n}&quot;);
    Ok(())
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_custom_error_types"></a>

### 11.1. Custom Error Types

```
use thiserror::Error;  // thiserror crate

#[derive(Debug, Error)]
enum AppError {
    #[error("I/O failed: {0}")]
    Io(#[from] std::io::Error),

    #[error("parse error: {msg}")]
    Parse { msg: String },
}

fn load() -> Result<i32, AppError> {
    let s = std::fs::read_to_string("n.txt")?; // auto-converts io::Error
    s.trim().parse().map_err(|_| AppError::Parse {
        msg: format!("not a number: {s}")
    })
}
```

------------------------------------------------------------------------

<a id="_threads_sync"></a>

## 12. Threads & Sync

Fearless concurrency — data races are compile-time errors.

The `Send` and `Sync` traits form Rust’s concurrency safety model.
They’re automatically derived and restrict what can cross thread
boundaries.

| Marker trait | Meaning | Example types |
|----|----|----|
| `Send` | Safe to send ownership to another thread | Most types; not `Rc<T>`, raw pointers |
| `Sync` | Safe to share reference across threads | Most types; not `Cell<T>`, `RefCell<T>` |

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::mutex mtx;
int shared = 0;
&#10;auto t = std::thread([&amp;] {
    std::lock_guard lock(mtx);
    shared += 1;
});
t.join();</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>use std::sync::{Arc, Mutex};
&#10;let shared = Arc::new(Mutex::new(0));
let s = Arc::clone(&amp;shared);
&#10;let t = std::thread::spawn(move</code></pre></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"></td>
<td class="tableblock halign-left valign-top"><p>{ *s.lock().unwrap() +=
1; }); t.join().unwrap();</p></td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Warning | Rust prevents data races but not deadlocks. Logic errors (lock ordering, etc.) remain your responsibility — just as in C++. |

<a id="_channels_csp_style"></a>

### 12.1. Channels — CSP Style

```
use std::sync::mpsc;

let (tx, rx) = mpsc::channel();

std::thread::spawn(move || {
    tx.send(42).unwrap();
});

let val = rx.recv().unwrap();
println!("received {val}");
```

------------------------------------------------------------------------

<a id="_async_await"></a>

## 13. Async / Await

Stackless coroutines — no runtime included.

Rust’s async is similar to C++20 coroutines — zero-cost, stackless,
compiled to state machines. Unlike C++, `async`/`await` is idiomatic and
widely used via runtimes like Tokio.

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>std::future&lt;std::string&gt;
fetch(std::string url) {
    auto resp = co_await http_get(url);
    co_return resp.body();
}</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>async fn fetch(url: &amp;str) -&gt; String {
    let resp = reqwest::get(url)
        .await
        .unwrap();
    resp.text().await.unwrap()
}
&#10;#[tokio::main]
async fn main() {
    let body = fetch(&quot;https://example.com&quot;).await;
}</code></pre></td>
</tr>
</tbody>
</table>

|  |  |
|----|----|
| Note | `async fn` returns a `Future` — a lazy value that does nothing until driven by an executor. You must choose a runtime: **Tokio** (most popular), **async-std**, or **smol**. This is unlike Go or Node.js where the runtime is baked in. |

------------------------------------------------------------------------

<a id="_cargo_vs_cmake"></a>

## 14. Cargo vs CMake

First-party tooling changes everything.

| Task | C++ | Rust |
|----|----|----|
| Build | `cmake --build .` | `cargo build` |
| Release build | `cmake -DCMAKE_BUILD_TYPE=Release` | `cargo build --release` |
| Run | `./build/app` | `cargo run` |
| Test | GoogleTest / Catch2 (manual setup) | `cargo test` (built in) |
| Benchmark | Google Benchmark (separate) | `cargo bench` |
| Docs | Doxygen (separate) | `cargo doc` (built in) |
| Add dependency | vcpkg/Conan + CMakeLists.txt | `cargo add serde` |
| Lint | clang-tidy (separate) | `cargo clippy` (built in) |
| Format | clang-format (separate) | `cargo fmt` (built in) |

<a id="_cargo_toml_the_manifest"></a>

### 14.1. Cargo.toml — The Manifest

```
[package]
name    = "my-app"
version = "0.1.0"
edition = "2024"

[dependencies]
serde  = { version = "1", features = ["derive"] }
tokio  = { version = "1", features = ["full"] }
anyhow = "1"

[dev-dependencies]
criterion = "0.5"

[profile.release]
opt-level = 3
lto       = true
```

<a id="_built_in_test_framework"></a>

### 14.2. Built-in Test Framework

```
fn add(a: i32, b: i32) -> i32 { a + b }

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    #[should_panic]
    fn test_overflow() {
        add(i32::MAX, 1);  // panics in debug mode
    }
}
```

------------------------------------------------------------------------

<a id="_unsafe_rust"></a>

## 15. Unsafe Rust

The escape hatch — not a license, a contract.

`unsafe` blocks tell the compiler "I take responsibility for these
invariants." The surface area of UB in Rust is much smaller than in C++,
and explicitly delineated.

<a id="_what_unsafe_allows"></a>

### 15.1. What unsafe Allows

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon">Warning</td>
<td class="content"><ol>
<li><p>Dereference raw pointers (<code>*const T</code>,
<code>*mut T</code>)</p></li>
<li><p>Call <code>unsafe</code> functions (including FFI)</p></li>
<li><p>Access or modify mutable static variables</p></li>
<li><p>Implement <code>unsafe</code> traits (<code>Send</code>,
<code>Sync</code>)</p></li>
<li><p>Access fields of <code>union</code> types</p></li>
</ol></td>
</tr>
</tbody>
</table>

```
let mut v = vec![1, 2, 3];
let raw: *mut i32 = v.as_mut_ptr();

unsafe {
    // Programmer guarantees: ptr valid, aligned, in bounds
    *raw.add(1) = 99;
}

assert_eq!(v, [1, 99, 3]);

// Split a slice into two non-overlapping mutable halves
// Safe functions can't express this — unsafe enables it
let (left, right) = v.split_at_mut(2);
```

|  |  |
|----|----|
| Tip | Wrap unsafe code in a safe abstraction. The unsafe block is a hot-spot that reviewers focus on. All of Rust’s standard collections are built this way — safe API, minimal unsafe interior. |

------------------------------------------------------------------------

<a id="_ffi_interop"></a>

## 16. FFI & Interop

<a id="_calling_c_from_rust"></a>

### 16.1. Calling C from Rust

```
extern "C" {
    fn strlen(s: *const std::os::raw::c_char) -> usize;
    fn malloc(size: usize) -> *mut std::os::raw::c_void;
}

let n = unsafe {
    strlen(c"hello".as_ptr())  // c"..." = CStr literal (Rust 1.77+)
};
```

<a id="_exposing_rust_to_cc"></a>

### 16.2. Exposing Rust to C/C++

```
#[no_mangle]
pub extern "C" fn rust_add(a: i32, b: i32) -> i32 {
    a + b
}
// Callable from C++: extern "C" int rust_add(int, int);
```

|  |  |
|----|----|
| Note | For serious C++ interop, use the **cxx** crate (safe, idiomatic C++/Rust bridge) or **bindgen** (auto-generates Rust FFI from C headers). These handle the boilerplate and type mapping. |

------------------------------------------------------------------------

<a id="_c_patterns_in_rust"></a>

## 17. C++ Patterns in Rust

<a id="_pimpl_box"></a>

### 17.1. PIMPL → Box

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">C++</th>
<th class="tableblock halign-left valign-top">Rust</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="cpp"><code>class Widget {
    struct Impl;
    std::unique_ptr&lt;Impl&gt; d;
public:
    Widget();
    void doWork();
};</code></pre></td>
<td class="tableblock halign-left valign-top"><pre class="highlight"
data-lang="rust"><code>pub struct Widget(Box&lt;WidgetImpl&gt;);
struct WidgetImpl { /* private */ }
&#10;impl Widget {
    pub fn new() -&gt; Self { ... }
    pub fn do_work(&amp;self) { ... }
}</code></pre></td>
</tr>
</tbody>
</table>

<a id="_builder_pattern"></a>

### 17.2. Builder Pattern

```
#[derive(Default)]
struct ServerBuilder {
    host:    Option<String>,
    port:    Option<u16>,
    threads: usize,
}

impl ServerBuilder {
    fn host(mut self, h: impl Into<String>) -> Self {
        self.host = Some(h.into()); self
    }
    fn port(mut self, p: u16) -> Self {
        self.port = Some(p); self
    }
    fn build(self) -> Result<Server, String> {
        Ok(Server {
            host: self.host.ok_or("host required")?,
            port: self.port.unwrap_or(8080),
        })
    }
}

let server = ServerBuilder::default()
    .host("localhost")
    .port(3000)
    .build()?;
```

<a id="_type_state_pattern_compile_time_state_machines"></a>

### 17.3. Type State Pattern — Compile-time State Machines

```
struct Connection<S> { state: S }
struct Disconnected;
struct Connected;

impl Connection<Disconnected> {
    fn connect(self) -> Connection<Connected> {
        Connection { state: Connected }
    }
}

impl Connection<Connected> {
    fn send(&self, data: &[u8]) { /* ... */ }
    fn disconnect(self) -> Connection<Disconnected> {
        Connection { state: Disconnected }
    }
}

let conn = Connection { state: Disconnected };
// conn.send(&[]);  // ❌ compile error — not connected yet
let conn = conn.connect();
conn.send(&[1,2,3]);  // ✓
```

<a id="_common_pitfalls_from_c"></a>

### 17.4. Common Pitfalls from C++

| C++ Habit | Rust Reality |
|----|----|
| Return `T*`, caller frees | Return `Box<T>` or `Rc<T>`; ownership is explicit |
| Pass by value, rely on copy | Only `Copy` types copy; others move. Use `.clone()` explicitly |
| `this` is a raw pointer | `self` is a proper reference; `&self` or `&mut self` |
| Mutate while iterating | Borrow checker prevents it — restructure to iterate then modify |
| Global mutable state | Requires `Mutex<T>` or `OnceLock` — intentionally friction |
| Implicit integer conversion | All casts explicit: `x as u32`, `T::try_from(x)?` |
| `std::thread_local` | `thread_local!` macro — same concept |
| Uninitialized variables | Compile error — must initialize before use |

Last updated 2026-10-15 08:05:23 UTC
