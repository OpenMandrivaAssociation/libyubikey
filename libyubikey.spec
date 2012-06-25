%define	major 0
%define libname	%mklibname yubikey %{major}
%define develname %mklibname -d yubikey

Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Name:		libyubikey
Version:	1.9
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/yubico-c/
Source0:	http://yubico-c.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubico-c.googlecode.com/files/%{name}-%{version}.tar.gz.sig
BuildRequires:	autoconf automake libtool
Patch0:		libyubikey-1.9-am-progs.patch

%description
Low-level library for decrypting and parsing Yubikey One-Time Passwords (OTP),
for C.

%package -n	%{libname}
Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Group:          System/Libraries

%description -n	%{libname}
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{develname}
Summary:	Static library and header files for the libyubikeyt library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{develname}
Low-level library for decrypting and parsing Yubikey One-Time Passwords (OTP),
for C.

This package contains the static libyubikey library and its header files.

%package	tools
Summary:	Command line tools for libyubikey
Group:          System/Libraries

%description	tools
Low-level library for decrypting and parsing Yubikey One-Time Passwords (OTP),
for C.

This package contains various tools for libyubikey.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build
libtoolize -f -c
autoreconf -fis

%configure2_5x

%make

%install
%makeinstall_std

# rename the too generic file names
mv %{buildroot}%{_bindir}/modhex %{buildroot}%{_bindir}/libyubikey-modhex
mv %{buildroot}%{_bindir}/ykgenerate %{buildroot}%{_bindir}/libyubikey-ykgenerate
mv %{buildroot}%{_bindir}/ykparse %{buildroot}%{_bindir}/libyubikey-ykparse

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so

%files tools
%{_bindir}/libyubikey-modhex
%{_bindir}/libyubikey-ykgenerate
%{_bindir}/libyubikey-ykparse
