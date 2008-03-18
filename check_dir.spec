%define version 2.1.1
%define release 0
%define name    check_dir
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Nagios plugin to monitor the number of files in one or more directories.
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Nagios plugin to monitor the number of files in one or more directories.

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN1DIR=%{buildroot}/usr/share/man/man1
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/%{name}
%attr(0755, root, root) /usr/share/man/man1/%{name}.1.gz

%changelog
* Tue Mar 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.1-0
- added more sanity checks

* Tue Mar 18 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 2.1.0-0
- accepts ranges for -c and -w

* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- first RPM package

# /usr/share/man/man1/check_dir.1
