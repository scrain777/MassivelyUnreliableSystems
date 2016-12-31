package SimErr;

use strict;

use Exporter;
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

$VERSION=1.00;
@ISA=qw(Exporter);
@EXPORT=qw(siminit simerror simfix simdone);
@EXPORT_OK=();

our $log;
our $errors=0;
our $fixed=0;

# Initialize
#
# Input: The name of a file in which to log the errors and fixes.
#
sub siminit($)
{ my($filename)=@_;

  open($log,">>$filename") || die("siminit: Error opening simulation results logfile.");
}

# Simulate an error condition.
#
# Input: the number of lines in the calling function. More lines indicates
#        higher complexity so we simulate more errors.
#
# Return: 1 indicates that an error is to be simulated. 0 indicates no error.
#
sub simerror($$)
{ my($func, $lines)=@_;
  $func=~s/\n/ /g; # Do not want any cheating...

  if($lines<1 || rand()<$lines*$lines*1e-6)
  { $errors++;
    print $log "Hit error $errors in function $func.\n";
    return 1;
  }

  return 0;
}

# Record a correction from a simulated error.
#
# Input: message indicating how the error was handled.
#
sub simfix($)
{ my($msg)=@_;

  $msg=~s/\n/ /g; # Do not want any cheating...
  $fixed++;
  print $log "Error fix [$fixed/$errors]: $msg\n";
}

# Print a final summary and close the log.
#
sub simdone()
{ print $log "\n\nSummary: Fixed $fixed/$errors\n";
  close($log);
}

1;
