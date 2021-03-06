#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Digest
%define		pnam	SHA
Summary:	Digest::SHA - interface to the SHA algorithm
Summary(pl.UTF-8):	Digest::SHA - interfejs do algorytmu SHA
Name:		perl-Digest-SHA
Version:	6.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e22f92fa4e2d7ec9b1168538b307d31c
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
	CC="%{__cc}" \
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
%attr(755,root,root) %{_bindir}/shasum
%{perl_vendorarch}/Digest/SHA.pm
%dir %{perl_vendorarch}/auto/Digest/SHA
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/SHA/SHA.so
%{_mandir}/man1/shasum.1p*
%{_mandir}/man3/Digest::SHA.3pm*
