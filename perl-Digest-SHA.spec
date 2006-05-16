#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA
Summary:	Digest::SHA - interface to the SHA algorithm
Summary(pl):	Digest::SHA - interfejs do algorytmu SHA
Name:		perl-Digest-SHA
Version:	5.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	51be3fe2ac74c7c78109222c8e895abd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard. It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.
The module can handle all types of input, including partial-byte
data.

%description -l pl
Digest::SHA to pe³na implementacja standardu NIST Secure Hash.
Udostêpnia programistom perlowym wygodny sposób obliczania skrótów
wiadomo¶ci SHA-1, SHA-224, SHA-256, SHA-384 i SHA-512. Ten modu³
potrafi obs³u¿yæ wszelkie rodzaje wej¶cia, w³±cznie z danymi
sk³adaj±cymi siê z czê¶ci bajtów.

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
