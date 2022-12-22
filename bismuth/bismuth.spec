Name:           bismuth
Version:        3.1.4
Release:        2%{?dist}
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
%dir %{_qt5_plugindir}/kcms
%dir %{_kf5_datadir}/kpackage
%dir %{_kf5_datadir}/kpackage/kcms
%dir %{_qt5_plugindir}/org.kde.kdecoration2
%dir %{_qt5_qmldir}/org/kde/bismuth
%dir %{_qt5_qmldir}/org/kde/bismuth/core
%{_kf5_datadir}/kservices5/
%{_kf5_datadir}/kwin/scripts/bismuth/
%{_qt5_plugindir}/org.kde.kdecoration2/bismuth_kdecoration.so
%{_qt5_plugindir}/kcms/kcm_bismuth.so
%{_qt5_qmldir}/org/kde/bismuth/core/libbismuth_core.so
%{_qt5_qmldir}/org/kde/bismuth/core/qmldir
%{_kf5_datadir}/config.kcfg/bismuth_config.kcfg
%{_datadir}/icons/hicolor/scalable/apps/bismuth.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-column.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-floating.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-monocle.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-quarter.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-spiral.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-spread.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-stair.svg
%{_datadir}/icons/hicolor/16x16/status/bismuth-tile.svg
%{_datadir}/icons/hicolor/22x22/categories/bismuth-kcm.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-column.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-floating.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-monocle.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-quarter.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-spiral.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-spread.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-stair.svg
%{_datadir}/icons/hicolor/32x32/status/bismuth-tile.svg
%{_datadir}/icons/hicolor/64x64/categories/bismuth-kcm.svg
%{_kf5_datadir}/qlogging-categories5/bismuth.categories
%{_kf5_datadir}/kconf_update/bismuth_old_conf_ui.sh
%{_kf5_datadir}/kconf_update/bismuth_old_conf_ui.upd
%{_kf5_datadir}/kconf_update/bismuth_new_logger.upd
%{_kf5_datadir}/kconf_update/bismuth_shortcuts_category.upd
%{_kf5_datadir}/kpackage/kcms/kcm_bismuth/

%changelog
* Thu Dec 22 2022 Gerry Agbobada <git@gagbo.net> - 3.1.4-2
- Trigger rebuild
* Sat Sep 24 2022 Gerry Agbobada <git@gagbo.net> - 3.1.4-1
- Update to version 3.1.4
* Wed Jul 13 2022 Gerry Agbobada <git@gagbo.net> - 3.1.2-1
- Update to version 3.1.2
* Tue Jun 14 2022 Gerry Agbobada <git@gagbo.net> - 3.1.1-1
- Update to version 3.1.1
- Change the list of files installed
* Sun Jan 30 2022 João Capucho <jcapucho7 at gmail.com> - 2.3.0-1
- Update to version 2.3.0
* Tue Dec 07 2021 João Capucho <jcapucho7 at gmail.com> - 2.2.0-1
- First bismuth package
