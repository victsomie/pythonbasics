"""
FOR/ELSE Statement
==============
Just like with while, for loops may have an else associated with them.

In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. This code will break when it hits 'tomato', so the else block won't be executed.
=================
"""

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

print
print "NOTE: The else part runs in the below code ccase there \
is no tomato"
"""
======================
FOR/ELSE that run the else statement
NOTE: The else part run here
"""
