%define	module	Net-Pcap
%define name	perl-Net-Pcap
%define version 0.14
%define release %mkrel 1

Summary:	%{module} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel libpcap-devel libpcap
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Interface to pcap(3) LBL packet capture library.

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
%__rm -rf $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Net/*
%{perl_vendorarch}/auto/Net/Pcap/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

