%global pypi_name websockets

Name:           python-%{pypi_name}
Version:        14.1
Release:        1
Summary:        An implementation of the WebSocket Protocol for python with asyncio
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/websockets
Source0:        https://pypi.python.org/packages/source/w/websocket/%{pypi_name}-%{version}.tar.gz

%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description 
websockets is a library for developing WebSocket servers and clients in\
Python. It implements RFC 6455 with a focus on correctness and simplicity. It\
passes the Autobahn Testsuite.

Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it\
provides an API based on coroutines, making it easy to write highly concurrent\
applications.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove upstream's egg-info
rm -vrf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install
# Remove installed C file
rm -vf %{buildroot}%{python_sitearch}/%{pypi_name}/speedups.c

%files
%license LICENSE
%doc README.rst
%{python_sitearch}/websockets-%{version}.dist-info
%{python_sitearch}/%{pypi_name}/
