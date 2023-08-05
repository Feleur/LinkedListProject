# LinkedListProject

For a short description which might be useful if anything is confusing:

1. It wasn't sure if structure once initialized may allow *only one type* so I decided to use if statement in push() method which check is self.head is None. In this situation any time we make our our List empty, we can push and work on any other data type we want to.
2. pop() method has 3 options:
  * remove from index X;
  * remove first meet value;
  * remove all occurrences of a value;
In this situation I wasn't sure if you expect one method, which connect all three possibilities or three different methods, but I went into the second option. It could be done with method overloading such as pop(self, value=0, index=0, occurrences=No) or similar with changing parameters but it would make a little bit more chaos.
3. You listed three Errors - FullList, NoSuchElement, NoSuchIndex so I set up them in Exceptions module, but additionally I've added PushIncorrectType is a situation when we want to put wrong type object and PopOnEmptyList which doesn't need any explenations.
4. I didn't know what excatly you wanted by "test the solution" but in main module there are some methods which are comparing decorators with 1000-element object and some "dummy method" named test_of_linked_list. Inside I used many methods step-by-step which prints all informations in important moments. I tested it also for raising Exceptions - for this you can change params of 1st line or any pop()'s method.
5. Finally I've implemented __ iter __ and __ next __ methods for allowing them to iterate and used this methodology in pop_by_index() and pop_by_value(). To be honest it's quite slower than different approaches but may show it works.

If you have any other questions or doubts, I hope, I will have an opportunity to explain anything needed.
