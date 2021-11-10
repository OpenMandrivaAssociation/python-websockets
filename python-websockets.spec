%global pypi_name websockets

Name:           python-%{pypi_name}
Version:        8.1
Release:        %mkrel 2
Summary:        An implementation of the WebSocket Protocol for python with asyncio
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/websockets
Source0:        https://github.com/aaugustin/websockets/archive/%{version}/%{pypi_name}-%{version}.tar.gz

%global _description \
websockets is a library for developing WebSocket servers and clients in\
Python. It implements RFC 6455 with a focus on correctness and simplicity. It\
passes the Autobahn Testsuite.\
\
Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it\
provides an API based on coroutines, making it easy to write highly concurrent\
applications.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        An implementation of the WebSocket Protocol for python with asyncio
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove upstream's egg-info
rm -vrf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
# Remove installed C file
rm -vf %{buildroot}%{python3_sitearch}/%{pypi_name}/speedups.c

%check
# Skip tests because they fail on Python 3.8. See: https://github.com/aaugustin/websockets/issues/648
# WEBSOCKETS_TESTS_TIMEOUT_FACTOR=100 %%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{pypi_name}/
