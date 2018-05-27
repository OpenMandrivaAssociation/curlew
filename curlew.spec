Name:    curlew
Version: 0.2.5
Release: 1
Summary: Curlew multimedia converter
License: Waqf
Url:     https://curlew.sourceforge.io/
#Url:    https://github.com/chamfay/Curlew
Source:  https://sourceforge.net/projects/%{name}/files/%{name}-%{version}/%{name}-%{version}.tar.gz
Group:   Video
BuildArch:	noarch
BuildRequires: python xdg-utils python-setuptools intltool imagemagick
BuildRequires: librsvg
Requires:      ffmpeg mencoder python xdg-utils ffmpeg
#BuildRequires: python-gobject3-devel
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:      python-gi

%description
Easy to use, Free and Open-Source Multimedia converter for Linux.

%prep
%setup -q

%build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot} --optimize=2

%files
%{_bindir}/curlew
%{python_sitelib}/curlew*
%{_datadir}/applications/curlew.desktop
%{_datadir}/doc/curlew
%{_datadir}/icons/hicolor/scalable/apps/curlew.svg
%{_datadir}/icons/hicolor/*/apps/curlew.png
%{_datadir}/curlew
%{_datadir}/pixmaps/curlew.svg
