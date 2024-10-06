#
# Conditional build:
%bcond_without	libtracefs	# libtracefs support
%bcond_without	static_libs	# static libraries
%bcond_without	systemd		# systemd services
#
Summary:	Manage "libnvdimm" subsystem devices (Non-volatile Memory)
Summary(pl.UTF-8):	Zarządzanie urządzeniami podsystemu "libnvdimm" (pamięci nieulotnej)
Name:		ndctl
Version:	79
Release:	1
License:	LGPL v2.1+ (libraries), GPL v2+ with CC0 and MIT parts (utilities)
Group:		Applications/System
#Source0Download: https://github.com/pmem/ndctl/releases
Source0:	https://github.com/pmem/ndctl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bb2d9f612112b6496117551dc4e3d654
URL:		https://pmem.io/ndctl/
# or asciidoctor instead of asciidoc+xmlto
BuildRequires:	asciidoc
BuildRequires:	glibc-devel >= 6:2.28
BuildRequires:	iniparser-devel
BuildRequires:	json-c-devel
BuildRequires:	keyutils-devel
BuildRequires:	kmod-devel
%if %{with libtracefs}
BuildRequires:	libtraceevent-devel
BuildRequires:	libtracefs-devel >= 1.2.0
%endif
BuildRequires:	libuuid-devel
BuildRequires:	linux-libc-headers >= 7:4.15
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
%{?with_systemd:BuildRequires:	systemd-devel}
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

%package -n cxl
Summary:	Manage CXL devices
Summary(pl.UTF-8):	Zarządzanie urządzeniami CXL
License:	GPL v2+ with CC0 and MIT parts (utilities)
Group:		Applications/System
Requires:	cxl-libs = %{version}-%{release}
Requires:	libtracefs-devel >= 1.2.0

%description -n cxl
The cxl utility provices enumeration and provisioning commands for
CXL platforms.

%description -n cxl -l pl.UTF-8
Narzędzie cxl udostępnia polecenia do numerowania i zaopatrywania
dla platform CXL.

%package -n bash-completion-cxl
Summary:	Bash completion for cxl command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia cxl
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
Requires:	cxl = %{version}-%{release}

%description -n bash-completion-cxl
Bash completion for cxl command.

%description -n bash-completion-cxl -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia cxl.

%package -n cxl-libs
Summary:	Management library for CXL devices
Summary(pl.UTF-8):	Biblioteka zarządzająca urządzeniami CXL
License:	LGPL v2.1+
Group:		Libraries

%description -n cxl-libs
Management library for CXL devices.

%description -n cxl-libs -l pl.UTF-8
Biblioteka zarządzająca urządzeniami CXL.

%package -n cxl-devel
Summary:	Header fiels for cxl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cxl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	cxl-libs = %{version}-%{release}
Requires:	libuuid-devel

%description -n cxl-devel
Header fiels for cxl library.

%description -n cxl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cxl.

%package -n cxl-static
Summary:	Static cxl library
Summary(pl.UTF-8):	Statyczna biblioteka cxl
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n cxl-static
Static cxl library.

%description -n cxl-static -l pl.UTF-8
Statyczna biblioteka cxl.

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

%package -n bash-completion-daxctl
Summary:	Bash completion for daxctl command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia daxctl
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
Requires:	daxctl = %{version}-%{release}

%description -n bash-completion-daxctl
Bash completion for daxctl command.

%description -n bash-completion-daxctl -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia daxctl.

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

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Dasciidoctor=disabled \
	-Dbashcompletiondir=%{bash_compdir} \
	%{!?with_libtracefs:-Dlibtracefs=disabled} \
	%{!?with_systemd:-Dsystemd=disabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n cxl-libs -p /sbin/ldconfig
%postun	-n cxl-libs -p /sbin/ldconfig

%post	-n daxctl-libs -p /sbin/ldconfig
%postun	-n daxctl-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ndctl
%dir %{_sysconfdir}/ndctl
%dir %{_sysconfdir}/ndctl/keys
%dir %{_sysconfdir}/ndctl.conf.d
%config(noreplace) %verify(not md5 mtime size)  %{_sysconfdir}/ndctl.conf.d/monitor.conf
%config(noreplace) %verify(not md5 mtime size)  %{_sysconfdir}/ndctl.conf.d/ndctl.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/nvdimm-security.conf
%if %{with systemd}
%{systemdunitdir}/ndctl-monitor.service
%endif
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

%files -n cxl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxl
%if %{with systemd}
%{systemdunitdir}/cxl-monitor.service
%endif
%{_mandir}/man1/cxl.1*
%{_mandir}/man1/cxl-*.1*

%files -n bash-completion-cxl
%defattr(644,root,root,755)
%{bash_compdir}/cxl

%files -n cxl-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcxl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcxl.so.1

%files -n cxl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcxl.so
%{_includedir}/cxl
%{_pkgconfigdir}/libcxl.pc
%{_mandir}/man3/cxl_new.3*
%{_mandir}/man3/libcxl.3*

%if %{with static_libs}
%files -n cxl-static
%defattr(644,root,root,755)
%{_libdir}/libcxl.a
%endif

%files -n daxctl
%defattr(644,root,root,755)
%doc daxctl/daxctl.example.conf
%attr(755,root,root) %{_bindir}/daxctl
%dir %{_sysconfdir}/daxctl.conf.d
%{_datadir}/daxctl
/lib/udev/rules.d/90-daxctl-device.rules
%if %{with systemd}
%{systemdunitdir}/daxdev-reconfigure@.service
%endif
%{_mandir}/man1/daxctl.1*
%{_mandir}/man1/daxctl-*.1*

%files -n bash-completion-daxctl
%defattr(644,root,root,755)
%{bash_compdir}/daxctl

%files -n daxctl-libs
%defattr(644,root,root,755)
%doc COPYING README.md LICENSES/other/{CC0-1.0,MIT}
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
