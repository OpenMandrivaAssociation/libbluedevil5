%define major	5
%define libname	%mklibname bluedevil %{major}
%define devname	%mklibname bluedevil -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Qt-based library written in C++ to handle all Bluetooth functionality
Name:		libbluedevil5
Group:		Graphical desktop/KDE
Version:	5.2.2
Release:	1
License:	LGPLv2+
Url:		https://projects.kde.org/projects/playground/libs/libname
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/libbluedevil-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	bluez-devel
BuildRequires:	ninja
BuildRequires:	extra-cmake-modules5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)

%description
Qt-based library written in C++ to handle all Bluetooth functionality.

%package -n %{libname}
Summary:	Bluedevil Runtime library
Group:		System/Libraries

%description -n %{libname}
Qt-based library written in C++ to handle all Bluetooth functionality.

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libbluedevil-devel < 1.9.3-2

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%prep
%setup -qn libbluedevil-%{version}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

%files -n %{libname}
%{_libdir}/libbluedevil.so.%{major}*

%files -n %{devname}
%{_includedir}/bluedevil
%{_libdir}/libbluedevil.so
%{_libdir}/pkgconfig/bluedevil.pc

