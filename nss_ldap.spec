# $Revision: 1.12 $Date: 2000-03-29 22:17:38 $
Summary:	LDAP Name Service Switch Module
Name:		nss_ldap
Version:	107
Release:	1
License:	LGPL
Group:		Base
Group(pl):	Bazowe
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	openldap-devel 
BuildRoot:	/tmp/%{name}-%{version}-root

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%prep
%setup -q

%build
make -f Makefile.linux GCCFLAGS="$RPM_OPT_FLAGS -Wall -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib
install libnss_ldap-*.so $RPM_BUILD_ROOT/lib/

strip --strip-unneeded $RPM_BUILD_ROOT/lib/*

gzip -9nf ANNOUNCE BUGS ChangeLog README CONTRIBUTORS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) /lib/*.so
%doc {ANNOUNCE,BUGS,ChangeLog,README,CONTRIBUTORS}.gz
