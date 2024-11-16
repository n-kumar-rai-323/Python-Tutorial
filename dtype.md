Python Data Types
Data Types	Classes	Description
Numeric	int, float, complex	holds numeric values
String	str	holds sequence of characters
Sequence	list, tuple, range	holds collection of items
Mapping	dict	holds data in key-value pair form
Boolean	bool	holds either True or False
Set	set, frozenset	hold collection of unique items
Since everything is an object in Python programming, data types are actually classes and variables are instances(object) of these classes.

Python Numeric Data type
In Python, numeric data type is used to hold numeric values.

Integers, floating-point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

int - holds signed integers of non-limited length.
float - holds floating decimal points and it's accurate up to 15 decimal places.
complex - holds complex numbers.
We can use the type() function to know which class a variable or a value belongs to.

Let's see an example,

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))
Run Code
Output

5 is of type <class 'int'>
2.0 is of type <class 'float'>
(1+2j) is of type <class 'complex'>
In the above example, we have created three variables named num1, num2 and num3 with values 5, 5.0, and 1+2j respectively.

We have also used the type() function to know which class a certain variable belongs to.

Since,

5 is an integer value, type() returns int as the class of num1 i.e <class 'int'>
2.0 is a floating value, type() returns float as the class of num2 i.e <class 'float'>
1 + 2j is a complex number, type() returns complex as the class of num3 i.e <class 'complex'>
Python List Data Type
List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]. For example,

languages = ["Swift", "Java", "Python"]

Here, we have created a list named languages with 3 string values inside it.

Access List Items
To access items from a list, we use the index number (0, 1, 2 ...). For example,

languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0])   # Swift

# access element at index 2
print(languages[2])   # Python
Run Code
In the above example, we have used the index values to access items from the languages list.

languages[0] - access first item from languages i.e. Swift
languages[2] - access third item from languages i.e. Python
To learn more about lists, visit Python List.

Python Tuple Data Type
Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

In Python, we use the parentheses () to store items of a tuple. For example,

product = ('Xbox', 499.99)
Here, product is a tuple with a string value Xbox and a float value 499.99.

Access Tuple Items
Similar to lists, we use the index number to access tuple items in Python . For example,

# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])   # Microsoft

# access element at index 1
print(product[1])   # Xbox
Run Code
To learn more about tuples, visit Python Tuples.

Python String Data Type
String is a sequence of characters represented by either single or double quotes. For example,

name = 'Python'
print(name)  

message = 'Python for beginners'
print(message)
Run Code
Output

Python
Python for beginners
In the above example, we have created string-type variables: name and message with values 'Python' and 'Python for beginners' respectively.

To learn more about strings, visit Python Strings.

Python Set Data Type
Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }. For example,

# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))
Run Code
Output

{112, 114, 115, 116, 118}
<class 'set'>
Here, we have created a set named student_info with 5 integer values.

Since sets are unordered collections, indexing has no meaning. Hence, the slicing operator [] does not work.

To learn more about sets, visit Python Sets.

Python Dictionary Data Type
Python dictionary is an ordered collection of items. It stores elements in key/value pairs.

Here, keys are unique identifiers that are associated with each value.

Let's see an example,

# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)
Run Code
Output

{'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
In the above example, we have created a dictionary named capital_city. Here,

Keys are 'Nepal', 'Italy', 'England'
Values are 'Kathmandu', 'Rome', 'London'
Access Dictionary Values Using Keys
We use keys to retrieve the respective value. But not the other way around. For example,

# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city['Nepal'])  # prints Kathmandu

print(capital_city['Kathmandu'])  # throws error message 
Run Code
Here, we have accessed values using keys from the capital_city dictionary.

Since 'Nepal' is key, capital_city['Nepal'] accesses its respective value i.e. Kathmandu

However, 'Kathmandu' is the value for the 'Nepal' key, so capital_city['Kathmandu'] throws an error message.