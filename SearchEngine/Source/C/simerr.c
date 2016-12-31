#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "simerr.h"

static FILE *log;
static unsigned errors=0, fixed=0;

/* Initialize
 *
 * Input: The name of a file in which to log the errors and fixes.
 *
 * Return: 0 if OK, -1 if error.
 */
int siminit(char *filename)
{ srand48((long)time(NULL));

  if(!(log=fopen(filename,"a")))
  { perror("siminit: Error opening simulation results logfile.");
    return -1;
  }

  return 0;
}

/* Simulate an error condition.
 *
 * Input: the number of lines in the calling function. More lines indicates
 *        higher complexity so we simulate more errors.
 *
 * Return: 1 indicates that an error is to be simulated. 0 indicates no error.
 */
int simerror(char *func, int lines)
{ char *p=func;

  /* Do not want any cheating... */
  while((p=strchr(p,'\n')))
    *p=' ';

  if(lines<1 || drand48() < lines*lines*1e-6)
  { errors++;
    fprintf(log,"Hit error %u in function %s.\n",errors,func);
    return 1;
  }

  return 0;
}

/* Record a correction from a simulated error.
 *
 * Input: message indicating how the error was handled.
 */
int simfix(char *msg)
{ char *p=msg;

  /* Do not want any cheating... */
  while((p=strchr(p,'\n')))
    *p=' ';

  fixed++;
  return -(fprintf(log, "Error fix [%u/%u]: %s\n", fixed, errors, msg) <=0);
}

/* Print a final summary and close the log.
 *
 * Return value: 0 if OK, -1 if error.
 */
int simdone()
{ int ret;

  ret=-(fprintf(log, "\n\nSummary: Fixed %u/%u\n", fixed, errors) <= 0);
  ret|=fclose(log);
  return ret;
}
