import random

errors=0
fixed=0

# Initialize
#
# Input: The name of a file in which to log the errors and fixes.
#
def siminit(filename):
  global log
  log=open(filename,'a')

# Simulate an error condition.
#
# Input: the number of lines in the calling function. More lines indicates
#        higher complexity so we simulate more errors.
#
# Return: 1 indicates that an error is to be simulated. 0 indicates no error.
#
def simerror(func, lines):
  global log
  global errors
  # Do not want any cheating...
  func=func.replace('\n',' ')
  if(lines<1 or random.random() < lines*lines*1e-6):
    errors=errors+1
    log.write('Hit error {0} in function {1}.\n'.format(errors, func))
    return 1
  return 0

# Record a correction from a simulated error.
#
# Input: message indicating how the error was handled.
#
def simfix(msg):
  global log
  global errors
  global fixed
  # Do not want any cheating...
  msg=msg.replace('\n',' ')
  fixed=fixed+1
  log.write('Error fix [{0}/{1}]: {2}\n'.format(fixed, errors, msg))

# Print a final summary and close the log.
#
def simdone():
  global log
  global errors
  global fixed
  log.write('\n\nSummary: Fixed {0}/{1}\n'.format(fixed, errors))
  log.close()

