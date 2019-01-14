%define	upstream_name	 Net-Pcap
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.18
Release:	1

Summary:	Interface to pcap(3) LBL packet capture library 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Net/Net-Pcap-0.18.tar.gz
# Adapt a test to libpcap-1.8.0, bug #1375919, CPAN RT#117831
Patch0:		Net-Pcap-0.18-Adapt-a-test-to-libpcap-1.8.0.patch
BuildRequires:	pcap
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel
#BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library.
The README for libpcap describes itself as:

"a system-independent interface for user-level packet capture.
libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection,
security monitoring, network debugging, etc."

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
%{__perl} Makefile.PL INC=-I/usr/include/pcap LIBS='-L/usr/lib64/ -lpcap'
%{__perl} Makefile.PL INSTALLDIRS=vendor --defaultdeps
%make

%check
%__make test

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__rm -rf %{buildroot}%{perl_archlib}/perllocal.pod
%__rm -rf %{buildroot}%{perl_archlib}/Net/._Pcap.pm

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.160.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 407822
- rebuild using %%perl_convert_version

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.16-5mdv2009.1
+ Revision: 298348
- rebuilt against libpcap-1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.16-3mdv2009.0
+ Revision: 246162
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 152905
- update to new version 0.16
- update to new version 0.16

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.15-2mdv2008.1
+ Revision: 151343
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - wrap description

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 115266
- fix build dependencies
- new version

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.14-1mdv2008.0
+ Revision: 20671
- 0.14


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-3mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-2mdk
- BuildRequires

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- 0.12

* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.11-1mdk
- 0.11

* Wed Nov 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- 0.10
- Add regression tests (now can be run as non-root)

* Fri Oct 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-1mdk
- 0.08

* Fri Sep 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- New version
- Put meaningful description

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.05-2mdk
- Rebuild for new perl

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.05-1mdk
- 0.05
- drop explicit library depdency
- fix buildrequires (lib64..)
- cosmetics

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.04-7mdk
- Use %%makeinstall_std now that it works on klama
- Remove PREFIX from Makefile.PL

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.04-6mdk
- use %%make and %%makeinstall

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 0.04-5mdk
- Fix man page path
- Macroify and use the perl specific macros
- Cleanout some commented out stuff

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-4mdk
- rebuild for new auto{prov,req}


