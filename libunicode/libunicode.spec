%global sha 94e0eeadadf61a957b1184ea276e7d94e0d40cf9
Summary: Modern C++17 Unicode Library
Name: libunicode
Version: 20220216
Release: 1%{?dist}
URL: https://github.com/contour-terminal/libunicode
License: APL 2.0
Source: https://github.com/contour-terminal/libunicode/archive/%{sha}.tar.gz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: fmt-devel
BuildRequires: pkgconfig(catch2) pkgconf

%description
Later.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{sha}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_test

%files
%license LICENSE
%doc README.md
%{_includedir}/libunicode/
%{_libdir}/libunicode*

%files devel
%{_includedir}/libunicode/

%changelog
* Fri Jun 10 2022 Gerry Agbobada <git@gagbo.net> - 20220216-1
- Initial version
