%define oversion 2011-08-R1
%define version %(echo %{oversion}| tr - .)

Name:		spectools
Summary:	IEEE 802.11 wireless LAN sniffer
Group:		Networking/Other
Version:	%{version}
Release:	1
License:	GPL
Url:		https://www.kismetwireless.net
Source0:	http://www.kismetwireless.net/code/%{name}-%{oversion}.tar.gz
BuildRequires:	bison
BuildRequires:	flex 
BuildRequires:	glib-devel
BuildRequires:	gpsd-devel gmp-devel expat-devel
BuildRequires:	imagemagick-devel
BuildRequires:	ncurses-devel 
BuildRequires:	pcap-devel
BuildRequires:	wget
Requires:       wget
Requires:       wireless-tools

%description
Spectools is a set of utilities for using various spectrum analyzer hardware.
It supports the suite of Wi-Spy devices (original, 24x, 24x2, DBX, DBX2, 900, 24i)
by Metageek LLC and the Ubertooth. Spectools includes userspace drivers for
the hardware itself, a graphing UI built GTK and Cairo, network protocols
for remote device capture, and simple utilities for developing additional tools. 

%prep
%setup -qn %{name}-%{oversion}
    
%build
%configure2_5x \
    CXXFLAGS="%{optflags} -D__STDC_FORMAT_MACROS"
    
%make

%install
%makeinstall_std

%files
%doc GPL README
%{_bindir}/*
