Summary:	A GNU general-purpose parser generator
Name:		bison
Version:	2.6.5
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/bison/%{name}-%{version}.tar.xz
# Source0-md5:	75c8508e0a9e5c68f608658672d6bda4
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	m4
BuildRequires:	texinfo
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgdatadir	%{_datadir}/bison

%description
Bison is a general purpose parser generator which converts a grammar
description for an LALR context-free grammar into a C program to parse
that grammar. Bison can be used to develop a wide range of language
parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using Bison
(but you do need to be very proficient in C programming to be able to
use Bison). Many programs use Bison as part of their build process.
Bison is only needed on systems that are used for development.

%package runtime
Summary:	Runtime library for programs containing bison-generated parsers
Group:		Libraries

%description runtime
Runtime library for internationalized programs containing
bison-generated parsers.

%prep
%setup -q

sed -i -e 's|examples tests|tests|' Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make} \
	pkgdatadir=%{pkgdatadir}

%check
cd tests
./testsuite

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdatadir=%{pkgdatadir}

%find_lang %{name}
%find_lang %{name}-runtime

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/bison
%attr(755,root,root) %{_bindir}/yacc
%{pkgdatadir}
%{_libdir}/lib*.a
%{_aclocaldir}/bison-i18n.m4
%{_mandir}/man1/bison.1*
%{_infodir}/*.info*

%files runtime -f %{name}-runtime.lang
%defattr(644,root,root,755)

