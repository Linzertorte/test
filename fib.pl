#! /usr/bin/perl
use strict;
use warnings;

my $email = 'liuzhaoliang1988@gmail.com';

if($email =~ /([^@]+)@(.+)/){
    print "Username is $1\n";
    print "Hostname is $2\n"
}

sub fib{
    my $n = shift;
    if($n == 0 || $n == 1){
	return $n;
    }
    else{
	return fib($n-1)+fib($n-2);
    }
}

print fib(10);
print "\n";
