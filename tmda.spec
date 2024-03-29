Summary:	Tagged Message Delivery Agent
Summary(pl.UTF-8):	Agent (MDA) dostarczający oznaczone wiadomości
Name:		tmda
Version:	1.1.4
Release:	7
License:	GPL
Group:		Networking/Daemons
Source0:	http://tmda.sf.net/releases/unstable/%{name}-%{version}.tgz
# Source0-md5:	58c79099ea0cd4bfc48f85de5502a2f2
URL:		http://tmda.sourceforge.net/
BuildRequires:	python-devel >= 1:2.3.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TMDA is an OSI certified software application designed to
significantly reduce the amount of SPAM/UCE (junk-mail) you receive.
TMDA combines a "whitelist" (for known/trusted senders), a "blacklist"
(for undesired senders), and a cryptographically enhanced confirmation
system (for unknown, but legitimate senders).

%description -l pl.UTF-8
TMDA to oprogramowanie zaprojektowane by zredukować liczbę spamu,
który otrzymujesz. TMDA łączy w sobie "białą listę" (dla znanych /
zaufanych nadawców), "czarną listę" (dla niepożądanych nadawców) oraz
system potwierdzania wiadomości (dla nieznanych ale prawidłowych
nadawców).

%prep
%setup -q

%build
python ./compileall

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tmda,%{py_scriptdir}/site-packages/TMDA/pythonlib/email}

install bin/tmda-* $RPM_BUILD_ROOT%{_bindir}
install templates/*.txt $RPM_BUILD_ROOT%{_datadir}/tmda
install TMDA/*.{py,pyc} $RPM_BUILD_ROOT%{py_scriptdir}/site-packages/TMDA
install TMDA/pythonlib/email/*.{py,pyc} $RPM_BUILD_ROOT%{py_scriptdir}/site-packages/TMDA/pythonlib/email
install contrib/{collectaddys,printcdb,printdbm} $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_scriptdir}
%py_comp $RPM_BUILD_ROOT%{py_scriptdir}
rm -f htdocs/{ChangeLog,Makefile,*.h,*.ht,*.py*,*.tpl}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CRYPTO README THANKS UPGRADE contrib htdocs
%attr(755,root,root) %{_bindir}/*
%dir %{py_scriptdir}/site-packages/TMDA
%{py_scriptdir}/site-packages/TMDA/*.py[co]
%dir %dir %{py_scriptdir}/site-packages/TMDA/pythonlib
%dir %{py_scriptdir}/site-packages/TMDA/pythonlib/email
%{py_scriptdir}/site-packages/TMDA/pythonlib/email/*.py[co]
%{_datadir}/tmda
