Name:           bismuth
Version:        3.1.1
Release:        1%{?dist}
Summary:        KDE Plasma extension that lets you tile your windows automatically

License:        MIT
URL:            https://bismuth-forge.github.io/bismuth
Source0:        https://github.com/Bismuth-Forge/bismuth/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake ninja-build extra-cmake-modules npm
BuildRequires:  kf5-kconfigwidgets-devel qt5-qtbase-devel qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-qtsvg-devel 
BuildRequires:  qt5-qtfeedback-devel kf5-kcmutils-devel kf5-ki18n-devel kf5-kdeclarative-devel
BuildRequires:  kf5-kglobalaccel-devel kdecoration-devel

%description
KDE Plasma extension, that lets you tile your windows automatically and manage
them via keyboard, just like in classical tiling window managers

%prep
%autosetup

%build
%cmake_kf5 -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_TSC=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%dir %{_libdir}/qt5/plugins/kcms
%dir %{_datarootdir}/kpackage
%dir %{_datarootdir}/kpackage/kcms
%dir %{_libdir}/qt5/plugins/org.kde.kdecoration2
%dir %{_kf5_qmldir}/org/kde/bismuth
%dir %{_kf5_qmldir}/org/kde/bismuth/core
%{_datarootdir}/kservices5/
%{_datarootdir}/kwin/
%{_libdir}/qt5/plugins/org.kde.kdecoration2/bismuth_kdecoration.so
%{_libdir}/qt5/plugins/kcms/kcm_bismuth.so
%{_kf5_qmldir}/org/kde/bismuth/core/libbismuth_core.so
%{_kf5_qmldir}/org/kde/bismuth/core/qmldir
%{_datarootdir}/config.kcfg/bismuth_config.kcfg
%{_iconsdir}/hicolor/scalable/apps/bismuth.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-column.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-floating.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-monocle.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-quarter.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-spiral.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-spread.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-stair.svg
%{_iconsdir}/hicolor/16x16/status/bismuth-tile.svg
%{_iconsdir}/hicolor/22x22/categories/bismuth-kcm.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-column.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-floating.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-monocle.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-quarter.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-spiral.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-spread.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-stair.svg
%{_iconsdir}/hicolor/32x32/status/bismuth-tile.svg
%{_iconsdir}/hicolor/64x64/categories/bismuth-kcm.svg
%{_datadir}/kconf_update/bismuth_old_conf_ui.sh
%{_datadir}/kconf_update/bismuth_old_conf_ui.upd
%{_datadir}/kconf_update/bismuth_new_logger.upd
%{_datadir}/kconf_update/bismuth_shortcuts_category.upd
%{_datarootdir}/kpackage/kcms/kcm_bismuth/

%changelog
* Tue Jun 14 2022 Gerry Agbobada <git@gagbo.net> - 3.1.1-1
- Update to version 3.1.1
* Sun Jan 30 2022 João Capucho <jcapucho7 at gmail.com> - 2.3.0-1
- Update to version 2.3.0
* Tue Dec 07 2021 João Capucho <jcapucho7 at gmail.com> - 2.2.0-1
- First bismuth package
