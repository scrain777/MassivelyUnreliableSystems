#ifndef SIMERR_H
#define SIMERR_H

/* Initialize
 *
 * Input: The name of a file in which to log the errors and fixes.
 *
 * Return: 0 if OK, -1 if error.
 */
int siminit(char *filename);

/* Simulate an error condition.
 *
 * Input: the number of lines in the calling function. More lines indicates
 *        higher complexity so we simulate more errors.
 *
 * Return: 1 indicates that an error is to be simulated. 0 indicates no error.
 */
int simerror(char *func, int lines);

/* Record a correction from a simulated error.
 *
 * Input: message indicating how the error was handled.
 */
int simfix(char *msg);

/* Print a final summary and close the log.
 *
 * Return value: 0 if OK, -1 if error.
 */
int simdone();

#endif
