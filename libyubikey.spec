%define	major 0
%define libname		%mklibname yubikey
%define devname 	%mklibname yubikey -d
%define oldlibname	%mklibname yubikey

Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Name:		libyubikey
Version:	1.13
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://developers.yubico.com/yubico-c/
Source0:	https://developers.yubico.com/yubico-c/Releases/%{name}-%{version}.tar.gz
#Patch0:	libyubikey-1.9-am-progs.patch

BuildRequires:	libtool

%description
Low-level library for decrypting and parsing Yubikey One-Time Passwords (OTP),
for C.

%package -n	%{libname}
Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Group:		System/Libraries
Obsoletes:	%{oldlibname} <= %{EVRD}

%description -n	%{libname}
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

%files -n %{libname}
%{_libdir}/libyubikey.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Static library and header files for the libyubikeyt library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%files -n %{devname}
%license COPYING
%{_includedir}/*
%{_libdir}/*.so

#----------------------------------------------------------------------------

%package	tools
Summary:	Command line tools for libyubikey
Group:	  System/Libraries

%description	tools
This package contains various tools for libyubikey.

%files tools
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/modhex
%{_bindir}/ykparse
%{_bindir}/ykgenerate
%{_mandir}/man1/ykgenerate.1*
%{_mandir}/man1/ykparse.1*
%{_mandir}/man1/modhex.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# rename the too generic file names
#mv %{buildroot}%{_bindir}/modhex %{buildroot}%{_bindir}/libyubikey-modhex
#mv %{buildroot}%{_bindir}/ykgenerate %{buildroot}%{_bindir}/libyubikey-ykgenerate
#mv %{buildroot}%{_bindir}/ykparse %{buildroot}%{_bindir}/libyubikey-ykparse

