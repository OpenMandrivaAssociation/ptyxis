%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

#define _disable_ld_no_undefined 1
#define _disable_lto 1

Name:           ptyxis
Version:        48.5
Release:        1
Summary:        A terminal for GNOME with first-class support for containers
License:        GPL-3.0-or-later
URL:            https://www.gnome.org
Source:         https://download.gnome.org/sources/ptyxis/48/ptyxis-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(vte-2.91-gtk4)

%description
Ptyxis is a terminal for GNOME with first-class support for containers.

%prep
%autosetup -p1

%build
#export CC=gcc
#export CXX=g++
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%{_bindir}/ptyxis
%{_libexecdir}/ptyxis-agent
%{_datadir}/applications/org.gnome.Ptyxis.desktop
%{_datadir}/dbus-1/services/org.gnome.Ptyxis.service
%{_datadir}/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Ptyxis.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Ptyxis-symbolic.svg
%{_mandir}/man1/ptyxis.1.*
%{_datadir}/metainfo/org.gnome.Ptyxis.metainfo.xml
