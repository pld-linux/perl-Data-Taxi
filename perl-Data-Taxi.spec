#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Taxi
Summary:	Data::Taxi - Taint-aware, XML-ish data serialization
Name:		perl-Data-Taxi
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d7c981fba542ae8b170e6d31af4c86d
URL:		http://search.cpan.org/dist/Data-Taxi/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Taxi (Taint-Aware XML-Ish) is a data serializer with several handy
features:
- Taint aware. Taxi does not force you to trust the data you are
  serializing. None of the input data is executed.
- Human readable. Taxi produces a human-readable string that
  simplifies checking the output of your objects.
- XML-ish. While full XML compliance is not promised, Taxi produces a
  block of XML-ish data that could probably be read in by other XML
  parsers.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/Taxi.pm
%{_mandir}/man3/*
