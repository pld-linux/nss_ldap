# $Revision: 1.2 $
Summary: LDAP Name Service Switch Module
Name: nss_ldap
Version: 85
Release: 1
Source0: ftp://ftp.padl.com/pub/nss_ldap-%{version}.tar.gz
Patch0: nss_ldap-makefile.patch
URL: http://www.padl.com/
Copyright: LGPL
Group: System Environment/Base
BuildRequires: openldap-devel 
BuildRoot: /var/tmp/%{name}-root

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.

%prep
%setup -q

%build
make -f Makefile.linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib
install libnss_ldap-2.1.so $RPM_BUILD_ROOT/lib/libnss_ldap-2.1.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) /lib/*.so
%doc ANNOUNCE BUGS COPYING.LIB ChangeLog README README.LINUX 
