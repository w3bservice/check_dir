#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 16;

our $VERSION = '3.0.0';

use_ok('Carp');

use_ok('English');

use_ok('Monitoring::Plugin');
can_ok( 'Monitoring::Plugin', 'new' );
can_ok( 'Monitoring::Plugin', 'nagios_exit' );
can_ok( 'Monitoring::Plugin', 'add_perfdata' );

use_ok('Monitoring::Plugin::Range');
can_ok( 'Monitoring::Plugin::Range', 'parse_range_string' );

use_ok('Monitoring::Plugin::Getopt');
can_ok( 'Monitoring::Plugin::Getopt', 'new' );
can_ok( 'Monitoring::Plugin::Getopt', 'arg' );
can_ok( 'Monitoring::Plugin::Getopt', 'getopts' );
can_ok( 'Monitoring::Plugin::Getopt', 'get' );

use_ok('Monitoring::Plugin::Threshold');
can_ok( 'Monitoring::Plugin::Threshold', 'new' );
can_ok( 'Monitoring::Plugin::Threshold', 'set_thresholds' );

