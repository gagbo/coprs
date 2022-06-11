Summary: A near drop-in replacement for rm that uses the trash bin
Name: trash-d
Version: 17
Release: 3%{?dist}
URL: https://github.com/rushsteve1/trash-d
License: MIT
Source: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  dub
BuildRequires:  ldc
BuildRequires:  libgphobos-static
BuildRequires:  pandoc

%description
A near drop-in replacement for rm that uses the trash bin.

%prep
%setup -q -n %{name}-%{version}

%build
dub build -n --compiler=ldmd2
pandoc -s -t man -o trash.man MANUAL.md
gzip ./trash.man

%install
install -Dm 755 ./trash ${RPM_BUILD_ROOT}/usr/bin/trash
install -Dm 444 ./trash.man.gz ${RPM_BUILD_ROOT}/usr/share/man/trash.1.gz

%check
dub test

%files
%license LICENSE
%doc MANUAL.md README.md
%{_bindir}/trash
%{_mandir}/trash.1.*

%changelog
* Sat Jun 11 2022 Gerry Agbobada <git@gagbo.net> - 17-3
- Remove gcc tooclhain from build requires

* Sat Jun 11 2022 Gerry Agbobada <git@gagbo.net> - 17-2
- Force usage of ldc to get a statically linked executable

* Fri Jun 10 2022 Gerry Agbobada <git@gagbo.net> - 17-1
- Initial version
