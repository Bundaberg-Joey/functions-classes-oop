# Lesson Plan
## 1) Modular Code vs Correct Code
* Lots of ways to make a program which returns the correct number
* This lesson focusses on writing code in a good way to get the number
* Code is read and written more often than it is run so needs to be clear and understandable to someone reading it (who isn't you)

## 2) Function Refresh
* Functions are used to save copy pasting code everywhere
* If we want to make a change then only change the code in one location and it is changed everywhere!
* **EXAMPLE :** calcualtion of mean from list of numbers 
* This is a demonstration of modular programming where a module of code is written which can be re-used over and over again
* > Dont Repeat Yourself --> D.R.Y
* Only ever want a function to do one thing (if you describe it using an "and" then it does two things)
* **EXAMPLE :** mean calculation which also does something else
* Show how this can be split into two functions, you could then create a third function which uses both of them if you really wanted
* > Single Responsibility Principle --> S.R.P

* Overall benefit to this is that your code is much simpler and re-usable meaning you can use it with confidence more and **more easily test it**

## 3) Objects and State
* Typically, we want to store information about something for later / current use in a program / script
* In python we do this by creating variables which are objects
* > `float` or `int` : stores numeric data
* > `str`: stores text data
* > `list` or `dict` : Stores multiple objects containing data
* These objects are fairly basic in that we can apply them to many different scenarios and applications fairly well when scripting
* When writing code with a bit more complexity to it however, we will want to start using our own custom objects to make interaction easier or to handle quirks of our data / program
* Again, we want to make sure that this complexity is easy to read and understand!!!!
* (Overall example from this section and below subsections will be creating an object which is a "playing card")

### 3.1) Class syntax in python
* How to create a class and call it
* convention on `CamelCase` for naming

### 3.2) `__init__` method
* allows us to store data in the object when creating new ones
* Going to skip over `self` largely here as it just muddies the waters

### 3.3) Attributes
* What are they
* Setting them
* Accessing them

* Finalise section saying we could have just used a dict up to this point
* Key benefit is however that we are starting small but can easily transform this into something more complex which a dict would not be suited for
* i.e. consistent API for the object we are creating

## 4) Methods
* So we can store data in attributes
* Ideally want to interact with it also in a consistent way
* Methods help us do that by being functions associated with a specific class that can only be called once a class is instantiated (not going to mention static methods)
* Syntax is identical to regular function except also passing the `self` as an argument
* Able to interact with object attributes in the methods (again brings back to the idea of "state") i.e. instead of passing a hodge-podge of arguments to the functions can just pass the core ones since rest are attributes
* **Example :** can add a method or two to the "playing card" created in earlier stage (e.g. flip it over or something)

## 5) Interacting Objects
* Up till now you could've just used dict and external functions
* Consider however when we have two dicts, each storing about different information but are related to each other
* We can create functions that map entries etc to each other and back but as soon as we change something about either dict or function we have to change the other components of the rest of our code also!
* **The power of OOP is that once we have a consistent interface, we can make all sorts of changes to the underlying code without it impacting the remainder of our code!!**
* This makes it much easier to make any changes such as adding functionality or changing the type of data we are passing around / reading from
* Fundamentally it also makes the code easier to read because I dont need to know what the 4th element of the `args` key of the 2nd nested dict is because we can have a simple `get_value()` method which another object can interact with
* **EXAMPLE :** Secondary object `CardDeck` and `PlayerHand` which interacts with `PlayingCard` to store information etc

## 6) Dunder methods
* Can create objects which store data and have methods associated with them to interact with the data and other objects
* Would be nice if our custom objects were a bit more "interactive" and could interact with other objects using native python functionality
* i.e. nice to call `len` on `CardDeck` rather than `len(CardDeck.cards)`
* Can do so with dunder methods
* `__repr__` for string reresetnation of cards, deck, hand
* `__len__` for deck and hand
* `__radd__` and `__ladd__` to get value of the hand (use this to update the get hand value method to use `sum` rather than loop and access value
* `__eq__` for comparing card hands 

## 7) How to Use OOP in your research context
* This has been a very abstract discussion so its hard to know where to start
* General rule of thumb is this:
 > 1. Write your "code goal" as a sentence or series of short sentences
 > 2. The **nouns** become individual **objects**
 > 3. The **adjectives** become object **attributes**
 > 4. The **verbs** become object **methods**
* **EXAMPLE :** "*Taylor the dog barked at Sam the Cat. Sam then hissed, and spat at Taylor*" (also have code describing this)
* Exercise : ask people to do this for their own research and go hands up if anyone is brave

## 8) Inheritance
* Can see that likely there will be an overlap between what you want objects to do
* Ideally would like to re-use that code without having to re-write it all
* recall that by defining a function we dont have to re-use the same code
* This can be achieved in OOP by using inheritance
* Inheritance where one object "inherits" its methods and attributes from a parent class
* **EXAMPLE :** use the cat and dog approach from class `Animal` but make cat have a "spit" method







