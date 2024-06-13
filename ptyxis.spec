%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           ptyxis
Version:        46.3
Release:        1
Summary:        A terminal for GNOME with first-class support for containers
License:        GPL-3.0-or-later
URL:            https://www.gnome.org
Source:         https://download.gnome.org/sources/ptyxis/46/ptyxis-%{version}.tar.xz

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
%meson
%meson_build

%install
%meson_instal

%files
