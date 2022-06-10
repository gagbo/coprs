Summary: The Guidelines Support Library
Name: guidelines-support-lib-devel
Version: 3.1.0
Release: 1%{?dist}
URL: https://github.com/microsoft/GSL
License: MIT
Source: https://github.com/microsoft/GSL/archive/refs/tags/v{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

Requires: pkgconfig

%description
The Guidelines Support Library (GSL) contains functions and
types that are suggested for use by the C++ Core Guidelines
maintained by the Standard C++ Foundation.

%prep
%setup -q -n %{name}-%{version}

%build

%install
cp -r include/gsl %{buildroot}%{_includedir}
cp cmake/guidelineSupportLibrary.cmake 

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_includedir}/gsl/algorithm
%{_includedir}/gsl/assert
%{_includedir}/gsl/byte
%{_includedir}/gsl/gsl
%{_includedir}/gsl/gsl_algorithm
%{_includedir}/gsl/gsl_assert
%{_includedir}/gsl/gsl_byte
%{_includedir}/gsl/gsl_narrow
%{_includedir}/gsl/gsl_util
%{_includedir}/gsl/narrow
%{_includedir}/gsl/pointer
%{_includedir}/gsl/span
%{_includedir}/gsl/span_ext
%{_includedir}/gsl/string_span
%{_includedir}/gsl/util
/cmake/guidelineSupportLibrary.cmake



%changelog
* Fri Jun 10 2022 Gerry Agbobada <git@gagbo.net> - 3.0-1
- Bump version to version 3
