#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	FXScintilla - Scintilla Editor Widget for FOX
Name:		fxscintilla
Version:	1.63
Release:	0.1
License:	LGPL
Group:		X11/Development/Libraries
Source0:	http://download.savannah.nongnu.org/releases/fxscintilla/%{name}-%{version}.tar.gz
# Source0-md5:	d33ffcc6066efa2758271f6a16645327
URL:		http://savannah.gnu.org/projects/fxscintilla/
BuildRequires:	fox-devel >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FXScintilla is an implementation of the Scintilla Widget Editor for
the FOX Graphical User Interface toolkit. This package includes the
library itself.

%package devel
Summary:	Header files for FXScintilla library	
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fox-devel >= 1.4

%description devel
Header files for FXScintilla library.

%description devel -l pl
Pliki nag��wkowe bilioteki FXScintilla.

%package static
Summary:	Static FXScintilla libraries
Summary(pl):	Statyczne biblioteki FXScintilla
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FXScintilla libraries.

%description static -l pl
Statyczne biblioteki FXScintilla.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__automake}
%configure \
	--enable-nolexer \
	--enable-shared \
	--with-fox-1-4 \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc scintilla/doc
%{_includedir}/fxscintilla
%{_libdir}/lib*.so
%{_libdir}/lib*.la

%if %{with static_libs}
%files static
%{_libdir}/lib*.a
%endif
