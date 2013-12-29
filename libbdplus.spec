#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	BD+ support library for Blu-ray playback
Summary(pl.UTF-8):	Biblioteka obsługująca BD+ w celu odtwarzania płyt Blu-ray
Name:		libbdplus
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.videolan.org/pub/videolan/libbdplus/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	4cf74020b91aafa33075e8ceef4d0e40
URL:		http://www.videolan.org/developers/libbdplus.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libaacs-devel >= 0.7.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libbdplus is a research project to implement the BD+ System
Specifications. This research project provides, through an open-source
library, a way to understand how the BD+ works.

%description -l pl
libbdplus to projekt badawczy mający na celu implementację
specyfikacji systemu BD. Projekt ten, poprzez bibliotekę o otwartych
źródłach, pozwala zrozumieć, jak działa BD+.

%package devel
Summary:	Header files for libbdplus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libbdplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libbdplus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libbdplus.

%package static
Summary:	Static libbdplus library
Summary(pl.UTF-8):	Statyczna biblioteka libbdplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbdplus library.

%description static -l pl.UTF-8
Statyczna biblioteka libbdplus.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%attr(755,root,root) %{_libdir}/libbdplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbdplus.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbdplus.so
%{_includedir}/libbdplus
%{_pkgconfigdir}/libbdplus.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbdplus.a
%endif
