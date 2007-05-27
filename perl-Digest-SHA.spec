#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA
Summary:	Digest::SHA - interface to the SHA algorithm
Summary(pl.UTF-8):	Digest::SHA - interfejs do algorytmu SHA
Name:		perl-Digest-SHA
Version:	5.44
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bddab365973a795baddc3ec3fb84d16e
URL:		http://search.cpan.org/dist/Digest-SHA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard. It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.
The module can handle all types of input, including partial-byte
data.

%description -l pl.UTF-8
Digest::SHA to pełna implementacja standardu NIST Secure Hash.
Udostępnia programistom perlowym wygodny sposób obliczania skrótów
wiadomości SHA-1, SHA-224, SHA-256, SHA-384 i SHA-512. Ten moduł
potrafi obsłużyć wszelkie rodzaje wejścia, włącznie z danymi
składającymi się z części bajtów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Digest/*
%dir %{perl_vendorarch}/auto/Digest/*
%{perl_vendorarch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/*/*.so
%{_mandir}/man1/*
%{_mandir}/man3/*
