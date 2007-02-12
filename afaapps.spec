# TODO:
#	- afasnmp subpackage?
#
Summary:	AACRAID Storage Management software
Summary(pl.UTF-8):   Oprogramowanie do zarządzania macierzami AACRAID
Name:		afaapps
Version:	2.8
Release:	1
License:	Dell
Group:		Base
Source0:	ftp://ftp.us.dell.com/scsi-raid/afa-apps-snmp.2807420-A04.tar.gz
# Source0-md5:	3f70c523ebb97c9ef212eb49c3cdbb76
Source1:	%{name}-LICENSE
URL:		http://domsch.com/linux/
BuildRequires:	rpm-utils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
AACRAID Storage Management software.

%description -l pl.UTF-8
Oprogramowanie do zarządzania macierzami AACRAID.

%prep
%setup -q -c

%build
rpm2cpio *.rpm | cpio -i -d

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install usr/sbin/afacli $RPM_BUILD_ROOT%{_sbindir}/afacli
install %{SOURCE1} LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dev/MAKEDEV.afa LICENSE usr/sbin/getcfg.afa
%attr(755,root,root) %{_sbindir}/*
