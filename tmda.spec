%include	/usr/lib/rpm/macros.python
Summary:	Tagged Message Delivery Agent
Summary(pl):	Agent (MDA) dostarczaj±cy oznaczone wiadomo¶ci
Name:		tmda
Version:	1.0
Release:	0.9
License:	GPL
Group:		Networking/Daemons
Source0:	http://tmda.net/releases/%{name}-%{version}.tgz
# Source0-md5:	6823af3edeffcf390ec4dc630a46f8c0
URL:		http://tmda.sourceforge.net/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TMDA is an OSI certified software application designed to
significantly reduce the amount of SPAM/UCE (junk-mail) you receive.
TMDA combines a "whitelist" (for known/trusted senders), a "blacklist"
(for undesired senders), and a cryptographically enhanced confirmation
system (for unknown, but legitimate senders).

%description -l pl
TMDA to oprogramowanie zaprojektowane by zredukowaæ liczbê spamu,
który otrzymujesz. TMDA ³±czy w sobie "bia³± listê" (dla znanych /
zaufanych nadawców), "czarn± listê" (dla niepo¿±danych nadawców) oraz
system potwierdzania wiadomo¶ci (dla nieznanych ale prawid³owych
nadawców).

%prep
%setup -q

%build
python ./compileall

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tmda,%{py_libdir}/TMDA}

install bin/tmda-* $RPM_BUILD_ROOT%{_bindir}
install templates/*.txt $RPM_BUILD_ROOT%{_datadir}/tmda
install TMDA/*.{py,pyc} $RPM_BUILD_ROOT%{py_libdir}/TMDA
install contrib/{collectaddys,printcdb,printdbm} $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_libdir}
%py_comp $RPM_BUILD_ROOT%{py_libdir}
rm -f htdocs/{ChangeLog,Makefile,*.h,*.ht,*.py*,*.tpl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CRYPTO README THANKS UPGRADE contrib/sample.config htdocs
%attr(755,root,root) %{_bindir}/*
%dir %{py_libdir}/TMDA
%{py_libdir}/TMDA/*.py[co]
%{_datadir}/tmda
