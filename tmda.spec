%include        /usr/lib/rpm/macros.python
Summary:	Tagged Message Delivery Agent
Summary(pl):	Agent (MDA) dostarczaj�cy oznaczone wiadomo�ci
Name:		tmda
Version:	0.81
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://tmda.net/releases/%{name}-%{version}.tgz
# Source0-md5:	25c8d48d96eafef914f9ca1d3c6c965d
URL:		http://tmda.sourceforge.net/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TMDA is an OSI certified software application designed to
significantly reduce the amount of SPAM/UCE (junk-mail) you receive.
TMDA combines a "whitelist" (for known/trusted senders), a "blacklist"
(for undesired senders), and a cryptographically enhanced confirmation
system (for unknown, but legitimate senders).

%description -l pl
TMDA to oprogramowanie zaprojektowane by zredukowa� liczb� spamu,
kt�ry otrzymujesz. TMDA ��czy w sobie "bia�� list�" (dla znanych /
zaufanych nadawc�w), "czarn� list�" (dla niepo��danych nadawc�w) oraz
system potwierdzania wiadomo�ci (dla nieznanych ale prawid�owych
nadawc�w).

%prep
%setup -q

%build
python ./compileall

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tmda,%{py_libdir}/TMDA}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/htdocs

install bin/tmda-* $RPM_BUILD_ROOT%{_bindir}
install templates/*.txt $RPM_BUILD_ROOT%{_datadir}/tmda
install TMDA/*.{py,pyc} $RPM_BUILD_ROOT%{py_libdir}/TMDA
install contrib/{collectaddys,printcdb,printdbm} $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_libdir}
%py_comp $RPM_BUILD_ROOT%{py_libdir}
cp -f htdocs/{*.html,README} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/htdocs
cp -f ChangeLog CRYPTO INSTALL README THANKS UPGRADE contrib/sample* \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
# compress %%doc manually; automation does not work in this case
gzip -9 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{ChangeLog,CRYPTO,INSTALL,README,THANKS,UPGRADE,htdocs/README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%dir %{py_libdir}/TMDA
%{py_libdir}/TMDA/*.py[co]
%{_datadir}/tmda
