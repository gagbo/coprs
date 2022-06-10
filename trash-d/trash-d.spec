Summary: A near drop-in replacement for rm that uses the trash bin
Name: trash-d
Version: 17
Release: 1%{?dist}
URL: https://github.com/rushsteve1/trash-d
License: MIT
Source: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  dub
BuildRequires:  ldc
BuildRequires:  gcc
BuildRequires:  libgphobos-static

%description
A near drop-in replacement for rm that uses the trash bin.

%prep
%setup -q -n %{name}-%{version}

%build
dub build -n
gzip ./trash.man

%install
install -Dm 755 ./trash ${RPM_BUILD_ROOT}/usr/bin/trash
install -Dm 444 ./trash.man.gz ${RPM_BUILD_ROOT}/usr/share/man1/trash.1.gz

%check
dub test

%files
%license LICENSE
%doc MANUAL.md README.md
%{_bindir}/trash
%{_mandir}/trash.1.*

%changelog
