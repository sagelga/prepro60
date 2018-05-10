# Dictionary
Dictionary is similar to list. But they will require these two to complete:

- Key
- Value

Where key is for keeping the value (like variable, but you may use numbers and strings)
And the value will store the value of the key.

# Creating your new dictionary
```python
my_dictionary = dict()
```

or you can start defining your dictionary

```python
my_dictionary = {
"happy" : 20,
"not happy" : 30,
"sad" : False,
}
```

# Accessing the value from key
```python
my_dictionary['happy'] # Returns 20
```

or checking if this key or value exists in dictionary

```python
"happy" in my_dictionary # Return true
20 in my_dictionary # Return true
```

# Adding key and value to the dictionary
You can add it like list.
```python
alphabet = input()
my_dictionary = dict()

for i in alphabet:
    if not i in my_dictionary:
      my_dictionary[i] = 1
    else:
      my_dictionary += 1

```
