%include	/usr/lib/rpm/macros.python
Summary:	Tagged Message Delivery Agent
Summary(pl):	Agent (MDA) dostarczaj±cy oznaczone wiadomo¶ci
Name:		tmda
Version:	1.1.4
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://tmda.sf.net/releases/unstable/%{name}-%{version}.tgz
# Source0-md5:	58c79099ea0cd4bfc48f85de5502a2f2
URL:		http://tmda.sourceforge.net/
BuildRequires:	python-devel >= 2.3.3
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tmda,%{py_libdir}/site-packages/TMDA,%{py_libdir}/site-packages/TMDA/pythonlib/email}

install bin/tmda-* $RPM_BUILD_ROOT%{_bindir}
install templates/*.txt $RPM_BUILD_ROOT%{_datadir}/tmda
install TMDA/*.{py,pyc} $RPM_BUILD_ROOT%{py_libdir}/site-packages/TMDA
install TMDA/pythonlib/email/*.{py,pyc} $RPM_BUILD_ROOT%{py_libdir}/site-packages/TMDA/pythonlib/email
install contrib/{collectaddys,printcdb,printdbm} $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_libdir}
%py_comp $RPM_BUILD_ROOT%{py_libdir}
rm -f htdocs/{ChangeLog,Makefile,*.h,*.ht,*.py*,*.tpl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CRYPTO README THANKS UPGRADE contrib htdocs
%attr(755,root,root) %{_bindir}/*
%dir %{py_libdir}/site-packages/TMDA
%{py_libdir}/site-packages/TMDA/*.py[co]
%dir %{py_libdir}/site-packages/TMDA/pythonlib/email
%{py_libdir}/site-packages/TMDA/pythonlib/email/*.py[co]
%{_datadir}/tmda
