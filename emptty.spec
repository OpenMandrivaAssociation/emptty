%global debug_package %{nil}

Name:		emptty
Version:	0.14.0
Release:	1
Source0:	https://github.com/tvrzna/emptty/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Dead sumple CLI Display Manager on TTY
URL:		https://github.com/tvrzna/emptty
License:	MIT
Group:		Window Manager/Display Manager
BuildRequires:	make
BuildRequires:	pkgconfig(pam)
BuildRequires:	pkgconfig(x11)
BuildRequires:  go
BuildRequires:  git

%description
%summary.

%prep
%autosetup -p1
tar -zxf %{S:1}

%build
make build

%install
make install-all DESTDIR=%{buildroot}
make install-config DESTDIR=%{buildroot}
make install-systemd DESTDIR=%{buildroot}
sed -i 's/system-login/system-auth/g' %{buildroot}%{_sysconfdir}/pam.d/emptty

%post
%systemd_post %{name}.service

%preun
%systemd_postun %{name}.service

%postun
%systemd_preun %{name}.service

%files
%{_bindir}/%{name}
%{_sysconfdir}/pam.d/%{name}
%{_sysconfdir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.1.zst
