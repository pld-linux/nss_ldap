# $Revision: 1.18 $Date: 2000-09-12 13:57:37 $
Summary:	LDAP Name Service Switch Module
Name:		nss_ldap
Version:	113
Release:	2
License:	LGPL
Group:		Base
Group(pl):	Podstawowe
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	openldap-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%prep
%setup -q

%build
%{__make} -f Makefile.linux.openldap2 GCCFLAGS="$RPM_OPT_FLAGS -Wall -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib
install libnss_ldap-*.so $RPM_BUILD_ROOT/lib/

strip --strip-unneeded $RPM_BUILD_ROOT/lib/*

gzip -9nf ANNOUNCE BUGS ChangeLog README CONTRIBUTORS nsswitch* rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,BUGS,ChangeLog,README,CONTRIBUTORS}.gz nsswitch*.gz rfc*.gz
%attr(0755,root,root) /lib/*.so
