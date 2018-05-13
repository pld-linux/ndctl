#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Manage "libnvdimm" subsystem devices (Non-volatile Memory)
Summary(pl.UTF-8):	Zarządzanie urządzeniami podsystemu "libnvdimm" (pamięci nieulotnej)
Name:		ndctl
Version:	60.1
Release:	1
License:	LGPL v2.1+ (libraries), GPL v2+ with CC0 and MIT parts (utilities)
Group:		Applications/System
#Source0Download: https://github.com/pmem/ndctl/releases
Source0:	https://github.com/pmem/ndctl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b67e154bf6cf6e34ac8c43bbae85952e
URL:		http://pmem.io/ndctl/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	json-c-devel
BuildRequires:	kmod-devel
BuildRequires:	libuuid-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	udev-devel
BuildRequires:	xmlto
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for managing the "libnvdimm" subsystem. The "libnvdimm"
subsystem defines a kernel device model and control message interface
for platform NVDIMM resources like those defined by the ACPI 6+ NFIT
(NVDIMM Firmware Interface Table).

%description -l pl.UTF-8
Narzędzia do zarządzania podsystemem "libnvdimm". Podsystem ten
definiuje model urządzeń jądra i interfejs komunikatów sterujących dla
specyficznych dla platformy zasobów NVDIMM, takich jak zdefiniowane w
ACPI 6+ NFIT (NVDIMM Firmware Interface Table).

%package -n bash-completion-ndctl
Summary:	Bash completion for ndctl command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia ndctl
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-ndctl
Bash completion for ndctl command.

%description -n bash-completion-ndctl -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia ndctl.

%package libs
Summary:	Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
Summary(pl.UTF-8):	Biblioteka zarządzająca do urządzeń podsystemu "libnvdimm" (pamięci nieulotnej)
License:	LGPL v2.1+
Group:		Libraries
Requires:	daxctl-libs = %{version}-%{release}

%description libs
Management library for "libnvdimm" subsystem devices (Non-volatile
Memory).

%description libs -l pl.UTF-8
Biblioteka zarządzająca do urządzeń podsystemu "libnvdimm"
(Non-volatile Memory - pamięci nieulotnej).

%package devel
Summary:	Header files for ndctl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ndctl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	daxctl-devel = %{version}-%{release}

%description devel
Header files for ndctl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ndctl.

%package static
Summary:	Static ndctl library
Summary(pl.UTF-8):	Statyczna biblioteka ndctl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ndctl library.

%description static -l pl.UTF-8
Statyczna biblioteka ndctl.

%package -n daxctl
Summary:	Manage Device-DAX instances
Summary(pl.UTF-8):	Zarządzanie instancjami Device-DAX
License:	GPL v2+ with CC0 and MIT parts (utilities)
Group:		Applications/System
Requires:	daxctl-libs = %{version}-%{release}

%description -n daxctl
The daxctl utility provides enumeration and provisioning commands for
the Linux kernel Device-DAX facility. This facility enables DAX
mappings of performance/feature differentiated memory without need of
a filesystem.

%description -n daxctl -l pl.UTF-8
Narzędzie daxctl udostępnia polecenia do numerowania i zaopatrywania
funkcji Device-DAX jądra Linuksa. Funkcja ta włącza odwzorowanie DAX
pamięci o zróżnicowanej wydajności/funkcjonalności bez potrzeby
systemu plików.

%package -n daxctl-libs
Summary:	Management library for "Device DAX" devices
Summary(pl.UTF-8):	Biblioteka zarządzająca do urządzeń "Device DAX"
License:	LGPL v2.1+
Group:		Libraries

%description -n daxctl-libs
Device DAX is a facility for establishing DAX mappings of
performance/feature-differentiated memory. daxctl-libs provides an
enumeration/control API for these devices.

%description -n daxctl-libs -l pl.UTF-8
Device DAX to funkcja ustanawiająca odwzorowania DAX pamięci o
zróżnicowanej wydajności/funkcjonalności. Biblioteka daxctl-libs
dostarcza API do numerowania i kontroli tych urządzeń.

%package -n daxctl-devel
Summary:	Header fiels for daxctl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki daxctl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	daxctl-libs = %{version}-%{release}
Requires:	libuuid-devel

%description -n daxctl-devel
Header fiels for daxctl library.

%description -n daxctl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki daxctl.

%package -n daxctl-static
Summary:	Static daxctl library
Summary(pl.UTF-8):	Statyczna biblioteka daxctl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n daxctl-static
Static daxctl library.

%description -n daxctl-static -l pl.UTF-8
Statyczna biblioteka daxctl.

%prep
%setup -q

echo '%{version}' >version

%build
./git-version-gen
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-bash-completion-dir=%{bash_compdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n daxctl-libs -p /sbin/ldconfig
%postun	-n daxctl-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md licenses/{BSD-MIT,CC0}
%attr(755,root,root) %{_bindir}/ndctl
%{_mandir}/man1/ndctl.1*
%{_mandir}/man1/ndctl-*.1*

%files -n bash-completion-ndctl
%defattr(644,root,root,755)
%{bash_compdir}/ndctl

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libndctl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libndctl.so.6

%files devel
%attr(755,root,root) %{_libdir}/libndctl.so
%defattr(644,root,root,755)
%{_includedir}/ndctl
%{_pkgconfigdir}/libndctl.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libndctl.a
%endif

%files -n daxctl
%defattr(644,root,root,755)
%doc licenses/{BSD-MIT,CC0}
%attr(755,root,root) %{_bindir}/daxctl
%{_mandir}/man1/daxctl.1*
%{_mandir}/man1/daxctl-*.1*

%files -n daxctl-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaxctl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdaxctl.so.1

%files -n daxctl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaxctl.so
%{_includedir}/daxctl
%{_pkgconfigdir}/libdaxctl.pc

%if %{with static_libs}
%files -n daxctl-static
%defattr(644,root,root,755)
%{_libdir}/libdaxctl.a
%endif
