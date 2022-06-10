# This enables cmake to work consistently between pre-f33 and after.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/#_notes
%undefine __cmake_in_source_build

Name:           contour
Version:        0.3.1.200
Release:        1%{?dist}
Summary:        Modern C++ Terminal Emulator

License:        ASL 2.0
URL:            https://github.com/contour-terminal/%{name}
Source0:        https://github.com/contour-terminal/contour/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  harfbuzz-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconf
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  catch-devel
BuildRequires:  range-v3-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  fmt-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  termbench-pro-devel
BuildRequires:  libunicode-devel

Requires:       libunicode
Requires:       termbench-pro
Requires:       fontconfig
Requires:       freetype
Requires:       harfbuzz
Requires:       kf5-kwindowsystem
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       yaml-cpp

%description
contour is a modern terminal emulator, for everyday use.
It is aiming for power users with a modern feature mindset.

%prep
%setup -q -n %{name}-%{version}

%build
cmake . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCONTOUR_BLUR_PLATFORM_KWIN=ON \
    -DPEDANTIC_COMPILER=ON \
    -DPEDANTIC_COMPILER_WERROR=ON \
    -B build \
    -GNinja
cd build
%ninja_build

%install
cd build
%ninja_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
./build/src/crispy/crispy_test
./build/src/terminal/terminal_test


%files
%license LICENSE.txt
%doc README.md Changelog.md CONTRIBUTING.md TODO.md
%{_bindir}/contour
%{_datadir}/applications/%{name}.desktop


%changelog

