%global sha cd571e3cebb7c00de9168126b28852f32fb204ed
Summary: Terminal Benchmarking as CLI and library.
Name: termbench-pro
Version: 20220216
Release: 1%{?dist}
URL: https://github.com/contour-terminal/termbench-pro
License: APL 2.0
Source: https://github.com/contour-terminal/termbench-pro/archive/%{sha}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  make
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++

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
# No test as fg is not usable

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libtermbench.so
%{_bindir}/tbp

%files devel
%doc README.md
%{_includedir}/termbench/

%changelog
* Fri Jun 10 2022 Gerry Agbobada <git@gagbo.net> - 20220216-1
- Initial version
