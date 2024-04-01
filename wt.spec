%define devname %mklibname -d wt

Name: wt
Version: 4.10.3
Release: 4
Source0: https://github.com/emweb/wt/archive/%{version}/%{name}-%{version}.tar.gz
Summary: C++ Web toolkit
URL: https://webtoolkit.eu/
License: GPL; commercial licensing available
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: boost-devel

%description
Wt is a web GUI library in modern C++. Quickly develop highly interactive web
UIs with widgets, without having to write a single line of JavaScript. Wt
handles all request handling and page rendering for you, so you can focus on
functionality.

%prep
%autosetup -p1
%cmake \
	-DCMAKE_CXX_STANDARD=23 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%libpackages -D -d

cat >%{specpartsdir}/%{devname}.specpart <<"EOF"
%%%%package -n %{devname}
Summary:	Development files for Wt, the C++ Web toolkit
Group:		Development/C and C++
EOF
for i in $LIBPACKAGES; do
	echo "Requires: %%{mklibname $i} = %{EVRD}" >>%{specpartsdir}/%{devname}.specpart
done
cat >>%{specpartsdir}/%{devname}.specpart <<"EOF"
%%%%description -n %{devname}
Development files for Wt, the C++ Web toolkit

%%%%files -n %{devname}
%{_includedir}/Wt
%{_libdir}/cmake/wt
%{_libdir}/*.so
EOF

%files
%{_datadir}/Wt
%dir %{_sysconfdir}/wt
%config %{_sysconfdir}/wt/*
