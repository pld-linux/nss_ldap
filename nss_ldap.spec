# $Revision: 1.23 $Date: 2000-11-08 21:25:05 $
#
# Conditional builds:	
# openldap1 - build with openldap < 2.0.0
#
Summary:	LDAP Name Service Switch Module
Name:		nss_ldap
Version:	122
Release:	0.1
License:	LGPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
URL:		http://www.padl.com/nss_ldap.html
%{!?openldap1:BuildRequires: openldap-devel >= 2.0.0}
%{?openldap1:BuildRequires:  openldap-devel <  2.0.0}
%{?openldap1:BuildRequires:  openldap-devel >  1.2.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%prep
%setup -q

%build
%{__make} -f Makefile.linux%{!?openldap1:.openldap2} \
	GCCFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -Wall -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

install libnss_ldap-*.so $RPM_BUILD_ROOT/lib/

gzip -9nf ANNOUNCE BUGS ChangeLog README CONTRIBUTORS nsswitch* rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(0755,root,root) /lib/*.so
