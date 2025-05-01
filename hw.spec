Name:       hw
Version:    1.3
Release:    %autorelease
Summary:    Most simple RPM package
License:    FIXME
Source0: https://github.com/Mormacill/hw/archive/refs/tags/%{version}.tar.gz
BuildRequires: gcc

%description
This is my first RPM package, which does say Hello World.

%prep
%setup -q

%build
gcc -g -o hw hw.c

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hw %{buildroot}/usr/bin/hw

%files
/usr/bin/hw

%changelog
%autochangelog
