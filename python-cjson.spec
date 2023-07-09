Summary:	Python C JSON - Fast JSON encoder/decoder for Python
Summary(pl.UTF-8):	Python C JSON - szybki koder/dekoder JSON dla Pythona
Name:		python-cjson
Version:	1.2.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-cjson/%{name}-%{version}.tar.gz
# Source0-md5:	187e43d94a78694129bf25e541a74cd5
URL:		https://pypi.org/project/python-cjson/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a very fast JSON encoder/decoder for Python.
The module is written in C and it is up to 250 times faster when
compared to the other python JSON implementations which are written
directly in python.

%description -l pl.UTF-8
Ten moduł to bardzo szybka implementacja kodera/dekodera JSON dla
Pythona. Moduł jest napisany w C i jest do 250 razy szybszy w stosunku
do innych implementacji JSON, napisanych bezpośrednio w Pythonie.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%attr(755,root,root) %{py_sitedir}/cjson.so
%{py_sitedir}/python_cjson-%{version}-py*.egg-info
