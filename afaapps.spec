Summary:	AACRAID Storage Management software
Summary(pl):	Oprogramowanie do zarz±dzania macierzami AACRAID
Name:		afaapps
Version:	2.7
Release:	1
License:	Dell
Group:		Base
Source0:	ftp://ftp.us.dell.com/scsi-raid/aacraid-util-rh8.0-i386.tar.gz
# Source0-md5:	06195cbabedef5983d2d06fa7cf2088a
Source1:	%{name}-LICENSE
URL:		http://domsch.com/linux/
BuildRequires:	rpm-utils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
AACRAID Storage Management software.

%description -l pl
Oprogramowanie do zarz±dzania macierzami AACRAID.

%prep
%setup -q -c

%build
install -d dev usr/sbin
rpm2cpio *.rpm | cpio -i

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install usr/sbin/afacli.bin $RPM_BUILD_ROOT%{_sbindir}/afacli
install %{SOURCE1} LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dev/MAKEDEV.afa LICENSE
%attr(755,root,root) %{_sbindir}/*
