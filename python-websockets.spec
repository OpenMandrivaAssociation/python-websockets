%global module websockets

Name:           python-%{module}
Version:        16.0
Release:        1
Summary:        An implementation of the WebSocket Protocol for python with asyncio
Group:          Development/Python
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/websockets
Source0:        https://pypi.python.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description 
websockets is a library for developing WebSocket servers and clients in\
Python. It implements RFC 6455 with a focus on correctness and simplicity. It\
passes the Autobahn Testsuite.

Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it\
provides an API based on coroutines, making it easy to write highly concurrent\
applications.

%prep -a
# Remove upstream's egg-info
rm -vrf src/%{module}.egg-info

%install -a
# Remove installed C file
rm -vf %{buildroot}%{python_sitearch}/%{module}/speedups.c

%files
%license LICENSE
%doc README.rst
%{_bindir}/%{module}
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
