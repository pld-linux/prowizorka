Summary:	RPM handler
Summary(pl):	narzêdzie do obs³ugi RPMów
Name:		prowizorka
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}.tar.gz
#BuildRequires:	bzip2-devel
#BuildRequires:	conflib-devel
BuildRequires:	db3-devel
BuildRequires:	db1-devel
#BuildRequires:	newt-devel
BuildRequires:	popt-devel
#BuildRequires:	postgresql-devel
BuildRequires:	rpm-devel
#BuildRequires:	slang-devel
#BuildRequires:	trurlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
prowizorka is a tool to allow easy installation of RPM packages.

%description -l pl
prowizorka jest narzêdziem które pozwala na ³atw± instalacjê
pakietów RPM.

%package BOOT
Summary:	prowizorka for bootdisk
Group:		Applications/System

%description BOOT

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install rpmmenlib/%{name} $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install gentocf/gentocf $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/sbin/*
