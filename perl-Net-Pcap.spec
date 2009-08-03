%define	upstream_name	 Net-Pcap
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Interface to pcap(3) LBL packet capture library 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libpcap-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library.
The README for libpcap describes itself as:

"a system-independent interface for user-level packet capture.
libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection,
security monitoring, network debugging, etc."

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
