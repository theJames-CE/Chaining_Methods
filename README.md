# Chaining_Methods

In the last assignment, your code might have looked something like this:

![image](https://github.com/theJames-CE/Chaining_Methods/assets/124546382/7ddfcce4-d2d1-4244-9098-a5cde8ea8458)

This takes up a lot of space and we're repeating our call to user1 and user2 many times. 

<h2>Short-cut!</h2>

There is a way to call on <i>user1</i> just once and keep attaching new method calls to the end of the previous one, like so:

![image](https://github.com/theJames-CE/Chaining_Methods/assets/124546382/813beedc-5371-4b92-958f-5ee5963fb25b)

This is called <b>chaining</b>. In order for this to work, each method must return <i>self</i>. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.<br>

For example if <b><i>user1.spend_points(50)</b></i> returns its own instance (user1 ), then we can call one of that instance's methods after that call, like <b><i>user1.spend_points(50).display_info()</b></i>.

![image](https://github.com/theJames-CE/Chaining_Methods/assets/124546382/c89d2e24-a82b-474b-862e-c7fa996ea1f1)

The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not <b><i>self</b></i>, but instead <b><i>this</b></i>.

<b>Note:</b> This only works with methods that do not need to return anything. If your method needs to return something other than self, it is not possible to chain the method.

![image](https://github.com/theJames-CE/Chaining_Methods/assets/124546382/60289157-30e1-4dbb-ad9a-c5b23d4de66c)

#CodingDojo
