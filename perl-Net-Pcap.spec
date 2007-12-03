%define	module	Net-Pcap
%define name	perl-%{module}
%define version 0.15
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to pcap(3) LBL packet capture library 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library. The README for libpcap describes itself as:

"a system-independent interface for user-level packet capture.
libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection,
security monitoring, network debugging, etc."

%prep
%setup -q -n %{module}-%{version}

%build
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

