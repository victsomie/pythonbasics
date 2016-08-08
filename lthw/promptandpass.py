from sys import argv

script, user_name = argv

prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "What is you name?"
raw_input(prompt)
