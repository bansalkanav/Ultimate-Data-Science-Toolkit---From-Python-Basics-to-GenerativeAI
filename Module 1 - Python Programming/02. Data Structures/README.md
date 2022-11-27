# Data Types and Data Structures in Python

As we know that python is Dynamically typed programming language, than why do we need to learn about data type at all?

Although python automatically understands the data type, but it is important to know about data types so that we can utilize the power of data structures in future.

Basic Data Types available in python are:
<pre>
    <b>Numeric</b> - int, float, complex (Immutable)
    <b>Strings</b> (Immutable)
    <b>List</b> (Mutable, mostly used to store homogeneous data types)
    <b>Tuple</b> (Immutable, faster compared to List)
    <b>Set</b> (Unordered collection of items, mutable, removes duplicates)
    <b>Dictionary</b> (Unordered collection of Key-Value Pairs, Mutable, Keys are Unique - values may not be unique)
</pre>


### Strings

```python
string_var = 'ThatAIGuy'
```
> 1. String is a sequence of characters.
> 2. Use index to access characters in a string
> 3. If we try to access index out of range or use decimal numbers we will get an error
> 4. Python supports both +ve and -ve index
> 5. Strings are immutable. Elemets of strings can't be changed once it has been assigned. We can simply reassign different strings to the same name
> 6. Strings support indexing as well as slicing

### Lists

```python
list_var = ['Checkout', 'ThatAIGuy', '.', 'com']
```
> 1. Sequence Data Structure.
> 2. Used to store collection of items.
> 3. Order is preserved in a list
> 4. Mutable
> 5. Indexing and slicing
> 6. Dynamic i.e. increase or decrease in size

### Tuples

```python
tuple_var = ('Checkout', 'ThatAIGuy', '.', 'com')
```
> 1. Similar to list but immutable.
> 2. Sequence data type.
> 3. Supports indexing and slicing.

### Set

```python
set_var = {1, 11, 0, 1, 2}
```
> 1. Unordered collection of items i.e. they can't be indexed
> 2. No duplicates allowed
> 3. Mutable
> 4. Used to perform mathematical operations like Union, intersection, etc..

### Dictionary

```python
dict_var = {'key_1': 'val_1', 'key_2': 'val_2'}
```
> 1. Unordered collection of items i.e. can't be indexed
> 2. Other compound data tupes have only values as an element, whereas a dictionary has a KEY:VALUE pair
> 3. Keys are unique, values may not be unique
> 4. Values can be of any type, but key must be immutable
