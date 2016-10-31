Name:    curlew
Version: 0.2.2
Release: 1
Summary: Curlew multimedia converter
License: Waqf
Url:     http://gtk-apps.org/content/show.php/Curlew?content=155664&PHPSESSID=e679b8e6ba032e740d2a654d05d3ac5b
#Url:    https://github.com/chamfay/Curlew
Source:  curlew-%{version}.tar.gz
Group:   Video
BuildArch:	noarch
BuildRequires: python xdg-utils python-setuptools python-distutils-extra intltool imagemagick
Requires:      ffmpeg mencoder python xdg-utils ffmpeg
BuildRequires: python-gobject3-devel
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
