The solution I came up with has one person that is designated to keep
track of the amount of missing cupcakes. For clarity and simplification I
provided an algorithm for each role below.

Designated Guest:
    No cupcake:
        Increment counter by 1 and replace cupcake

    If there is a cupcake and you have not eaten one yet:
        Eat the cupcake and replace it

    If there is a cupcake and you have eaten one:
        1. Eat and replace
        2. Leave the cupcake

Regular:
    No cupcake:
        Do not replace even if you have not eaten yet

    If there is a cupcake and you have not eaten one yet:
        Eat the cupcake, but do not replace it 

    If there is a cupcake and you have eaten one:
        1. Eat and replace
        2. Leave the cupcake


This solution works because it only ends one the designated guest counts that they
have seen a missing cupcake n-1 times (excludes the guest themselves). If all other
guests have followed the algorithm, then it is confirmed everybody had at least one cupcake.
