Summary:	AACRAID Storage Management software
Summary(pl):	Oprogramowanie do zarządzania macierzami AACRAID
Name:		afaapps
Version:	2.6
Release:	1
License:	BSD
Group:		Base
Source0:	http://domsch.com/linux/aacraid/%{name}-%{version}-0.tar.gz
# Source0-md5:	509565c909098646242172397aba5157
URL:		http://domsch.com/linux/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
AACRAID Storage Management software.

%description -l pl
Oprogramowanie do zarządzania macierzami AACRAID.

%prep
%setup -q -T -c
tar xzf %{SOURCE0} --exclude='/dev/afa*'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install usr/sbin/afacli $RPM_BUILD_ROOT%{_sbindir}/dptutil

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dev/MAKEDEV.afa
%attr(755,root,root) %{_sbindir}/*
