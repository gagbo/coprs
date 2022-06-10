Summary: A near drop-in replacement for rm that uses the trash bin
Name: trash-d
Version: 17
Release: 1%{?dist}
URL: https://github.com/rushsteve1/trash-d
License: MIT
Source: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  dub
BuildRequires:  ldc

%description
A near drop-in replacement for rm that uses the trash bin.

%prep
%setup -q -n %{name}-%{version}

%build
dub build -n

%install
cp ./trash-d %{_bindir}/trash-d

%check
dub test

%files
%license LICENSE
%doc MANUAL.md README.md
%{_bindir}/trash-d

%changelog
