Summary:	Ambisonic encoding / decoding and binauralization library
Summary(pl.UTF-8):	Biblioteka kodowania/dekodowania dźwięku sferycznego Ambisonic i binauralnego
Name:		spatialaudio
Version:	0.4.0
Release:	1
License:	LGPL v2.1+ or commercial
Group:		Libraries
#Source0Download: https://github.com/videolan/libspatialaudio/releases
Source0:	https://github.com/videolan/libspatialaudio/archive/refs/tags/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	d8ff822b4af87cb3c57d5d677331bdd3
Patch0:		%{name}-install.patch
URL:		https://github.com/videolan/libspatialaudio
BuildRequires:	cmake >= 3.23
BuildRequires:	libmysofa-devel
BuildRequires:	libstdc++-devel >= 6:5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libspatialaudio is an open-source and cross-platform C++ library for
Ambisonic encoding and decoding, filtering and binaural rendering. It
is targetted to render High-Order Ambisonic (HOA) and VR/3D audio
samples in multiple environments, from headphones to classic
loudspeakers. Its binaural rendering can be used for classical 5.1/7.1
spatial channels as well as Ambisonics inputs.

%description -l pl.UTF-8
libspatialaudio to wieloplatformowa, mająca otwarte źródła biblioteka
C++ do kodowania i dekodowania sferycznego Ambisonic oraz filtrowania
i renderowania binauralnego. Celem jest renderowanie próbek
dźwiękowych HOA (High-Order Ambisonic) i VR/3D w wielu środowiskach,
od słuchawek do klasycznych głośników. Renderowanie binauralne może
być używane do klasycznych kanałów przestrzennych 5.1/7.1, jak i
wejść Ambisonics.

%package devel
Summary:	Header files for spatialaudio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki spatialaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmysofa-devel
Requires:	libstdc++-devel >= 6:5
Requires:	zlib-devel

%description devel
Header files for spatialaudio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki spatialaudio.

%prep
%setup -q -n libspatialaudio-%{version}
%patch -P0 -p1

%{__sed} -ne '1,/^===/ p' LICENSE > COPYING

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libspatialaudio.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libspatialaudio.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspatialaudio.so
%{_includedir}/spatialaudio
%{_pkgconfigdir}/spatialaudio.pc
