Summary:	Python C JSON - Fast JSON encoder/decoder for Python
Name:		python-cjson
Version:	1.0.5
Release:	3
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/python-cjson/%{name}-%{version}.tar.gz
# Source0-md5:	4d55b66ecdf0300313af9d030d9644a3
URL:		http://pypi.python.org/pypi/python-cjson/
BuildRequires:	python-devel >= 1:2.5.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a very fast JSON encoder/decoder for Python.
The module is written in C and it is up to 250 times faster when
compared to the other python JSON implementations which are written
directly in python.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/python_cjson-%{version}-py*.egg-info
%{py_sitedir}/cjson.so
