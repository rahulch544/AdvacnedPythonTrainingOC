#!/usr/bin/perl

use IPC::Open3;
use Symbol 'gensym';
use Data::Dumper;

eval{
# my $ret = system(`python -u /Users/rahulch/Downloads/AdvancedPython/remote_machine.py`);
my $temp ='afdfd';
  my $remote_param = "python -u remote_machine.py "." $temp"; 

my $pid = open3(my $chld_in, my $chld_out, my $chld_err = gensym,
                $remote_param);
print "Return value $pid";
waitpid( $pid, 0 );
my $child_exit_status = $? >> 8;
# system ($ret) == 0 or die "command was unable to run to completion:\n$ret\n";
};