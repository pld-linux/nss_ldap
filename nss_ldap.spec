# $Revision: 1.25 $Date: 2000-12-23 00:48:46 $
#
# Conditional builds:	
# --with openldap1 - build with openldap < 2.0.0
#
Summary:	LDAP Name Service Switch Module
Name:		nss_ldap
Version:	123
Release:	1
License:	LGPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
URL:		http://www.padl.com/nss_ldap.html
%{!?bcond_on_openldap1:BuildRequires: openldap-devel >= 2.0.0}
%{?bcond_on_openldap1:BuildRequires:  openldap-devel <  2.0.0}
%{?bcond_on_openldap1:BuildRequires:  openldap-devel >  1.2.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%prep
%setup -q

%build
%{__make} -f Makefile.linux%{!?bcond_on_openldap1:.openldap2} \
	GCCFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} -Wall -fPIC"

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
