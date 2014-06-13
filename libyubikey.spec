%define	major 0
%define libname	%mklibname yubikey %{major}
%define devname %mklibname -d yubikey

Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Name:		libyubikey
Version:	1.9
Release:	7
Group:		System/Libraries
License:	BSD
Url:		http://code.google.com/p/yubico-c/
Source0:	http://yubico-c.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubico-c.googlecode.com/files/%{name}-%{version}.tar.gz.sig
Patch0:		libyubikey-1.9-am-progs.patch
BuildRequires:	libtool

%description
Low-level library for decrypting and parsing Yubikey One-Time Passwords (OTP),
for C.

%package -n	%{libname}
Summary:	Decrypting and parsing Yubikey One-Time Passwords Low-level library
Group:          System/Libraries

%description -n	%{libname}
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{devname}
Summary:	Static library and header files for the libyubikeyt library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%package	tools
Summary:	Command line tools for libyubikey
Group:          System/Libraries

%description	tools
This package contains various tools for libyubikey.

%prep
%setup -q
%apply_patches
libtoolize -f -c
autoreconf -fis

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

# rename the too generic file names
mv %{buildroot}%{_bindir}/modhex %{buildroot}%{_bindir}/libyubikey-modhex
mv %{buildroot}%{_bindir}/ykgenerate %{buildroot}%{_bindir}/libyubikey-ykgenerate
mv %{buildroot}%{_bindir}/ykparse %{buildroot}%{_bindir}/libyubikey-ykparse

%files -n %{libname}
%{_libdir}/libyubikey.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so

%files tools
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/libyubikey-modhex
%{_bindir}/libyubikey-ykgenerate
%{_bindir}/libyubikey-ykparse

