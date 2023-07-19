# Seminar 3: Testing with Python // exploring linters
## Question 1:

After installing pylint using the command pip3 install pylint I ran the command pylint pylintTest.py

The first report came back with general syntax and convetion errors. First, I removed:

- Indentation errors
- Added a docstring
- Renamed the file to pylint test to comply with snake case standards
- Changed the variable ‘raw input’ to just ‘input’
- Corrected spacing errors around the operator ‘=’
- Added parentheses to the print statement variable

I then ran pylint again. I was still getting these errors:

    pylint_test.py:9:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
    pylint_test.py:17:22: E0602: Undefined variable 'encoded' (undefined-variable)
    pylint_test.py:19:16: E0602: Undefined variable 'letters' (undefined-variable)
    pylint_test.py:20:20: E0602: Undefined variable 'encoded' (undefined-variable)
    pylint_test.py:20:30: E0602: Undefined variable 'letters' (undefined-variable)
    pylint_test.py:20:38: E0602: Undefined variable 'x' (undefined-variable)
    pylint_test.py:22:12: W0621: Redefining name 'letter' from outer scope (line 15) (redefined-outer-name)
    pylint_test.py:24:30: E0602: Undefined variable 'encoded' (undefined-variable)
    pylint_test.py:26:24: E0602: Undefined variable 'letters' (undefined-variable)
    pylint_test.py:27:30: E0602: Undefined variable 'encoded' (undefined-variable)
    pylint_test.py:27:40: E0602: Undefined variable 'letters' (undefined-variable)
    pylint_test.py:27:48: E0602: Undefined variable 'x' (undefined-variable)
    pylint_test.py:29:6: E0602: Undefined variable 'encoded' (undefined-variable)

Using the following command, I could try to solve the UPPERCASE error: 

    codio@deletechrome-beachbicycle:~/workspace$ pylint --const-rgx='[a-z_][a-z0-9_]{2,30}$' pylint_test.py
    
Which returned the following:

    ************* Module pylint_test
    pylint_test.py:19:12: C0103: Constant name "x" doesn't conform to '[a-z_][a-z0-9_]{2,30}$' pattern (invalid-name)
    pylint_test.py:22:12: W0621: Redefining name 'letter' from outer scope (line 15) (redefined-outer-name)
    pylint_test.py:26:20: C0103: Constant name "x" doesn't conform to '[a-z_][a-z0-9_]{2,30}$' pattern (invalid-name)

    ------------------------------------------------------------------
    Your code has been rated at 8.42/10 (previous run: 2.11/10, +6.32)

Ref: https://docs.pylint.org/tutorial.html

## Question 2:

With flake8 on pylintTest.py, after correcting the indentation errors the only error which was thrown back was and indentation error:

    codio@deletechrome-beachbicycle:~/workspace$ flake8 pylintTest.py
    pylintTest.py:1:1: E902 IndentationError: unindent does not match any outer indentation level

On the file metricTest.py, running flake8 returned the following:

    codio@deletechrome-beachbicycle:~/workspace$ flake8 metricTest.py
    metricTest.py:10:1: E302 expected 2 blank lines, found 1
    metricTest.py:14:1: E302 expected 2 blank lines, found 1
    metricTest.py:14:58: W291 trailing whitespace
    metricTest.py:15:37: E128 continuation line under-indented for visual indent
    metricTest.py:15:51: W291 trailing whitespace
    metricTest.py:16:37: E128 continuation line under-indented for visual indent
    metricTest.py:16:60: W291 trailing whitespace
    metricTest.py:17:37: E128 continuation line under-indented for visual indent
    metricTest.py:20:5: E303 too many blank lines (2)
    metricTest.py:22:9: E225 missing whitespace around operator
    metricTest.py:26:9: E225 missing whitespace around operator
    metricTest.py:26:17: E999 SyntaxError: invalid syntax
    metricTest.py:30:9: E225 missing whitespace around operator
    metricTest.py:31:13: E225 missing whitespace around operator
    metricTest.py:34:15: E225 missing whitespace around operator
    metricTest.py:36:55: E231 missing whitespace after ','
    metricTest.py:36:80: E501 line too long (100 > 79 characters)
    metricTest.py:37:1: W293 blank line contains whitespace
    metricTest.py:38:15: E225 missing whitespace around operator
    metricTest.py:40:47: W291 trailing whitespace
    metricTest.py:47:25: E231 missing whitespace after ','
    metricTest.py:50:1: W293 blank line contains whitespace
    metricTest.py:53:1: W293 blank line contains whitespace
    metricTest.py:56:18: E225 missing whitespace around operator
    metricTest.py:58:15: E225 missing whitespace around operator
    metricTest.py:59:21: E225 missing whitespace around operator
    metricTest.py:61:1: E302 expected 2 blank lines, found 1
    metricTest.py:66:1: W293 blank line contains whitespace
    metricTest.py:67:18: E231 missing whitespace after ','
    metricTest.py:68:13: E225 missing whitespace around operator
    metricTest.py:69:13: E113 unexpected indentation
    metricTest.py:75:18: E225 missing whitespace around operator
    metricTest.py:78:28: W292 no newline at end of file

I corrected the syntax and stylistic errors but was still receiving the following errors, which I couldn’t fix:

    codio@deletechrome-beachbicycle:~/workspace$ flake8 metricTest.py
    metricTest.py:25:19: E999 SyntaxError: invalid syntax
    metricTest.py:71:13: E113 unexpected indentation


## Question 3:

This is the code snippet (sums.py):

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    
if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

Running mccabe on sums.py produces:

    codio@deletechrome-beachbicycle:~/workspace$ python -m mccabe sums.py
    ("4:0: 'test_sum'", 1)
    ('If 7', 2)

This is the second code snippet (sums2.py):

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
```

Running mccabe on sums2.py produces:

    codio@deletechrome-beachbicycle:~/workspace$ python -m mccabe sums2.py
    ("7:0: 'test_sum_tuple'", 1)
    ("4:0: 'test_sum'", 1)
    ('If 10', 2)

Question: What are the contributors to the cyclomatic complexity in each piece of code?

In the first example, there is only one independent path through the code: - the ```test_sum()``` function. The ```if __name__ == "__main__":``` block is executed when the Python script is run as the main module. It calls the function and prints "everything passed". It does not add cyclomatic complexity because it does not introduce new decision points. The cyclomatic complexity should therefore be 1.

In the second example (sums2.py), the cyclomatic complexity is 2 because the ```test_sum()``` function and the ```test_sum_tuple()``` function present 2 independent paths through the code. The ```if __name__ == "__main__":``` block i executed when the Python script is run as the main module. It calls both functions and prints "everything passed".
